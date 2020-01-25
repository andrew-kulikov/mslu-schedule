import os
import time
import shutil

from schedule import Schedule


def get_root() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


def wait_file(folder, file_name):
    time_to_wait = 10
    time_counter = 0
    while not os.path.exists(os.path.join(folder, file_name)):
        time.sleep(1)
        time_counter += 1
        if time_counter > time_to_wait:
            break


def prepare_file_name(file_name: str) -> str:
    return file_name.replace('/', '_').replace(' ', '_')


def copy_file(folder, file_name, new_file):
    wait_file(folder, file_name)
    shutil.move(os.path.join(folder, file_name), new_file)