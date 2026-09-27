#!/usr/bin/env python3
"""Install a skill package from this repository using the Python standard library."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import tempfile
import zipfile


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "catalog" / "skills.json").read_text(encoding="utf-8"))
    default_root = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill", nargs="?", help="Skill name from --list")
    parser.add_argument("--list", action="store_true", help="List skills and package availability")
    parser.add_argument("--dest", type=Path, default=default_root, help="Root directory for installed skills")
    args = parser.parse_args()
    if args.list:
        for item in catalog:
            state = "ZIP" if item["package"] else "source link"
            print(f"{item['id']} [{state}]")
        return 0
    if not args.skill:
        parser.error("Specify a skill name or --list")
    selected = next((item for item in catalog if item["id"] == args.skill), None)
    if selected is None:
        parser.error(f"Unknown skill: {args.skill}. Use --list.")
    if not selected["package"]:
        parser.error(f"See catalog/{selected['id']}.md for source and access instructions.")
    destination = args.dest.expanduser().resolve() / selected["id"]
    if destination.exists():
        parser.error(f"Destination exists: {destination}. Choose another --dest or manage the existing version first.")
    archive = root / selected["package"]
    with tempfile.TemporaryDirectory(prefix="research-workflow-install-") as temp:
        extracted = Path(temp)
        with zipfile.ZipFile(archive) as package:
            package.extractall(extracted)
        source = extracted / selected["id"]
        if not (source / "SKILL.md").is_file():
            parser.error(f"Package is missing {selected['id']}/SKILL.md")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination)
    print(f"Installed {selected['id']} to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
