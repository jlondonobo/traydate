import sqlite3

import numpy as np
import pandas as pd


def create_slots(n: int) -> pd.DataFrame:
    start_date = pd.to_datetime("2023-01-01")
    end_date = pd.to_datetime("2023-01-02")
    time_intervals = pd.date_range(start=start_date, end=end_date, freq='30min')

    time_intervals = pd.to_datetime(
        np.random.choice(time_intervals, size=n, replace=True)
    )

    field_ids = np.random.choice(range(1, 6), n)
    prices = np.random.uniform(50, 200, n)

    return pd.DataFrame(
        {"time": time_intervals, "field_id": field_ids, "price": prices}
    ).rename_axis("slot_id").reset_index()


def create_clubs(slots: pd.DataFrame) -> pd.DataFrame:
    unique_field_ids = slots.field_id.unique()
    latitudes = np.random.uniform(-90, 90, len(unique_field_ids))
    longitudes = np.random.uniform(-180, 180, len(unique_field_ids))
    city_ids = np.random.choice(range(1, 6), len(unique_field_ids))

    return pd.DataFrame(
        {"field_id": unique_field_ids, "latitude": latitudes, "longitude": longitudes, "city_id": city_ids}
    )


def main():
    slots = create_slots(1000)
    fields = create_clubs(slots)
    with sqlite3.connect("fields_data.db") as conn:
        slots.to_sql("slots", conn, if_exists="replace", index=False)
        fields.to_sql("fields", conn, if_exists="replace", index=False)
        conn.commit()


if __name__ == "__main__":
    main()
