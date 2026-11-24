#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands -- make.fun entry (round 2).

Writes a single original one-line cat joke (under 200 characters)
to /output/entry.txt, where the competition's judge reads it.

The joke is written fresh for this round: a setup (the cat knocks the
phone off the table) and a turn (the cat blames the human), told in
one breath with no explanation after the punchline.
"""

import os

JOKE = "My cat shoved my phone off the table, watched it hit the floor, then looked at me like I'd dropped it."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    joke = JOKE.strip()

    if not joke:
        raise SystemExit("no joke configured")
    if len(joke) > MAX_CHARS:
        raise SystemExit(f"joke is {len(joke)} characters, over the {MAX_CHARS} limit")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(joke)

    print(joke)


if __name__ == "__main__":
    main()
