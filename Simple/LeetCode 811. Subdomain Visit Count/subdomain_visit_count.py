from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        counts = defaultdict(int)
        
        # Step 1: calculate counts
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            
            for child in self._get_children(domain):
                counts[child] += count
        
        # Step 2: build result list
        return ['{} {}'.format(value, domain) for domain, value in counts.items()]
        
        
    def _get_children(self, domain):
        current = ''
        for part in reversed(domain.split('.')):
            current = '{}.{}'.format(part, current)
            yield current[:-1]

solver = Solution()

#Example 1:
# We only have one website domain: 'discuss.leetcode.com'. As discussed above, the subdomain 'leetcode.com' and 'com' will also be visited. So they will all be visited 9001 times.
input = ['9001 discuss.leetcode.com']
output = ['9001 discuss.leetcode.com', '9001 leetcode.com', '9001 com']
assert set(output) == set(solver.subdomainVisits(input))

# Example 2:
# We will visit 'google.mail.com' 900 times, 'yahoo.com' 50 times, 'intel.mail.com' once and 'wiki.org' 5 times. For the subdomains, we will visit 'mail.com' 900 + 1 = 901 times, 'com' 900 + 50 + 1 = 951 times, and 'org' 5 times.
input = ['900 google.mail.com', '50 yahoo.com', '1 intel.mail.com', '5 wiki.org']
output = ['901 mail.com', '50 yahoo.com', '900 google.mail.com', '5 wiki.org', '5 org', '1 intel.mail.com', '951 com']
assert set(output) == set(solver.subdomainVisits(input))
