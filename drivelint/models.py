from dataclasses import dataclass


@dataclass(frozen=True)
class Violation:
    rule_id: str
    severity: str  # "error" (MUST / 하드캡) or "warning" (SHOULD)
    file: str
    line: int
    message: str
