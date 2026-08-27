from ..models import Violation
from ..scanner import count_calls, find_builder_scopes

RULE_ID = "GRID-003"
MAX_ITEMS = 6


def check(content: str, filename: str) -> list[Violation]:
    violations = []
    for scope in find_builder_scopes(content, "GridTemplate"):
        count = count_calls(scope.text, "addItem")
        if count > MAX_ITEMS:
            violations.append(
                Violation(
                    rule_id=RULE_ID,
                    severity="error",
                    file=filename,
                    line=scope.line,
                    message=(
                        f"GridTemplate 항목이 {count}개입니다. "
                        f"차종과 무관하게 최대 {MAX_ITEMS}개를 넘을 수 없습니다 (하드캡)."
                    ),
                )
            )
    return violations
