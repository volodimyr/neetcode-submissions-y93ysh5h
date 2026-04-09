class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        my_list =[]
        for i in range (len(tasks)):
            my_list.append(Task(i,tasks[i][0], tasks[i][1]))
        sorted_tasks = sorted(my_list, key=lambda p: p.enqueue, reverse=True)

        min_heap = []
        cur_time = sorted_tasks[-1].enqueue
        processed = []
        while sorted_tasks or len(min_heap) > 0:             
            while sorted_tasks and sorted_tasks[-1].enqueue <= cur_time:
                heapq.heappush(min_heap, sorted_tasks.pop())
            if len(min_heap) < 1:
                cur_time = sorted_tasks[-1].enqueue
            else:
                task = heapq.heappop(min_heap)
                cur_time = cur_time+task.processing
                processed.append(task.index)

        return processed

class Task:
    def __init__(self, index, enqueue, processing):
        self.index = index
        self.enqueue = enqueue
        self.processing = processing

    def __lt__(self, other):
        if self.processing == other.processing:
            return self.index < other.index
        return self.processing < other.processing