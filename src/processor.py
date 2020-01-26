from schedule import Schedule
from scheduleParser import ScheduleParser
from defaultLoader import get_settings
from util import get_root
from scheduleFileUtils import save, get_weeks


def load_week_schedule(week):
    schedule_url, faculty, course, years, group, _ = get_settings()
    schedule = Schedule(faculty, course, years, group, week)

    parser = ScheduleParser(schedule_url, get_root())
    with parser:
        parser.get_schedule(schedule)

    saved_image_path = save('schedules', 'scheduleGroup.xls', schedule)

    return saved_image_path


if __name__ == "__main__":
    weeks = get_weeks()
    load_week_schedule(weeks[0])
