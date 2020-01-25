import os
import shutil

from schedule import Schedule
from scheduleParser import ScheduleParser
from defaultLoader import get_settings
from util import get_root, wait_file, build_schedule_name


def copy_file(folder, file_name, new_file):
    wait_file(folder, file_name)
    shutil.move(os.path.join(folder, file_name), new_file)


def main():
    schedule_url, faculty, course, years, group, week = get_settings()
    schedule = Schedule(faculty, course, years, group, week)

    parser = ScheduleParser(schedule_url, get_root())
    with parser:
        parser.get_schedule(schedule)

    schedule_path = os.path.join(get_root(), 'schedules')
    schedule_name = build_schedule_name(schedule)
    schedule_file = os.path.join(schedule_path, schedule_name)

    copy_file(get_root(), 'scheduleGroup.xls', schedule_file)


if __name__ == "__main__":
    main()
