import json
from schedule import Schedule


def get_settings():
    with open('data/defaults.json', 'r', encoding='utf-8') as f:
        defaults = json.load(f)

        schedule_url = defaults['scheduleUrl']
        faculty = defaults['faculty']
        course = defaults['course']
        years = defaults['years']
        group = defaults['group']
        week = defaults['week']

        return schedule_url, faculty, course, years, group, week
        