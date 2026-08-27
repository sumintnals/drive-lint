import re

from ..models import Violation
from ..scanner import find_builder_scopes

RULE_ID = "LIST-001"
_EMPTY_SECTION_HEADER = re.compile(r"SectionedItemList\.create\s*\([^,]+,\s*\"\"\s*\)")


def check(content: str, filename: str) -> list[Violation]:
    violations = []
    for scope in find_builder_scopes(content, "ListTemplate"):
        if _EMPTY_SECTION_HEADER.search(scope.text):
            violations.append(
                Violation(
                    rule_id=RULE_ID,
                    severity="error",
                    file=filename,
                    line=scope.line,
                    message="섹션이 있는 ListTemplate인데 섹션 헤더가 빈 문자열입니다.",
                )
            )
    return violations
