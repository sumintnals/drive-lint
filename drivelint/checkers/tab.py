from ..models import Violation
from ..scanner import count_calls, find_builder_scopes

RULE_ID = "TAB-013"
MIN_TABS = 2
MAX_TABS = 4


def check(content: str, filename: str) -> list[Violation]:
    violations = []
    for scope in find_builder_scopes(content, "TabTemplate"):
        count = count_calls(scope.text, "addTab")
        if count < MIN_TABS or count > MAX_TABS:
            violations.append(
                Violation(
                    rule_id=RULE_ID,
                    severity="error",
                    file=filename,
                    line=scope.line,
                    message=(
                        f"TabTemplate 탭 개수가 {count}개입니다. "
                        f"{MIN_TABS}~{MAX_TABS}개 사이여야 합니다 (하드캡)."
                    ),
                )
            )
    return violations
