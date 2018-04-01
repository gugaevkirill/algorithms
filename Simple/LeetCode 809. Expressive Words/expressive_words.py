class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        s_groups = self._get_groups(S)
        words_groups = [self._get_groups(word) for word in words]
        
        # Filter words
        words_groups = [wg for wg in words_groups if len(wg) == len(s_groups)]

        satisfy = [1] * len(words_groups)
        
        for i in range(len(s_groups)):
            for num, wg in enumerate(words_groups):
                if not satisfy[num]:
                    continue
                
                if not self._group_can_be_extended(wg[i], s_groups[i]):
                    satisfy[num] = 0
        
        return satisfy.count(1)
    
    def _group_can_be_extended(self, group, target):
        if group == target:
            return True
        
        if len(target) < 3 or len(target) <= len(group):
            return False
        
        return group[0] == target[0]
        
        
    def _get_groups(self, S):
        groups = []
        current = ''
        for letter in S:
            if not current:
                current = letter
            elif current[0] != letter:
                groups.append(current)
                current = letter
            else:
                current += letter
        
        if current:
            groups.append(current)
        
        return groups
        

solver = Solution()

assert ['q', 'w', 'e', 'r'] == solver._get_groups('qwer')
assert ['aa', 'b', 'cc'] == solver._get_groups('aabcc')
assert ['eee'] == solver._get_groups('eee')

# Example:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.
assert 1 == solver.expressiveWords("heeellooo", ["hello", "hi", "helo"])
