import re

from ..models import Violation
from ..scanner import find_builder_scopes

RULE_ID = "SIGNIN-014"
_KNOWN_METHODS = re.compile(
    r"\b(ProviderSignInMethod|PinSignInMethod|QRCodeSignInMethod|InputSignInMethod)\b"
)


def check(content: str, filename: str) -> list[Violation]:
    violations = []
    for scope in find_builder_scopes(content, "SignInTemplate"):
        if not _KNOWN_METHODS.search(scope.text):
            violations.append(
                Violation(
                    rule_id=RULE_ID,
                    severity="error",
                    file=filename,
                    line=scope.line,
                    message=(
                        "SignInTemplate에 알려진 로그인 방법"
                        "(Provider/Pin/QRCode/InputSignInMethod)이 보이지 않습니다."
                    ),
                )
            )
    return violations
