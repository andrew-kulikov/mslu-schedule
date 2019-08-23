import time
import os
import shutil
from schedule import Schedule


def get_root() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


def wait_file(folder, file_name, new_folder, new_name):
    time_to_wait = 10
    time_counter = 0
    while not os.path.exists(os.path.join(folder, file_name)):
        time.sleep(1)
        time_counter += 1
        if time_counter > time_to_wait:
            break

    shutil.move(os.path.join(folder, file_name),
                os.path.join(new_folder, new_name))


def build_schedule_name(schedule: Schedule) -> str:
    return prepare_file_name(schedule.faculty + schedule.course + schedule.years + schedule.group + schedule.week + '.xls')


def prepare_file_name(file_name: str) -> str:
    return file_name.replace('/', '_').replace(' ', '_')
