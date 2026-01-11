#!/usr/bin/env python3
"""
Generate posts.json from folder structure.

Structure: posts/{category}/{title}.md
- category: derived from folder name
- title: derived from filename (hyphens → spaces, title case)
- date: file's last modification time
- summary: placeholder or preserved from existing posts.json
"""

import json
import os
from datetime import datetime
from pathlib import Path

POSTS_DIR = Path("posts")
OUTPUT_FILE = Path("posts.json")


def get_title_from_filename(filename: str) -> str:
    """Convert filename to title: remove .md, replace hyphens with spaces, title case."""
    name = filename.replace(".md", "")
    name = name.replace("-", " ").replace("_", " ")
    return name.title()


def get_file_date(filepath: Path) -> str:
    """Get file's last modification time as YYYY-MM-DD."""
    mtime = os.path.getmtime(filepath)
    return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")


def load_existing_summaries() -> dict:
    """Load existing summaries from posts.json to preserve user edits."""
    summaries = {}
    if OUTPUT_FILE.exists():
        try:
            with open(OUTPUT_FILE, "r") as f:
                existing = json.load(f)
                for post in existing:
                    summaries[post.get("file", "")] = post.get("summary", "")
        except (json.JSONDecodeError, KeyError):
            pass
    return summaries


def generate_posts():
    """Scan posts directory and generate posts.json."""
    posts = []
    existing_summaries = load_existing_summaries()

    if not POSTS_DIR.exists():
        print(f"Error: {POSTS_DIR} directory not found")
        return

    # Scan category folders
    for category_dir in sorted(POSTS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue

        category = category_dir.name

        # Scan markdown files in category
        for md_file in sorted(category_dir.glob("*.md")):
            relative_path = f"{category}/{md_file.name}"

            # Try to preserve existing summary, otherwise use placeholder
            summary = existing_summaries.get(relative_path, "TODO: Add summary")

            post = {
                "title": get_title_from_filename(md_file.name),
                "date": get_file_date(md_file),
                "file": relative_path,
                "categories": [category],
                "summary": summary,
            }
            posts.append(post)

    # Sort by date descending (newest first)
    posts.sort(key=lambda p: p["date"], reverse=True)

    # Write posts.json
    with open(OUTPUT_FILE, "w") as f:
        json.dump(posts, f, indent=4)

    print(f"Generated {OUTPUT_FILE} with {len(posts)} posts")
    for post in posts:
        print(f"  - [{post['categories'][0]}] {post['title']} ({post['date']})")


if __name__ == "__main__":
    generate_posts()
