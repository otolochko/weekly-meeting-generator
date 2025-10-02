import random
from datetime import datetime, timedelta
import pytz
from icalendar import Calendar, Event
from openai import OpenAI
import os
from dotenv import load_dotenv

# === LOAD ENV ===
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
TOPICS_PROMPT = os.getenv("TOPICS_PROMPT", "General work meetings")

if not API_KEY:
    raise ValueError("❌ OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=API_KEY)

# === CONFIG ===
tz = pytz.timezone("Europe/Paris")
work_start = 9
work_end = 18
days_to_generate = 5  # Mon–Fri
min_events = 5
max_events = 8

# === FUNCTIONS ===
def generate_topics(num_topics: int, topics_prompt: str):
    """Request GPT to generate meeting topics"""
    prompt = f"Generate {num_topics} short and concise work meeting topics in English related to {topics_prompt}. One per line. Do not use numbers or bullet points."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate only short meeting topics, no explanations or comments."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    text = response.choices[0].message.content.strip()
    topics = [t.strip("-• ") for t in text.split("\n") if t.strip()]
    return topics[:num_topics]

def get_next_monday(today: datetime.date):
    """Find the nearest Monday"""
    days_ahead = (0 - today.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    return today + timedelta(days=days_ahead)

# === MAIN ===
today = datetime.now(tz).date()
start_date = get_next_monday(today)

cal = Calendar()
cal.add('prodid', '-//Weekly Events//')
cal.add('version', '2.0')

generated_days = 0
current_date = start_date

while generated_days < days_to_generate:
    if current_date.weekday() < 5:  # only weekdays
        num_events = random.randint(min_events, max_events)
        topics = generate_topics(num_events, TOPICS_PROMPT)

        scheduled = []
        for topic in topics:
            for _ in range(100):  # up to 100 attempts to find a free slot
                start_hour = random.randint(work_start, work_end - 1)
                start_minute = random.choice([0, 15, 30, 45])
                duration = random.randint(15, 60)

                event_start = tz.localize(datetime.combine(current_date, datetime.min.time())) \
                              + timedelta(hours=start_hour, minutes=start_minute)
                event_end = event_start + timedelta(minutes=duration)

                # check for conflicts
                if any(not (event_end <= s or event_start >= e) for s, e in scheduled):
                    continue
                else:
                    scheduled.append((event_start, event_end))
                    break
            else:
                continue

            event = Event()
            event.add('summary', topic)
            event.add('dtstart', event_start)
            event.add('dtend', event_end)
            event.add('dtstamp', datetime.now(tz))
            cal.add_component(event)

        generated_days += 1

    current_date += timedelta(days=1)

# === SAVE ===
filename = f"{start_date}_week_events.ics"
with open(filename, 'wb') as f:
    f.write(cal.to_ical())

print(f"✅ Created file: {filename}")
