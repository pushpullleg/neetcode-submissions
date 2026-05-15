class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dest in sorted(tickets):
            adj[src].append(dest)
        #print(adj)
        res = ["JFK"]
        def dfs(city):
            if len(res) == len(tickets) + 1:
                return True
            if city not in adj:
                return False
            temp = list(adj[city])
            for idx, dest in enumerate(temp):
                res.append(dest)
                adj[city].pop(idx)
                if dfs(dest):
                    return True
                res.pop()
                adj[city].insert(idx, dest)
            return False

        dfs("JFK")
        return res