import pandas as pd


class FileUtilities:

    @staticmethod
    def get_data_from_file(file_path) -> pd.DataFrame:
        """
        Reads data from file and returns it as a pandas dataframe.
        :param file_path: File path as string.
        :return: Pandas dataframe.
        """
        df = pd.read_csv(file_path, sep=',')
        return df

