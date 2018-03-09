import time
from collections import deque


class ClassName:
    def method_name(self, start, finish, constr):
        print(start)
        max_depth = 0
        start_time = time.time()
    
        # Queue for BFS
        queue = deque([(start, 0)])
    
        # Already visited vertexes
        processed = {start}
    
        # Recursively process every vertex in graph
        ans = -1
        while queue:
            current, steps = queue.popleft()
        
            # Print progress
            if max_depth < steps:
                max_depth = steps
                print(max_depth, end=' ', flush=True)
        
            for next in self._get_next(current):
                if next in constr:
                    continue
                
                if next == finish:
                    ans = steps + 1
                    break
                
                # TODO: process next vertex
                
                queue.append((next, steps + 1))
            
                # To prevent multiple processing of same vertex
                processed.add(next)
            
            if ans != -1:
                break
    
        eval_time = round(time.time() - start_time, 4)
        print(f'\n{eval_time} sec', end='\n\n\n')
        
        return ans

    def _get_next(self, vertex):
        # TODO: implement this
        return []


obj = ClassName()

# Methods tests:
# TODO: add your tests
assert [] == obj._get_next(1)

# Solution checks:
# TODO: add tests from examples
