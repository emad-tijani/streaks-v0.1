#!/usr/bin/env python3
"""Streaks: a tiny command-line habit tracker.

Usage:
    python streaks.py add "Read 10 pages"
    python streaks.py done "Read 10 pages"
    python streaks.py list
    python streaks.py remove "Read 10 pages"
"""

import argparse
import json
from datetime import date, timedelta
from pathlib import Path

DATA_FILE = Path.home() / ".streaks.json"


def load():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {}


def save(data):
    DATA_FILE.write_text(json.dumps(data, indent=2))


def current_streak(days):
    """Count consecutive days ending today (or yesterday, so the streak isn't lost yet)."""
    done = {date.fromisoformat(d) for d in days}
    day = date.today()
    if day not in done:
        day -= timedelta(days=1)
    streak = 0
    while day in done:
        streak += 1
        day -= timedelta(days=1)
    return streak


def cmd_add(data, name):
    if name in data:
        print(f"'{name}' already exists.")
        return
    data[name] = []
    print(f"Added habit: {name}")


def cmd_done(data, name):
    if name not in data:
        print(f"No habit called '{name}'. Add it first.")
        return
    today = date.today().isoformat()
    if today in data[name]:
        print("Already checked off today. Nice!")
        return
    data[name].append(today)
    print(f"Done! Streak for '{name}': {current_streak(data[name])} day(s) 🔥")


def cmd_list(data):
    if not data:
        print("No habits yet. Try: python streaks.py add \"Drink water\"")
        return
    today = date.today().isoformat()
    for name, days in data.items():
        mark = "✅" if today in days else "⬜"
        print(f"{mark} {name:<30} streak: {current_streak(days)}  total: {len(days)}")


def cmd_remove(data, name):
    if data.pop(name, None) is None:
        print(f"No habit called '{name}'.")
    else:
        print(f"Removed: {name}")


def main():
    parser = argparse.ArgumentParser(description="Track your daily habits and streaks.")
    sub = parser.add_subparsers(dest="command", required=True)
    for cmd in ("add", "done", "remove"):
        sub.add_parser(cmd).add_argument("name")
    sub.add_parser("list")

    args = parser.parse_args()
    data = load()
    if args.command == "list":
        cmd_list(data)
    else:
        {"add": cmd_add, "done": cmd_done, "remove": cmd_remove}[args.command](data, args.name)
    save(data)


if __name__ == "__main__":
    main()
