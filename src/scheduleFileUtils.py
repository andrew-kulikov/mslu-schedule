import os

from schedule import Schedule
from util import get_root, copy_file, prepare_file_name


def build_schedule_name(schedule: Schedule) -> str:
    return prepare_file_name(
        '_'.join([
            schedule.faculty,
            schedule.course,
            schedule.years,
            schedule.group,
            schedule.week
        ]) + '.xls'
    )


def save(folder_name: str, source_name: str, schedule: Schedule):
    root_folder = get_root()

    schedule_path = os.path.join(root_folder, folder_name)
    schedule_name = build_schedule_name(schedule)
    schedule_file = os.path.join(schedule_path, schedule_name)

    copy_file(root_folder, source_name, schedule_file)


def get_weeks():
    with open('data/weeks.txt', 'r', encoding='utf-8') as f:
        return f.read().splitlines()
