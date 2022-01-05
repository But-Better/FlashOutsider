import shutil
import os


def run(build_path):
    if not os.path.exists(f"{build_path}/zephyr"):
        print(f"the remove of {build_path}/zephyr was not necessary, since it didn't exist")
        return

    shutil.rmtree(f"{build_path}/zephyr")
