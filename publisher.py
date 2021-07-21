"""Publisher script"""
import time

from pq.tasks import PQ

from config import get_db_connection
from tasks import dummy_task
    
if __name__ == "__main__":
    conn = get_db_connection()
    try:
        pq = PQ(conn)
        pq.create()
    except Exception as err:
        print(err)

    tasks_scheduled = 0

    while True:
        dummy_task()
        
        print(f"Scheduled task {tasks_scheduled}...")
        tasks_scheduled += 1

        # This is just a quick way to check the size of the task 
        # table without using `psql`; it can be commented out
        # without changing program behaviour
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM queue")
        print(f"There are {cur.fetchone()[0]} tasks total in the queue")

        time.sleep(2)