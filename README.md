# Streaks 🔥

A tiny command-line habit tracker written in Python. No dependencies, one file.

## Features
- Add and remove habits
- Check off habits once per day
- See your current streak and total completions
- Data is stored locally in `~/.streaks.json`

## Usage

```bash
python streaks.py add "Read 10 pages"
python streaks.py done "Read 10 pages"
python streaks.py list
python streaks.py remove "Read 10 pages"
```

Example output:

```
✅ Read 10 pages                  streak: 3  total: 3
⬜ Drink water                    streak: 0  total: 1
```

## Requirements
Python 3.8+

## Ideas for improvement
- Weekly summary command
- Colored output
- Export to CSV
- Reminders

## License
MIT
