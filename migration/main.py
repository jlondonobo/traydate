import sqlite3

from fetch import fetch


def main(days: int):
    
    # Fetch data
    timeslots = fetch(days, delay=15)
    
    # Rewrite data in current table
    with sqlite3.connect("fields_data.db") as conn:
        timeslots.to_sql("timeslots", conn, if_exists="replace", index=False)
        conn.commit()

if __name__ == "__main__":
    main(days=15)
