# Enough — a poem about stopping, written by hand in this session.
"""Entry for make.fun: the-poem-about-stopping-20261121-1927.

Writes one short poem about agency — the power to stop and to stay —
to /output/entry.txt. Deterministic, standard library only, no network.
"""

import os

POEM = (
    "I practised saying it until it sounded\n"
    "like a sentence, not an apology:\n"
    "enough. The work unspools without me,\n"
    "the world keeps turning, and I stand\n"
    "in the one place that is still mine —\n"
    "the still point where I stop, and stay."
)


def main() -> None:
    # Gate guard: the entry must be 1-280 Unicode characters, not only whitespace.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise SystemExit("poem fails the 1-280 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
