import argparse
import sys
from pathlib import Path

from .checkers import grid, pane, tab
from .models import Violation

CHECKERS = [grid.check, pane.check, tab.check]


def iter_kotlin_files(root: Path):
    if root.is_file():
        if root.suffix == ".kt":
            yield root
        return
    yield from sorted(root.rglob("*.kt"))


def run_check(path_str: str) -> int:
    root = Path(path_str)
    if not root.exists():
        print(f"경로를 찾을 수 없습니다: {path_str}", file=sys.stderr)
        return 2

    violations: list[Violation] = []
    files_scanned = 0
    for kt_file in iter_kotlin_files(root):
        files_scanned += 1
        content = kt_file.read_text(encoding="utf-8")
        for checker in CHECKERS:
            violations.extend(checker(content, str(kt_file)))

    if files_scanned == 0:
        print(f"검사할 .kt 파일을 찾지 못했습니다: {path_str}")
        return 0

    if not violations:
        print(f"[drivelint] {files_scanned}개 파일 검사 완료, 위반 사항 없음")
        return 0

    for v in sorted(violations, key=lambda v: (v.file, v.line)):
        print(f"{v.file}:{v.line}: [{v.severity.upper()}] {v.rule_id} {v.message}")

    error_count = sum(1 for v in violations if v.severity == "error")
    warning_count = len(violations) - error_count
    print(
        f"\n[drivelint] {files_scanned}개 파일 검사, "
        f"{len(violations)}건 위반 (error {error_count}건, warning {warning_count}건)"
    )
    return 1 if error_count else 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="drivelint")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser(
        "check", help="Android Auto 프로젝트의 Design for Driving 가이드라인 위반을 검사합니다"
    )
    check_parser.add_argument("path", help="검사할 프로젝트 경로 또는 .kt 파일")

    args = parser.parse_args(argv)

    if args.command == "check":
        return run_check(args.path)

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
