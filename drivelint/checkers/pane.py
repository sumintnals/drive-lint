from ..models import Violation
from ..scanner import count_calls, find_builder_scopes

RULE_ID_EMPTY = "PANE-009"
RULE_ID_TOO_MANY = "PANE-010"
MAX_ROWS = 4


def check(content: str, filename: str) -> list[Violation]:
    violations = []
    for scope in find_builder_scopes(content, "Pane"):
        count = count_calls(scope.text, "addRow")

        if count == 0:
            violations.append(
                Violation(
                    rule_id=RULE_ID_EMPTY,
                    severity="error",
                    file=filename,
                    line=scope.line,
                    message="Pane에 정보 행(addRow)이 하나도 없습니다. 최소 1개가 필요합니다.",
                )
            )
        elif count > MAX_ROWS:
            violations.append(
                Violation(
                    rule_id=RULE_ID_TOO_MANY,
                    severity="error",
                    file=filename,
                    line=scope.line,
                    message=(
                        f"Pane 정보 행이 {count}개입니다. "
                        f"최대 {MAX_ROWS}개까지만 허용됩니다 (하드캡)."
                    ),
                )
            )
    return violations
