from collections import deque
import heapq


class MaxStack:
    def __init__(self):
        self.max_heap = []
        self.stack = deque()
        self.generation = 0

    def push(self, x: int) -> None:
        self.generation += 1
        n = Node(x, self.generation)

        self.stack.append(n)
        heapq.heappush(self.max_heap, n)

    def pop(self) -> int:
        while self.stack and not self.stack[-1].valid:
            self.stack.pop()

        n = self.stack.pop()
        n.valid = False

        return n.x

    def top(self) -> int:
        while self.stack and not self.stack[-1].valid:
            self.stack.pop()

        return self.stack[-1].x

    def peekMax(self) -> int:
        while self.max_heap and not self.max_heap[0].valid:
            heapq.heappop(self.max_heap)

        return self.max_heap[0].x

    def popMax(self) -> int:
        while self.max_heap and not self.max_heap[0].valid:
            heapq.heappop(self.max_heap)

        n = heapq.heappop(self.max_heap)
        n.valid = False

        return n.x


class Node:
    def __init__(self, x, generation):
        self.x = x
        self.generation = generation
        self.valid = True

    def __lt__(self, other):
        if self.x == other.x:
            return self.generation > other.generation

        return self.x > other.x