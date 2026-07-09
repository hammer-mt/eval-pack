#!/usr/bin/env python3
"""Validate an eval pack's structure, portability, and handoff hygiene."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


FETCH_ATTRS = {
    "audio": ("src",),
    "iframe": ("src",),
    "img": ("src", "srcset"),
    "link": ("href",),
    "script": ("src",),
    "source": ("src", "srcset"),
    "video": ("src", "poster"),
}


class PackParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.slide_titles: list[str] = []
        self.ids: list[str] = []
        self.fetches: list[tuple[str, str, str]] = []
        self.images_without_alt: list[str] = []
        self.has_deck = False
        self.has_toc = False
        self.has_pager = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        element_id = values.get("id")
        if element_id:
            self.ids.append(element_id)
        if tag == "main" and element_id == "deck":
            self.has_deck = True
        if tag == "nav" and element_id == "toc":
            self.has_toc = True
        if element_id == "pager":
            self.has_pager = True
        if tag == "section" and "slide" in values.get("class", "").split():
            self.slide_titles.append(values.get("data-title", "").strip())
        if tag == "img" and not values.get("alt", "").strip():
            self.images_without_alt.append(values.get("src", "<unknown>"))
        for attr in FETCH_ATTRS.get(tag, ()):
            value = values.get(attr, "").strip()
            if value:
                self.fetches.append((tag, attr, value))


def validate_html(html: str, *, template: bool = False) -> tuple[list[str], list[str]]:
    parser = PackParser()
    parser.feed(html)
    errors: list[str] = []
    warnings: list[str] = []

    if not template and re.search(r"\b(?:REPLACE|TODO)\b", html, re.IGNORECASE):
        errors.append("Unresolved REPLACE or TODO placeholder remains.")
    if len(parser.slide_titles) < 2:
        errors.append("Expected at least two .slide sections.")
    if any(not title for title in parser.slide_titles):
        errors.append("Every slide needs a non-empty data-title for navigation.")
    if not any("summary" in title.lower() for title in parser.slide_titles):
        errors.append("Add an executive summary slide.")
    if not any("limitation" in title.lower() for title in parser.slide_titles):
        errors.append("Add a limitations slide.")
    if not parser.has_deck:
        errors.append("Missing <main id=\"deck\"> landmark.")
    if not parser.has_toc:
        errors.append("Missing <nav id=\"toc\"> navigation.")
    if not parser.has_pager:
        errors.append("Missing #pager controls.")
    if "slide-next" not in html:
        errors.append("Missing end-of-slide next navigation.")

    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        errors.append("Duplicate HTML id values: " + ", ".join(duplicates))
    for src in parser.images_without_alt:
        errors.append(f"Image needs useful alt text: {src}")

    for tag, attr, value in parser.fetches:
        if value.startswith(("data:", "#")):
            continue
        candidates = [part.strip().split()[0] for part in value.split(",")]
        for candidate in candidates:
            if not candidate or candidate.startswith(("data:", "#")):
                continue
            if candidate.startswith(("http://", "https://", "//")):
                errors.append(f"External fetch breaks offline use: <{tag} {attr}=\"{candidate}\">")
            elif not template:
                errors.append(
                    f"Local media is not embedded: <{tag} {attr}=\"{candidate}\">. "
                    "Run scripts/embed_media.py."
                )

    if len(parser.slide_titles) > 12:
        warnings.append(f"Pack has {len(parser.slide_titles)} slides; confirm each one earns its place.")
    if len(html.encode("utf-8")) > 15_000_000:
        warnings.append("Pack exceeds 15 MB; downscale screenshots or shorten GIFs.")

    return errors, warnings


def main() -> None:
    arg_parser = argparse.ArgumentParser(description=__doc__)
    arg_parser.add_argument("pack", type=Path)
    arg_parser.add_argument(
        "--template",
        action="store_true",
        help="Validate reusable template structure while allowing placeholders and local media.",
    )
    args = arg_parser.parse_args()

    if not args.pack.is_file():
        sys.exit(f"not found: {args.pack}")

    errors, warnings = validate_html(args.pack.read_text(encoding="utf-8"), template=args.template)
    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}")

    if errors:
        sys.exit(f"{args.pack}: {len(errors)} validation error(s)")
    print(f"{args.pack}: valid eval pack ({len(warnings)} warning(s))")


if __name__ == "__main__":
    main()
