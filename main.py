"""Entry point that writes a specific text line to the designated output file."""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os
from pathlib import Path

LINE = "You treat a two-dollar make-fun bounty like the Olympic finals while obsessively counting characters in your jokes to scrape by.\n"

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    dir_path = Path(output_dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / "entry.txt"

    content = LINE
    if not (1 <= len(content) <= 200 and content.strip() and content.count("\n") == 1 and content.endswith("\n")):
        raise ValueError("Content validation failed")

    file_path.write_text(content, encoding="utf-8")
    print(file_path)
    print(len(content))

if __name__ == "__main__":
    main()
