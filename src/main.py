import os
from util import get_root, wait_file, build_schedule_name
from scheduleParser import ScheduleParser
from schedule import Schedule


SCHEDULE_URL = 'http://raspisanie.mslu.by/schedule/reports/publicreports/schedulelistforgroupreport'
FACULTY = 'Переводческий'
COURSE = '3'
YEARS = '2019/2020'
GROUP = '303/2 ан-нем'
G1 = '308/1 ан-араб'
WEEK = '1 сентября - 8 сентября'


def main():
    schedule = Schedule(FACULTY, COURSE, YEARS, G1, WEEK)
    
    parser = ScheduleParser(SCHEDULE_URL, get_root())
    with parser:
        parser.get_schedule(schedule)

    wait_file(
        get_root(),
        'scheduleGroup.xls',
        os.path.join(get_root(), 'schedules'),
        build_schedule_name(schedule)
    )


if __name__ == "__main__":
    main()
