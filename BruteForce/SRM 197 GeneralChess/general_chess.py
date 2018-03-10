import time


class GeneralChess:
    def attackPositions(self, pieces):
        print(pieces)
        start_time = time.time()
        
        positions = self._get_positions(pieces[0])
        for figure in pieces[1:]:
            positions.intersection_update(self._get_positions(figure))
    
        eval_time = round(time.time() - start_time, 4)
        print(f'{eval_time} sec', end='\n\n\n')
        
        ans_int = sorted(list(positions))
        
        return tuple(f'{x},{y}' for x, y in ans_int)

    def _get_positions(self, coords):
        x, y = map(int, coords.split(','))
        
        ans = set()
        for multiplier in ((1, 2), (2, 1)):
            for x_dir in (1, -1):
                for y_dir in (1, -1):
                    xn = x + multiplier[0] * x_dir
                    yn = y + multiplier[1] * y_dir
                    
                    ans.add((xn, yn))
        
        return ans


game = GeneralChess()

# Methods tests:
assert {(4, 6), (4, 2), (5, 5), (5, 3), (2, 6), (2, 2), (1, 5), (1, 3)} == game._get_positions('3,4')

# Solution checks:
# This location is threatened from eight different places.
assert ("-2,-1", "-2,1", "-1,-2", "-1,2", "1,-2", "1,2", "2,-1", "2,1",) == game.attackPositions(("0,0",))

# A knight may be in two places such that both pieces are threatened. In chess, placing your pieces in such positions is usually undesirable when your opponent has a knight.
assert ("0,0", "1,-1",) == game.attackPositions(("2,1", "-1,-2"))

assert tuple() == game.attackPositions(("0,0", "2,1"))

# No three pieces can ever be threatened by a knight from more than one position.
# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
assert ("-1001,998",) == game.attackPositions(("-1000,1000", "-999,999", "-999,997"))
