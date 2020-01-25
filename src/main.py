from schedule import Schedule
from scheduleParser import ScheduleParser
from defaultLoader import get_settings
from util import get_root
from scheduleFileUtils import save


def main():
    schedule_url, faculty, course, years, group, week = get_settings()
    schedule = Schedule(faculty, course, years, group, week)

    parser = ScheduleParser(schedule_url, get_root())
    with parser:
        parser.get_schedule(schedule)

    save('schedules', 'scheduleGroup.xls', schedule)


if __name__ == "__main__":
    main()
