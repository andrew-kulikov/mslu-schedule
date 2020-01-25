import os
from util import get_root, wait_file, build_schedule_name
from scheduleParser import ScheduleParser
from schedule import Schedule
import shutil
import pandas as pd

SCHEDULE_URL = 'http://raspisanie.mslu.by/schedule/reports/publicreports/schedulelistforgroupreport'
FACULTY = 'Переводческий'
COURSE = '3'
YEARS = '2019/2020'
GROUP = '303/2 ан-нем'
WEEK = '1 сентября - 8 сентября'


def write_new_schedule(folder, file_name, new_file):
    wait_file(folder, file_name)
    shutil.move(os.path.join(folder, file_name), new_file)


def main():
    schedule = Schedule(FACULTY, COURSE, YEARS, GROUP, WEEK)

    parser = ScheduleParser(SCHEDULE_URL, get_root())
    with parser:
        parser.get_schedule(schedule)

    schedule_path = os.path.join(get_root(), 'schedules')
    schedule_name = build_schedule_name(schedule)
    schedule_file = os.path.join(schedule_path, schedule_name)

    write_new_schedule(get_root(), 'scheduleGroup.xls', schedule_file)


if __name__ == "__main__":
    main()
