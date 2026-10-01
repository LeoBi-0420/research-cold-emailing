#!/usr/bin/env python3
"""Validate the public skill package without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPOSITORY_ROOT / "research-cold-emailing"
SKILL_FILE = SKILL_ROOT / "SKILL.md"

REQUIRED_FILES = (
    REPOSITORY_ROOT / "LICENSE",
    REPOSITORY_ROOT / "README.md",
    SKILL_FILE,
    SKILL_ROOT / "agents" / "openai.yaml",
    SKILL_ROOT / "references" / "batch-workflow.md",
    SKILL_ROOT / "references" / "example-first-contact.md",
    SKILL_ROOT / "references" / "operating-mode.md",
    SKILL_ROOT / "references" / "quality-review.md",
    SKILL_ROOT / "references" / "research-method.md",
    SKILL_ROOT / "references" / "student-profile.example.md",
    SKILL_ROOT / "references" / "writing-rules.md",
    REPOSITORY_ROOT / "evals" / "behavior-cases.md",
)

FORBIDDEN_SUFFIXES = {".eml", ".msg", ".pdf"}
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EMAIL_ADDRESS = re.compile(r"(?<![\w.-])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}(?![\w.-])")
SECRET_TOKEN = re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")
ABSOLUTE_USER_PATH = re.compile(r"(?:/Users/[^/\s]+|[A-Za-z]:\\Users\\[^\\\s]+)")
LEGACY_IDENTIFIER = "research-" + "outreach-emails"


def validate_required_files(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(REPOSITORY_ROOT)}")


def validate_frontmatter(errors: list[str]) -> None:
    text = SKILL_FILE.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
        return

    try:
        _, frontmatter, _ = text.split("---", 2)
    except ValueError:
        errors.append("SKILL.md frontmatter is not closed")
        return

    fields: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()

    if fields.get("name") != SKILL_ROOT.name:
        errors.append("frontmatter name must match the skill directory")
    if not fields.get("description"):
        errors.append("frontmatter description is required")


def validate_relative_links(errors: list[str]) -> None:
    for markdown_file in REPOSITORY_ROOT.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative_target = target.split("#", 1)[0]
            if not relative_target:
                continue
            resolved = (markdown_file.parent / relative_target).resolve()
            if not resolved.exists():
                shown_file = markdown_file.relative_to(REPOSITORY_ROOT)
                errors.append(f"broken link in {shown_file}: {target}")


def validate_skill_links_stay_inside_skill(errors: list[str]) -> None:
    skill_root = SKILL_ROOT.resolve()
    for markdown_file in SKILL_ROOT.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative_target = target.split("#", 1)[0]
            if not relative_target:
                continue
            resolved = (markdown_file.parent / relative_target).resolve()
            if not resolved.is_relative_to(skill_root):
                shown_file = markdown_file.relative_to(REPOSITORY_ROOT)
                errors.append(f"skill link escapes the installable skill in {shown_file}: {target}")


def validate_public_files(errors: list[str]) -> None:
    for path in REPOSITORY_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden public file type: {path.relative_to(REPOSITORY_ROOT)}")
        if path.name in {".env", ".env.local", "student-profile.md"}:
            errors.append(f"private file must not be published: {path.relative_to(REPOSITORY_ROOT)}")


def validate_public_content(errors: list[str]) -> None:
    text_suffixes = {".md", ".json", ".py", ".toml", ".txt", ".yaml", ".yml"}
    for path in REPOSITORY_ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        text = path.read_text(encoding="utf-8")
        for address in EMAIL_ADDRESS.findall(text):
            if not address.lower().endswith("@example.edu") and not address.lower().endswith("@example.com"):
                shown_file = path.relative_to(REPOSITORY_ROOT)
                errors.append(f"non-synthetic email address in {shown_file}: {address}")
        if SECRET_TOKEN.search(text):
            errors.append(f"possible API secret in {path.relative_to(REPOSITORY_ROOT)}")
        if path.resolve() != Path(__file__).resolve() and ABSOLUTE_USER_PATH.search(text):
            errors.append(f"absolute user path in {path.relative_to(REPOSITORY_ROOT)}")
        if LEGACY_IDENTIFIER in text:
            errors.append(f"legacy skill identifier in {path.relative_to(REPOSITORY_ROOT)}")


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)
    if SKILL_FILE.is_file():
        validate_frontmatter(errors)
    validate_relative_links(errors)
    validate_skill_links_stay_inside_skill(errors)
    validate_public_files(errors)
    validate_public_content(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Public skill package is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
