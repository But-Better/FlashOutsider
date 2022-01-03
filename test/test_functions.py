import os.path
import unittest

import shutil

from flash_preparation.rework_scripts import rework_build_link
from utils import env_utils
from env_reader import env_reader


class TestSetup(unittest.TestCase):

    def test_get_original_dir(self):
        self.assertEqual("/workdir/zephyr/samples/basic/fade_led/build",
                         rework_build_link.get_original_dir("original_dir_included"))

    def test_file_update(self):
        if os.path.exists("file_to_update"):
            os.remove("file_to_update")

        shutil.copyfile("original_file_to_update", "file_to_update")
        # noinspection SpellCheckingInspection
        env_utils.replace_all_in_file("file_to_update", "/replacethis/", "/with_that/")

        # check if text got replaced
        with open("file_to_update", "r") as file:
            for line in file.readlines():
                # noinspection SpellCheckingInspection
                if line.__contains__("replacethis"):
                    self.fail(f"not everything got replaced in file, line: {line}")

            file.close()

        if os.path.exists("file_to_update"):
            os.remove("file_to_update")

    def test_get_all_files_in_path(self):
        file_scan = env_utils.get_all_filepaths_in_path("./scan_dir")
        self.assertEqual(["./scan_dir/a", "./scan_dir/b"], file_scan)

    def test_add_thread_event_to_list(self):
        new_list = list()
        env_utils.add_thread_event_to_list(new_list, "filename", "old", "new", True)
        self.assertEqual(1, new_list.__len__())

    def test_env_reader(self):
        expected_dict = dict({"key": "value", "anotherkey": "anothervalue", "thisisisakey": "/this/is/a/value"})
        self.assertEqual(expected_dict, env_reader.read_from_env("env_test_scan_file"))


if __name__ == '__main__':
    unittest.main()
