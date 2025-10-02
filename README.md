# Weekly Meeting Generator

Generate a realistic week of work meetings (ICS) with AI-generated topics. The script creates a `YYYY-MM-DD_week_events.ics` file for the upcoming work week (Mon–Fri), scheduling meetings in random 15–60 minute slots during working hours and avoiding conflicts.

## Features
- AI-generated meeting topics via OpenAI
- Week schedule (Mon–Fri) in timezone `Europe/Paris`
- Working hours 09:00–18:00 with 15-min granularity
- Conflict-free random time slots per day
- Outputs standard `.ics` calendar file

## Requirements
- Python 3.10+
- An OpenAI API key

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env` and set your values:

```
OPENAI_API_KEY=sk-...
TOPICS_PROMPT=General work meetings
```

- `OPENAI_API_KEY` (required): your OpenAI key
- `TOPICS_PROMPT` (optional): guiding theme for topic generation

## Usage
Run the generator:

```bash
python weekly_meeting_generator.py
```

This creates a file named like `2025-10-06_week_events.ics` in the current directory. Import it into your calendar (Google, Outlook, Apple Calendar, etc.).

## Notes
- Uses `gpt-4o-mini` for topic generation; adjust the model in code if desired.
- Timezone and working hours are set in code for simplicity; modify if needed.
- The script retries up to 100 times per topic to find a free slot.

## File Overview
- `weekly_meeting_generator.py` — main script
- `requirements.txt` — dependencies
- `.env` — secrets and configuration (not committed)
- `.gitignore` — standard Python and venv ignores

## License
Proprietary/Private (update as appropriate).