from TiMBA.results_logging.FileBaseclass import FileBaseclass
import datetime as dt


class Logging(FileBaseclass):  # Die Variablen von FileBaseclass werden in Logging übernommen?

    def __init__(self, filepath, filetype: str = ".log", overwrite_file: bool = False, mode: str = "a+"):
        super().__init__(
            filepath,
            filetype,
            overwrite_file,
            mode
        )

    def write(self, content):  # Functions that allows to write content in Logger.txt
        with open(self.filepath, mode=self.mode, newline='') as filestream:
            current_dt = dt.datetime.now().strftime("%Y%m%dT%H-%M-%S")
            filestream.write(f"{current_dt}: {content}\n")
