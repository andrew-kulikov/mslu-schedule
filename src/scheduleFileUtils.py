import os
import excel2img

from schedule import Schedule
from util import get_root, copy_file, prepare_file_name


def build_schedule_name(schedule: Schedule, extension: str) -> str:
    return prepare_file_name(
        '_'.join([
            schedule.faculty,
            schedule.course,
            schedule.years,
            schedule.group,
            schedule.week
        ]) + extension
    )


def save(folder_name: str, source_name: str, schedule: Schedule):
    root_folder = get_root()

    schedule_path = os.path.join(root_folder, folder_name)
    schedule_name = build_schedule_name(schedule, '.xls')
    schedule_file = os.path.join(schedule_path, schedule_name)

    copy_file(root_folder, source_name, schedule_file)

    image_name = build_schedule_name(schedule, '.png')
    image_file = os.path.join(schedule_path, image_name)
    excel2img.export_img(schedule_file, image_file, "Расписание", None)

    return image_file


def get_weeks():
    with open('data/weeks.txt', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        return [line for line in lines if not line.startswith('~')]
