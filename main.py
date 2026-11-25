#!/usr/bin/env python3
"""The 3 AM Excuse.

A hardware wallet refuses to sign a transaction at 3 AM.
Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os
from pathlib import Path

LINE = "Denied. I only take orders from daytime you \u2014 3 a.m. you once swapped the rent for a coin called MOON and blamed my buttons."
# The line speaks in the wallet's own voice: it is the device, not an assistant.
# The joke is the hour itself - 3 a.m. you is a different, untrustworthy person
# from daytime you, and the wallet remembers the rent-for-MOON incident.
# No battery, firmware, or cold-storage cliche: the angle is the wallet
# keeping a grudge against its owner's late-night self.

def main():
    # One deterministic line, no randomness, no network, no clock reads:
    # the output is the same on every run, byte for byte.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
