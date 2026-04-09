class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        def dfs(i: int, ip: List[str]):
            if i >= len(s):
                if len(ip) == 4:
                    ips.append('.'.join(ip[:]))
                return
            if len(ip) >= 4:
                return
            for j in range(i, min(i + 3, n)):
                segment = s[i:j+1]
                if int(segment) > 255:
                    break
                if len(segment) > 1 and segment[0] == "0":
                    break
                ip.append(segment)
                dfs(j+1, ip)
                ip.pop()
        
        ips = []
        dfs(0, [])
        return ips