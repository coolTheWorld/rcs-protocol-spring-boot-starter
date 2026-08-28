"""检查仓库内 Markdown 的相对链接目标是否存在、是否有行尾空白。"""
import pathlib
import re
import sys

LINK = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")
problems = []
for path in sorted(pathlib.Path(".").rglob("*.md")):
    if ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    for number, line in enumerate(text.splitlines(), 1):
        if line != line.rstrip():
            problems.append(f"{path}:{number}: 行尾空白")
    for match in LINK.finditer(text):
        target = match.group(1)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target):
            continue
        if not (path.parent / target).exists():
            problems.append(f"{path}: 链接目标不存在 {target}")
print("\n".join(problems) if problems else "Markdown 检查通过")
sys.exit(1 if problems else 0)
