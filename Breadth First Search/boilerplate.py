import time
from collections import deque


class ClassName:
    def method_name(self, start, constr):
        start_time = time.time()
    
        # Queue for BFS
        queue = deque([start])
    
        # Already visited words (vertexes)
        processed = {start}
    
        # Recursively process every vertex in graph
        while queue:
            current = queue.popleft()
        
            # TODO: process current vertex
        
            for next in self._get_next(current):
                if next in constr:
                    continue
                
                queue.append(next)
            
                # To prevent multiple processing of same words
                processed.add(next)
    
        eval_time = round(time.time() - start_time, 4)
        print(f'\n{eval_time} sec')

    def _get_next(self, vertex):
        # TODO: implement this
        return []


obj = ClassName()

# Methods tests:
# TODO: add your tests
assert [] == obj._get_next(1)

# Solution checks:
# TODO: add tests from examples
