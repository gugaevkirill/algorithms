import time
from collections import deque


class CaptureThemAll:
    def fastKnight(self, knight_str, rook_str, queen_str):
        """
        # From "a1", the knight can move directly to "b3" and capture the rook. From there, the knight can move directly to "c5" and capture the queen.
        >>> game = CaptureThemAll()
        >>> game.fastKnight("a1", "b3", "c5")
        2
        
        # The rook and the queen are both 1 move away from the knight. Once the knight captures one of them (it doesn't matter which one), it can return to its starting location, and capture the other piece in one more move.
        >>> game.fastKnight("b1", "c3", "a3")
        3
        
        # The rook and the queen are close, but it takes 6 moves to capture them.
        >>> game.fastKnight("a1", "a2", "b2")
        6
        
        >>> game.fastKnight("a5", "b7", "e4")
        3
        
        # This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
        >>> game.fastKnight("h8", "e2", "d2")
        6
        """
        print(knight_str, rook_str, queen_str)
        max_depth = 0
        start_time = time.time()
        
        knight = self._get_int_coords(knight_str)
        rook = self._get_int_coords(rook_str)
        queen = self._get_int_coords(queen_str)
    
        # Queue for BFS
        queue = deque([(knight, 0, 0b00)])
    
        # Already visited vertexes
        processed = {(knight, 0b00)}
    
        # Recursively process every vertex in graph
        ans = -1
        while queue:
            coords, steps, catched = queue.popleft()

            # Print progress
            if max_depth < steps:
                max_depth = steps
                print(max_depth, end=' ', flush=True)
            
            for new_coords in self._get_next(*coords):
                # Whom we catch after step into new_coords:
                will_catch = catched
                for i, figure in enumerate((rook, queen)):
                    if new_coords == figure:
                        will_catch |= i + 1
                
                if will_catch == 0b11:
                    ans = steps + 1
                    break
            
                queue.append((new_coords, steps + 1, will_catch))
            
                # To prevent multiple processing of same vertex
                processed.add((coords, will_catch))
                
            if ans != -1:
                break
    
        eval_time = round(time.time() - start_time, 4)
        print(f'\n{eval_time} sec', end='\n\n\n')
        
        return ans

    def _get_next(self, x, y):
        """
        >>> game = CaptureThemAll()
        >>> list(game._get_next(0, 0))
        [(1, 2), (2, 1)]
        
        >>> list(game._get_next(3, 4))
        [(4, 6), (4, 2), (2, 6), (2, 2), (5, 5), (5, 3), (1, 5), (1, 3)]
        """
        for multiplier in ((1, 2), (2, 1)):
            for x_dir in (1, -1):
                for y_dir in (1, -1):
                    xn = x + multiplier[0] * x_dir
                    yn = y + multiplier[1] * y_dir
                    
                    if xn < 1 or xn > 8 or yn < 1 or yn > 8:
                        continue
                    
                    yield xn, yn
            
    def _get_int_coords(self, str_coords):
        """
        >>> game = CaptureThemAll()
        >>> game._get_int_coords('a5')
        1, 5
        
        >>> game._get_int_coords('e4')
        5, 4
        """

        return ord(str_coords[0]) - ord('a') + 1, int(str_coords[1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
