class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []

        def dfs(start):
            if len(path) == 4 and start == len(s):
                res.append(".".join(path))
                return

            digit = ''
            for i in range(start,len(s)):
                digit += s[i]
                if not digit.isdigit() or int(digit) > 255 or (digit.startswith('0') and len(digit) > 1):
                    continue
                
                path.append(digit)
                dfs(i+1)
                path.pop()
        
        dfs(0)
            
        return res