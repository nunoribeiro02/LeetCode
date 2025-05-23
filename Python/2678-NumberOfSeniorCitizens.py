class Solution:
    def countSeniors(self, details: List[str]) -> int:
        target_age = 60
        res = 0
        for p in details:
            if target_age < int(p[11:13]):
                res += 1

        return res