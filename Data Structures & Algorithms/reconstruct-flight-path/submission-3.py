class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        iterenary = []

        def dfs(airport):

            while adj[airport]:
                dfs(heapq.heappop(adj[airport]))
            
            iterenary.append(airport)


        dfs('JFK')
        
        return iterenary[::-1]
