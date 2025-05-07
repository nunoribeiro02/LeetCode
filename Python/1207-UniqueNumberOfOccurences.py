class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_ = {}
        for n in arr:
            if n not in dict_:
                dict_[n] = 0
            dict_[n] += 1

        return len(dict_) == len(set(dict_.values()))
