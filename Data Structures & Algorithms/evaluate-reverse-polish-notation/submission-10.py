class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        res = 0
        for i in range(len(tokens)):
            if tokens[i] == "+":
                RO = num.pop()
                LO = num.pop()
                res = LO + RO
                num.append(res)
                continue
            elif tokens[i] == "-":
                RO = num.pop()
                LO = num.pop()
                res = LO - RO
                num.append(res)
                continue
            elif tokens[i] == "*":
                RO = num.pop()
                LO = num.pop()
                res = RO * LO
                num.append(res)
                continue
            elif tokens[i] == "/":
                RO = num.pop()
                LO = num.pop()
                res = int(LO / RO)
                num.append(res)
                continue
            num.append(int(tokens[i]))
        return num[0]
            
            