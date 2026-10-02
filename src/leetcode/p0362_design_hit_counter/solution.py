"""
Design a hit counter which counts the number of hits received in the past 5
minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and
you may assume that calls are being made to the system in chronological order
(i.e., timestamp is monotonically increasing). Several hits may arrive roughly
at the same time.

Implement the HitCounter class:

- HitCounter() Initializes the object of the hit counter system.
- void hit(int timestamp) Records a hit that happened at timestamp (in seconds).
  Several hits may happen at the same timestamp.
- int getHits(int timestamp) Returns the number of hits in the past 5 minutes
  from timestamp (i.e., the past 300 seconds).
"""

from collections import deque


class HitCounter:
    def __init__(self) -> None:
        self.hit_queue = deque()

    def hit(self, timestamp: int) -> None:
        self.hit_queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hit_queue and timestamp - self.hit_queue[0] >= 300:
            self.hit_queue.popleft()

        return len(self.hit_queue)
