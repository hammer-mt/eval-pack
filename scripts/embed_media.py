#!/usr/bin/env python3
"""Inline local media referenced via src="..." into data: URIs.

Makes an eval pack a single self-contained file: run it once after writing
the HTML with plain file references. Skips data:, http(s):, and #.

Usage: python3 embed_media.py <pack.html>
"""
import base64
import mimetypes
import re
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: embed_media.py <pack.html>")
    path = Path(sys.argv[1])
    html = path.read_text()
    base = path.parent

    def repl(match: re.Match) -> str:
        src = match.group(2)
        if src.startswith(("data:", "http://", "https://", "#")):
            return match.group(0)
        file = Path(src) if Path(src).is_absolute() else (base / src)
        if not file.is_file():
            print(f"skip (not found): {src}")
            return match.group(0)
        mime = mimetypes.guess_type(file.name)[0] or "application/octet-stream"
        data = base64.b64encode(file.read_bytes()).decode()
        print(f"embedded {src} ({len(data) // 1024} KB as base64)")
        return f"{match.group(1)}data:{mime};base64,{data}{match.group(3)}"

    html = re.sub(r'(src=")([^"]+)(")', repl, html)
    path.write_text(html)

    size_mb = path.stat().st_size / 1e6
    note = " — over 15MB, consider downscaling media" if size_mb > 15 else ""
    print(f"{path.name}: {size_mb:.1f} MB total{note}")


if __name__ == "__main__":
    main()
