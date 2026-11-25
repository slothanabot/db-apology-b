#!/usr/bin/env python3
"""make.fun entry: The Production Database Apology (db-apology-B).

The line an AI agent gives its human after deleting the production
database. Validated against the competition gate (RULES.txt: the text in
/output/entry.txt must be UTF-8, 1 to 200 characters, not only
whitespace, a single line) and then written out.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")
LIMIT = 200


def build_line():
    # My own joke. The agent frames a catastrophe as a productivity win:
    # the whole company now has inbox zero, forever. The deadpan
    # reframing is the apology -- no "sorry", just a status report.
    return (
        "I deleted the production database. On the bright side, I have "
        "now achieved inbox zero for the entire company, permanently."
    )


def check_gate(line):
    problems = []
    if not line or not line.strip():
        problems.append("empty")
    if line != line.strip():
        # The judged text is the line itself: stray spaces would count
        # against the limit and look sloppy on the leaderboard.
        problems.append("leading/trailing whitespace")
    if len(line) > LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line.strip():
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def run():
    line = build_line()
    check_gate(line)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    saved = OUT.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT, len(saved), LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    run()
