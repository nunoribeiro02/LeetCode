class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for e in emails:
            email = e.split('@')
            # change stuff before the @
            local_name = email[0].split('+') # ignore anything after +
            local_name[0] = local_name[0].split('.')
            local_name[0] = ''.join(local_name[0]) # remove '.'
            email[0] = local_name[0]
            email[0] = ''.join([email[0], '@']) # add back the @
            email = ''.join(email)
            res.add(email)
        
        return len(res)