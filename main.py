"""Print the Monday Morning Punchlines entry."""

import sys

LINE = "Monday's 9 a.m. meeting is a wellness check to make sure none of the weekend survived."


def main() -> None:
    if sys.argv[1:] == ["--check"]:
        assert 0 < len(LINE) <= 200
        assert LINE == LINE.strip()
        assert LINE.isprintable()
        return
    if sys.argv[1:]:
        raise SystemExit("usage: python3 main.py [--check]")
    print(LINE)


if __name__ == "__main__":
    main()
