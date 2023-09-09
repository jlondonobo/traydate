import sys
import time
from datetime import datetime
from typing import Iterable

import pandas as pd
from constants import HEADERS, ID_COLS, RENAMER
from utils import calculate_future_dates, hash_columns

sys.path.append("..")
from pydel.client import Pydel


def _fetch_multi_day_timeslots(
    dates: Iterable[datetime], pydel: Pydel, delay: int
) -> list[dict]:
    """Fetches available fields for a collection of dates"""
    results_collection = []
    for date in dates:
        single_day_results = pydel.timeslots(date)
        results_collection.extend(single_day_results)
        time.sleep(delay)
    return results_collection


def _results_to_pandas(results: list[dict]) -> pd.DataFrame:
    return pd.json_normalize(results["alternative_timeslots"], "timeslots")


def _format_columns(data: pd.DataFrame, renamer: dict[str, str]) -> pd.DataFrame:
    return data.filter(list(renamer)).rename(renamer, axis=1)


def _add_timeslot_id(data: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    return data.assign(timeslot_id=hash_columns(data, cols))


def fetch(days_ahead: int, delay: int = 5) -> pd.DataFrame:
    """Returns all available timeslots for a range of days."""
    pydel = Pydel(HEADERS)
    dates = calculate_future_dates(days_ahead)
    
    results = _fetch_multi_day_timeslots(dates, pydel, delay)
    timeslots = _results_to_pandas(results)
    formatted_timesolts = _format_columns(timeslots, RENAMER)
    timeslots_with_id = _add_timeslot_id(formatted_timesolts, ID_COLS)
    return timeslots_with_id
