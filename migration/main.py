import sys

import pandas as pd
from fetch import fetch

sys.path.append("/Users/joselondono/Documents/projects/playmaker")
from app.db.database import engine


def add_datetime(timeslots: pd.DataFrame) -> pd.DataFrame:
    start_datetime = pd.to_datetime(timeslots['date'] + ' ' + timeslots['start_time'])
    end_datetime = pd.to_datetime(timeslots['date'] + ' ' + timeslots['end_time'])

    timeslots['start_datetime'] = start_datetime
    timeslots['end_datetime'] = end_datetime
    return timeslots


def main(days: int):
    
    # Fetch data
    timeslots = fetch(days, delay=15)
    timeslots_datetime = add_datetime(timeslots)
    
    # Rewrite data in current table
    with engine.connect() as conn:
        timeslots_datetime.to_sql("timeslots", conn, if_exists="replace", index=False)
        conn.commit()

if __name__ == "__main__":
    main(days=15)
