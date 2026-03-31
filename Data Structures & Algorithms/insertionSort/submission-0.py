# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        state = []
        state.append([value for value in pairs])
        if len(pairs) == 1:
            return state
        for i in range(1,len(pairs)):
            j = i
            if pairs[i-1].key > pairs[i].key:
                remove = pairs.pop(i)
                num = remove.key
                while j > 0 and pairs[j - 1].key > num:
                    j -= 1
                pairs.insert(j,remove)
            state.append([value for value in pairs])
        return state
