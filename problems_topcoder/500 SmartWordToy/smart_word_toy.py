import time
from itertools import product
from queue import Queue, Empty


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
        
        # Already visited words (vertexes)
        processed = set()
        # Queue for BFS
        queue = Queue()
        # Set of disallowed vertexes
        constraints = self.expand_constraints(constraints_raw)
        
        # Put first elements in queue. We need 0 steps to reach start point.
        queue.put((start, 0))
        
        ans = -1
        try:
            # Recursively process every vertex in graph
            while True:
                vertex = queue.get(False)  # Non-blocking get
                word = vertex[0]
                count = vertex[1] + 1
                
                # Print progress
                if count > max_depth:
                    max_depth = count
                    print(max_depth, end=' ', flush=True)
                
                for next_word in self.get_next_words(word):
                    if next_word in processed or next_word in constraints:
                        continue
                    
                    if next_word == finish:
                        ans = count
                        break
                    
                    queue.put((next_word, count))
                    
                # To prevent multiple processing of same words
                processed.add(word)
                
                if ans != -1:
                    break
        except Empty:
            pass

        eval_time = round(time.time() - start_time, 4)
        print(f'\n{eval_time} sec')
        
        return ans

    def expand_constraints(self, constr_tuple):
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
    
    def get_next_words(self, current_word):
        for i in range(4):
            letter = current_word[i]
            if letter == 'a':
                letter_next = 'b'
                letter_prev = 'z'
            elif letter == 'z':
                letter_next = 'a'
                letter_prev = 'y'
            else:
                letter_next = chr(ord(letter) + 1)
                letter_prev = chr(ord(letter) - 1)
            
            yield current_word[0:i] + letter_next + current_word[i + 1: 4]
            yield current_word[0:i] + letter_prev + current_word[i + 1: 4]


toy = SmartWordToy()

# Methods tests:
assert {'late', 'fate', 'lace', 'face'} == toy.expand_constraints(('lf a tc e', ))
assert {'qwer', 'ardf', 'aldf'} == toy.expand_constraints(('q w e r', 'a rl d f'))

assert {'baaa', 'zaaa', 'abaa', 'azaa', 'aaba', 'aaza', 'aaab', 'aaaz'} == set(toy.get_next_words('aaaa'))
assert {'rwer', 'pwer', 'qver', 'qxer', 'qwdr', 'qwfr', 'qweq', 'qwes'} == set(toy.get_next_words('qwer'))

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

assert -1 == toy.minPresses('aaaa', 'bbbb', ('b b b b'))

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
