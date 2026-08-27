import re
from dataclasses import dataclass

_BUILDER_TOKEN = re.compile(r"\bBuilder\s*\(")
_BUILD_TOKEN = re.compile(r"\.build\s*\(\s*\)")


@dataclass(frozen=True)
class BuilderScope:
    text: str
    line: int  # 트리거가 된 `ClassName.Builder(` 호출의 1-indexed 줄 번호


def find_builder_scopes(content: str, class_name: str) -> list[BuilderScope]:
    trigger = re.compile(rf"\b{re.escape(class_name)}\.Builder\s*\(")
    scopes: list[BuilderScope] = []
    pos = 0

    while True:
        match = trigger.search(content, pos)
        if not match:
            break

        start = match.start()
        line = content.count("\n", 0, start) + 1
        depth = 1
        cursor = match.end()
        end = len(content)

        while depth > 0:
            next_build = _BUILD_TOKEN.search(content, cursor)
            if next_build is None:
                end = len(content)
                break
            next_builder = _BUILDER_TOKEN.search(content, cursor, next_build.start())
            if next_builder:
                depth += 1
                cursor = next_builder.end()
            else:
                depth -= 1
                cursor = next_build.end()
                if depth == 0:
                    end = next_build.end()

        scopes.append(BuilderScope(text=content[start:end], line=line))
        pos = end

    return scopes


def count_calls(scope_text: str, method_name: str) -> int:
    pattern = re.compile(rf"\.{re.escape(method_name)}\s*\(")
    return len(pattern.findall(scope_text))
