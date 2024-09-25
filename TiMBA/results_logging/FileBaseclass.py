from os.path import exists, isfile, dirname
from os import makedirs
import csv
import datetime as dt


class FileBaseclass:

    def __init__(self, filepath, filetype: str = ".csv", overwrite_file: bool = False, mode: str = "a+",
                 header: tuple = (), sep: str = ","):
        self._filepath = filepath
        self.filetype = filetype.lower()
        self.overwrite = overwrite_file
        self.header = header
        self.mode = mode
        self.sep = sep
        self.check_and_init_file()

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, filepath):
        self._filepath = filepath
        self.check_and_init_file()

    def check_and_init_file(self):
        if self.filepath is None:
            raise ValueError(f"filepath is set to 'None' but must be defined.")
        if exists(self.filepath) and isfile(self.filepath):
            with open(self.filepath, mode="r") as file:
                content = file.read()
                contentlines = file.readlines()
            if content == "" and len(contentlines) == 0:
                self.init_file(mode=self.mode)
            elif self.overwrite is False:
                current_dt = dt.datetime.now().strftime("%Y%m%dT%H-%M-%S")
                self.filepath = f"{self.filepath.replace(self.filetype, '')}_D{current_dt}{self.filetype}"
            elif self.overwrite is True:
                self.init_file(mode='w+')
            else:
                raise FileExistsError(f"File exists: {self.filepath}")
        else:
            self.init_file(mode=self.mode)

    def init_file(self, mode):
        if not exists(self.filepath):
            dir_path = dirname(self.filepath)
            if not exists(dir_path):
                makedirs(dir_path)
        if self.filetype.lower() == ".csv":
            pass #TODO implement this passage after removing problems with loops in main.py
            # with open(self.filepath, mode=mode, newline='') as logfile:
            #     log = csv.writer(logfile, delimiter=self.sep)
            #     log.writerow(self.header)
        else:
            with open(self.filepath, mode=mode, newline='') as logfile:
                current_dt = dt.datetime.now().strftime("%Y%m%dT%H-%M-%S")
                logfile.write(f"Logger initialized at start time: {current_dt}\n")
