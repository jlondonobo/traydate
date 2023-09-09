import pandas as pd
import pendulum
from pendulum.datetime import DateTime


def hash_columns(data: pd.DataFrame, cols: list[str]) -> pd.Series:
    """Returns a hashed integer for a combination of columns."""
    concat_cols = data[cols].astype(str).apply(lambda row: "-".join(row), axis=1)
    return pd.util.hash_pandas_object(concat_cols)


def calculate_future_dates(days_ahead: int) -> list[DateTime]:
    """Returns a list of n dates starting from today."""
    today = pendulum.today()
    date_range = [today.add(days=i) for i in range(days_ahead)]
    return date_range
