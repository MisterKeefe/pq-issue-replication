"""Worker script"""
from pq.tasks import PQ

from config import get_db_connection

# Uncomment/comment this line to fix things
# from tasks import dummy_task

pq = PQ(get_db_connection())

queue = pq['default']

if __name__ == "__main__":
    queue.work()