from collections import defaultdict
from typing import List

class LogSystem:

    def __init__(self):
        self.index = {
            "Year": 4,
            "Month": 7,  
            "Day": 10,
            "Hour": 13, 
            "Minute": 16,
            "Second": 19,
        }
        self.logs = []

    def put(self, id: int, ts: str) -> None:
        self.logs.append((id, ts))

    def retrieve(self, start: str, end: str, g: str) -> List[int]:
        logs = []
        until = self.index[g]
        for log in self.logs:
            id, ts = log
            if start[:until] <= ts[:until] <= end[:until]:
                logs.append(id)
        
        return logs