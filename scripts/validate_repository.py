#!/usr/bin/env python3
"""Validate required repository packaging and synthetic JSON fixtures."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "mmss-principle-synthesis"
REQUIRED_FILES = (
    "README.md",
    "README.ru.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    ".gitignore",
    "skills/mmss-principle-synthesis/SKILL.md",
    "examples/README.md",
    "examples/requirement-based-module/prompt.md",
    "examples/requirement-based-module/expected-properties.md",
    "examples/existing-stack-audit/prompt.md",
    "examples/existing-stack-audit/input.json",
    "examples/existing-stack-audit/expected-properties.md",
    "docs/design-principles.md",
    "docs/evaluation.md",
    ".github/workflows/validate.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/pull_request_template.md",
    "scripts/validate_repository.py",
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON constant {value}")


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def parse_frontmatter(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter opener")
        return
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter closer")
        return
    block = text[4:end]
    # Parse the restricted, scalar/list subset used in this SKILL.md. Reject
    # malformed indentation and duplicate top-level fields explicitly.
    top: dict[str, str] = {}
    current: str | None = None
    for line_number, line in enumerate(block.splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  "):
            if current == "description" and line.startswith("  "):
                continue
            if current == "metadata" and re.match(r"^  [A-Za-z_][\w-]*:\s*", line):
                continue
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: invalid frontmatter indentation")
            continue
        match = re.match(r"^([A-Za-z_][\w-]*):(?:\s+(.*))?$", line)
        if not match:
            # YAML folded block continuation (description) is permitted.
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: invalid frontmatter field")
            continue
        key, value = match.group(1), match.group(2) or ""
        if key in top:
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: duplicate field {key!r}")
        top[key] = value
        current = key
    expected_name = SKILL_DIR.name
    if top.get("name") != expected_name:
        errors.append(f"frontmatter name must be {expected_name!r}")
    if not top.get("description", "").strip():
        errors.append("frontmatter description must be non-empty")
    metadata_match = re.search(r"(?m)^  version:\s*[\"']?([^\"'\s]+)", block)
    if not metadata_match or metadata_match.group(1) != "0.1.5":
        errors.append("frontmatter metadata.version must be 0.1.5")


def check_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            target = target.strip().split("#", 1)[0]
            if not target or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("//"):
                continue
            if not (path.parent / target).resolve().exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local file link {target!r}")


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8") if (ROOT / "LICENSE").exists() else ""
    if "Copyright (c) 2026 Andrey Mundrievskiy (Abstract-Mindfreak)" not in license_text:
        errors.append("LICENSE is missing the required copyright notice")
    skill = ROOT / "skills/mmss-principle-synthesis/SKILL.md"
    if skill.is_file():
        parse_frontmatter(skill, errors)
    for fixture in (ROOT / "examples/existing-stack-audit/input.json",):
        if fixture.is_file():
            try:
                json.loads(fixture.read_text(encoding="utf-8"), object_pairs_hook=unique_object, parse_constant=reject_constant)
            except (json.JSONDecodeError, ValueError) as exc:
                errors.append(f"{fixture.relative_to(ROOT)}: invalid JSON: {exc}")
    check_links(errors)
    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Repository validation passed: {len(REQUIRED_FILES)} required files, skill version 0.1.5, JSON fixture, and local Markdown file links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
