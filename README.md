# PQ task bug replication 

Tested with `python==3.9.5` and package versions in `requirements.txt` 

## Testing

Spin up a `postgres` instance somehow. I used:

```
docker run --rm -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres
```

Then in one terminal, run `python publisher.py` to start publishing tasks.
In another, run `python consumer.py` to start consuming tasks.

## Scenarios 

- When running `consumer.py`, if line `7` is commented out and the task is not imported,
then the pq `queue` table in postgres will rapidly grow in size (as seen through `publisher.py` output). 
No output will be produced by the `consumer.py` script even though the `dummy_task` task should print 
to stdout.

- When running `consumer.py` with line `7` *un*commented then the pq `queue` table will grow much more
slowly (only from the inserts from `publisher.py`). `consumer.py` will produce output as it executes
the tasks successfully.
