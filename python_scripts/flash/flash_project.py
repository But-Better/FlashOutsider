import subprocess

from specific_utils import env_utils


def flash(path):
    env_utils.change_to_dir(path)

    command = ["west", "flash"]  # command to be executed
    res = subprocess.check_output(command)  # system command
    return res.decode("utf-8").split(" ")[1]
