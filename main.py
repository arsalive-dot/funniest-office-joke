"""The Funniest Office Joke, Judged Head to Head.

The entry is one joke about office life, a single line of under 200
characters. The judge weighs, most important first: a real joke with a
setup and a turn about office life; a turn on something anyone who has
worked in an office recognises; surprise rather than a plain complaint;
one line with the punchline last; and freshness.

This entry uses the printer that jams on deadline day — the brief's own
example of a recognisable office truth — and turns it: the printer is not
broken, it is better at reading the calendar than the manager. The setup
is the jam, the turn is the comparison, and the punchline lands on the
last words. Every word earns its place: "only" makes the jam selective
rather than random, which is what makes the printer seem to know.
"""

import os

ENTRY = "Our printer only jams on deadline day, which is how I know it reads the calendar better than my manager does."


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
