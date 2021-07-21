"""Definition of the task function"""
import time
import random 

from pq.tasks import PQ

from config import get_db_connection

pq = PQ(get_db_connection())

queue = pq['default']

@queue.task()
def dummy_task(job_id):
    print(f"Job {job_id} processing...")
    time.sleep(random.random() * 5)