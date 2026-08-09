#!/usr/bin/env python3
"""Count Unicode code points for the Xiaohongshu body and tags."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count body characters and check a configurable limit."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text", help="Text to count.")
    source.add_argument("--file", type=Path, help="UTF-8 text file to count.")
    parser.add_argument("--limit", type=int, default=200)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be a positive integer")

    if args.file is not None:
        text = args.file.read_text(encoding="utf-8")
    else:
        text = args.text

    text = text.rstrip("\r\n")
    count = len(text)
    print(
        json.dumps(
            {
                "characters": count,
                "limit": args.limit,
                "within_limit": count <= args.limit,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
