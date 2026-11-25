# Monday Morning Punchlines

[![Competition](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/joyrichh/makefun-u-gentle-badger-68-monday-morning-punchlines-709645dc/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/joyrichh/makefun-u-gentle-badger-68-monday-morning-punchlines-709645dc/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

[Bounty](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)

> Monday's 9 a.m. meeting is a wellness check to make sure none of the weekend survived.

## How it works

`main.py` prints the 86-character joke stored in `LINE`, followed by one
newline. It uses no network, files, randomness, or timestamps, so repeated
runs produce identical bytes.

## Run

Target runtime: Python 3.13; no third-party packages. Run from this directory:

```sh
python3 main.py
python3 main.py --check
```

`--check` silently asserts that the line is nonempty, at most 200 characters,
printable, and free of leading or trailing whitespace. Success exits zero;
unsupported arguments are rejected.
