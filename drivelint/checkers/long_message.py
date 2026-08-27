import re

from ..models import Violation
from ..scanner import find_builder_scopes

RULE_ID = "LONG-MESSAGE-005"
_EMPTY_MESSAGE = re.compile(r"LongMessageTemplate\.Builder\s*\(\s*\"\"\s*\)")


def check(content: str, filename: str) -> list[Violation]:
    violations = []
    for scope in find_builder_scopes(content, "LongMessageTemplate"):
        if _EMPTY_MESSAGE.search(scope.text):
            violations.append(
                Violation(
                    rule_id=RULE_ID,
                    severity="error",
                    file=filename,
                    line=scope.line,
                    message="LongMessageTemplate 본문 텍스트가 빈 문자열입니다.",
                )
            )
    return violations
