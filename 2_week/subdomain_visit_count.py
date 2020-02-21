from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output = {}
        for item in cpdomains:
            num, domain = item.split()
            domains = domain.split('.')
            for i in range(len(domains)):
                seq = '.'.join(domains[i:])
                output[seq] = output.setdefault(seq, 0) + int(num)
        return [f'{v} {k}' for k, v in output.items()]
