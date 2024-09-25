from TiMBA.results_logging.FileBaseclass import FileBaseclass
import csv


class ResultsWriter(FileBaseclass):  # FileBaseclass variables are read in

    def __init__(self, filepath, filetype: str = ".csv", overwrite_file: bool = False, header: tuple = (),
                 mode: str = "a+", sep: str = ","):
        super().__init__(
            filepath,
            filetype,
            overwrite_file,
            mode,
            header,
            sep
        )

    def write(self, *args):
        """
        Example:
            Writer = ResultsWriter(r"<filepath>", True, header=('file', 'name', 'result'))
            Writer.write('a', 'b', 2)
            # or:
            results = [1, 'b', -40]
            Writer.write(*results)
        """
        with open(self.filepath, mode=self.mode, newline='') as filestream:
            log = csv.writer(filestream, delimiter=self.sep)
            log.writerow(args)

    def write_iter(self, *args):
        """
        Example:
            Writer = ResultsWriter(r"<filepath_to_csv>", True, header=('file', 'name', 'result'))
            Writer.write_iter(list_01, list_02, list_03)
        """
        print(self.filepath)
        with open(self.filepath, mode=self.mode, newline='') as filestream:
            log = csv.writer(filestream, delimiter=self.sep)
            for _ in zip(*args):
                log.writerow(_)
