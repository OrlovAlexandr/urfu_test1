import pandas as pd

val = 100
print(type(val))

df = pd.DataFrame({
    "Date": [
        "2015-05-08", "2015-05-07", "2015-05-06", "2015-05-05",
        "2015-05-08", "2015-05-07", "2015-05-06", "2015-05-05"],
    "Data": [5, 8, 6, 1, 50, 100, 60, 120],
})
print(type(df))


def deviation_columns(d_frame:str, column_1:str, column_2:str, tab=False) -> pandas.core.frame.DataFrame:
    """_summary_

    Args:
        d_frame (str): _description_
        column_1 (str): _description_
        column_2 (str): _description_
        tab (bool, optional): _description_. Defaults to False.

    Returns:
        pandas.core.frame.DataFrame: _description_
    """