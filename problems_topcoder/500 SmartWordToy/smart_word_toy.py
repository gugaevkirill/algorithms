# -*- coding: utf-8 -*-
import time
from itertools import product
from collections import deque


class SmartWordToy:
    def minPresses(self, start, finish, constraints_raw):
        """
        Use Breadth First Search to find a solution

        :param start:  str
        :param finish:  str
        :param constraints_raw:  Tuple[str]
        :return:  int
        """

        # To see the evaluation progress
        print(f'\n\n{start} -> {finish}')
        max_depth = 0
        start_time = time.time()
        
        # Queue for BFS
        # Put first elements in queue. We need 0 steps to reach start point.
        queue = deque([(start, 0)])
        
        # Set of disallowed vertexes
        constr = self._expand_constraints(constraints_raw)
        
        # If finish is prevented
        if finish in constr:
            return -1
        
        # Already visited words (vertexes)
        processed = {start}

        ans = -1
        # Recursively process every vertex in graph
        while queue:
            word, count = queue.popleft()
            count += 1
            
            # Print progress
            if count > max_depth:
                max_depth = count
                print(max_depth, end=' ', flush=True)
            
            for next_word in self._get_next_words(word):
                if next_word in constr or next_word in processed:
                    continue
                
                if next_word == finish:
                    ans = count
                    break
                
                queue.append((next_word, count))

                # To prevent multiple processing of same words
                processed.add(next_word)
            
            if ans != -1:
                break

        eval_time = round(time.time() - start_time, 4)
        print(f'\n{eval_time} sec')
        
        return ans

    def _expand_constraints(self, constr_tuple):
        """
        Returns set with all constraint words

        :param constr_tuple:  Tuple[str]
        :return:  Set[str]
        """
        
        return {
            ''.join(chars_tuple)
            for constr_string in constr_tuple
            for chars_tuple in product(*constr_string.split())
        }
    
    def _get_next_words(self, current_word):
        for i,letter in enumerate(current_word):
            letter_next = chr(ord(letter) + 1)
            letter_prev = chr(ord(letter) - 1)
            
            if letter == 'a':
                letter_prev = 'z'
            elif letter == 'z':
                letter_next = 'a'
            
            yield current_word[:i] + letter_next + current_word[i + 1:]
            yield current_word[:i] + letter_prev + current_word[i + 1:]
    


toy = SmartWordToy()

# Methods tests:
assert {'late', 'fate', 'lace', 'face'} == set(toy._expand_constraints(('lf a tc e',)))
assert {'qwer', 'ardf', 'aldf'} == set(toy._expand_constraints(('q w e r', 'a rl d f')))

assert {'baaa', 'zaaa', 'abaa', 'azaa', 'aaba', 'aaza', 'aaab', 'aaaz'} == set(toy._get_next_words('aaaa'))
assert {'rwer', 'pwer', 'qver', 'qxer', 'qwdr', 'qwfr', 'qweq', 'qwes'} == set(toy._get_next_words('qwer'))

# Solution checks:
assert 8 == toy.minPresses(
    'aaaa',
    'zzzz',
    ('a a a z', 'a a z a', 'a z a a', 'z a a a', 'a z z z', 'z a z z', 'z z a z', 'z z z a')
)

# Simply change each letter one by one to the following letter in the alphabet.
assert 4 == toy.minPresses('aaaa', 'bbbb', ())

# Just as in the previous example, we have no forbidden words. Simply apply the correct number of button presses for each letter and you're there.
assert 50 == toy.minPresses('aaaa', 'mmnn', ())

# Here is an example where it is impossible to go to any word from 'aaaa'.
assert -1 == toy.minPresses('aaaa', 'zzzz', ('bz a a a', 'a bz a a', 'a a bz a', 'a a a bz'))

assert 6 == toy.minPresses(
    'aaaa',
    'zzzz',
    ('cdefghijklmnopqrstuvwxyz a a a', 'a cdefghijklmnopqrstuvwxyz a a', 'a a cdefghijklmnopqrstuvwxyz a',
     'a a a cdefghijklmnopqrstuvwxyz')
)

assert -1 == toy.minPresses('aaaa', 'bbbb', ('b b b b',))

assert -1 == toy.minPresses(
    'zzzz',
    'aaaa',
    ('abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk',
     'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk', 'abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk')
)
