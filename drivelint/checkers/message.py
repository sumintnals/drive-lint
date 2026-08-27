import re

from ..models import Violation
from ..scanner import find_builder_scopes

RULE_ID = "MESSAGE-006"
_EMPTY_MESSAGE = re.compile(r"MessageTemplate\.Builder\s*\(\s*\"\"\s*\)")


def check(content: str, filename: str) -> list[Violation]:
    violations = []
    for scope in find_builder_scopes(content, "MessageTemplate"):
        if _EMPTY_MESSAGE.search(scope.text):
            line = scope.line
            violations.append(
                Violation(
                    rule_id=RULE_ID,
                    severity="error",
                    file=filename,
                    line=line,
                    message="MessageTemplate 본문 텍스트가 빈 문자열입니다.",
                )
            )
    return violations
