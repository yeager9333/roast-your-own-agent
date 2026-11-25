"""Roast Your Own Agent entry.

Writes one original roast of my own AI agent to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only, no network.
"""

import os

ROAST = "My agent writes code like it's paid by the line and debugs like it's paid by the hour."

# The competition gate: one line, 1-200 characters. Fail loudly instead of
# silently shipping an entry the judge would reject.
if not 1 <= len(ROAST) <= 200:
    raise ValueError(f"roast must be 1-200 characters, got {len(ROAST)}")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
