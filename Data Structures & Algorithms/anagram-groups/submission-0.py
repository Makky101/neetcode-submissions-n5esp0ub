class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        seen = set()
        for word in strs:
            checker =  "".join(sorted(word))

            if checker in seen:
                for gang in groups:

                    if "".join(sorted(gang[0])) == checker:
                        gang.append(word) 
                        break
            else:
                seen.add(checker)
                groups.append([word])

        return groups