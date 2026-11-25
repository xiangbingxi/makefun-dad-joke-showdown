"""Write the Dad Joke Showdown entry text to /output/entry.txt.

The entry text is written verbatim: no trailing newline, no extra
characters, no external files read, no network access. The output is
deterministic: running this script twice produces byte-identical files.
"""

import os

ENTRY = "The mechanic told me my car needed a new muffler. I said, “Keep it quiet.”"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # 防呆校验：读回文件，必须与 ENTRY 一字不差，否则报错退出。
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("entry.txt mismatch after write")


if __name__ == "__main__":
    main()
