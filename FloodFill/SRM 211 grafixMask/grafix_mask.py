import time
from collections import deque
import numpy as np


class grafixMask:
    def __init__(self):
        self.x_max = 399
        self.y_max = 599
    
    def sortedAreas(self, filled_raw):
        print(filled_raw)
        start_time = time.time()
        
        # Prepare rectangles
        filled = self._prepare_filled(filled_raw)
        
        visited = np.zeros((400, 600), dtype=np.bool)
        
        areas = []
        
        # Iterate throw all the rectangles borders:
        for pixel in self._borders_iterator(filled):
            if not visited[pixel[0], pixel[1]] and not self._is_filled(pixel, filled):
                # If we find not visited white point, we will start BFS search from it
                areas.append(self._white_area_bfs(pixel, filled, visited))

        eval_time = round(time.time() - start_time, 4)
        print(f'{eval_time} sec', end='\n\n')
        
        return tuple(sorted(areas))
    
    def _prepare_filled(self, filled_raw):
        return tuple(
            tuple(int(num) for num in rect_str.split())
            for rect_str in filled_raw
        )
    
    def _borders_iterator(self, filled):
        for x_min, y_min, x_max, y_max in filled:
            if x_min > 0:
                for y in range(y_min, y_max + 1):
                    yield x_min - 1, y
            if y_max < self.y_max:
                for x in range(x_min, x_max + 1):
                    yield x, y_max + 1
            if x_max < self.x_max:
                for y in range(y_max, y_min - 1, -1):
                    yield x_max + 1, y
            if y_min > 0:
                for x in range(x_max, x_min - 1, -1):
                    yield x, y_min - 1
                    
    
    def _white_area_bfs(self, start_point, filled, visited):
        """
        Breadth first search across all the contiguous white pixels.
        Returns calculated area and set this points as visited.
        """

        # Queue for BFS
        queue = deque([start_point])

        # Already visited pixels
        visited[start_point[0], start_point[1]] = True

        # Recursively process every pixel in graph
        area = 0
        while queue:
            point = queue.popleft()
            area += 1

            for next_point in self._get_next(point):
                if visited[next_point[0], next_point[1]] or self._is_filled(next_point, filled):
                    continue

                queue.append(next_point)
        
                # To prevent multiple processing of same words
                visited[next_point[0], next_point[1]] = True

        return area


    def _is_filled(self, point, filled):
        """
        returns True if point is inside one of filled rectangles
        """
        
        x = point[0]
        y = point[1]
        for x_min, y_min, x_max, y_max in filled:
            if x_min <= x <= x_max and y_min <= y <= y_max:
                return True

        return False

    def _get_next(self, point):
        """
        (5, 8) -> ((4, 8), (6, 8), (5, 9), (5, 7))
        """

        for i in range(4):
            xn, yn = point
            
            if (i - 1) % 2:
                xn += i - 1
            
            if i % 2:
                yn += i - 2
            
            if xn < 0 or xn > self.x_max or yn < 0 or yn > self.y_max:
                continue
            
            yield xn, yn
        


graffix = grafixMask()

# Methods tests:
assert ((0, 292, 399, 307),) == graffix._prepare_filled(("0 292 399 307",))
assert ((48, 192, 351, 207), (48, 392, 351, 407), (120, 52, 135, 547), (260, 52, 275, 547)) == graffix._prepare_filled(("48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"))

assert {(1, 0), (0, 1)} == set(graffix._get_next((0, 0)))
assert {(4, 8), (6, 8), (5, 9), (5, 7)} == set(graffix._get_next((5, 8)))

assert True == graffix._is_filled((292, 307), ((0, 292, 399, 307),))
assert False == graffix._is_filled((100, 150), ((0, 292, 399, 307),))
assert False == graffix._is_filled((0, 0), ((48, 192, 351, 207), (48, 392, 351, 407), (120, 52, 135, 547), (260, 52, 275, 547)))
assert True == graffix._is_filled((125, 400), ((48, 192, 351, 207), (48, 392, 351, 407), (120, 52, 135, 547), (260, 52, 275, 547)))

assert 4 == graffix._white_area_bfs((0, 1), ((2, 0, 2, 100), (0, 2, 100, 2)), np.zeros((400, 600), dtype=np.bool))
assert 116800 == graffix._white_area_bfs((5, 9), ((0, 292, 399, 307), ), np.zeros((400, 600), dtype=np.bool))
assert 239504 == graffix._white_area_bfs((100, 13), ((0, 292, 30, 307), ), np.zeros((400, 600), dtype=np.bool))

assert [(2, 4), (2, 5), (3, 6), (4, 5), (4, 4), (3, 3)] == list(graffix._borders_iterator(((3, 4, 3, 5), )))
assert [(1, 2), (2, 3), (3, 2), (2, 1), (4, 5), (5, 6), (6, 5), (5, 4)] == list(graffix._borders_iterator(((2, 2, 2, 2), (5, 5, 5, 5))))


# Solution checks:
# The masking layer is depicted below in a 1:4 scale diagram.
assert (116800, 116800) == graffix.sortedAreas(("0 292 399 307",))

assert (22816, 192608) == graffix.sortedAreas(("48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"))

assert (22080, 22816, 22816, 23040, 23040, 23808, 23808, 23808, 23808) == graffix.sortedAreas(
    ("0 192 399 207", "0 392 399 407", "120 0 135 599", "260 0 275 599"))

assert (1, 239199) == graffix.sortedAreas(("50 300 199 300", "201 300 350 300", "200 50 200 299", "200 301 200 550"))

assert (
15, 30, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 100, 115, 115,
115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 200, 230,
230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 300,
300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345, 345,
345) == graffix.sortedAreas((
                           "0 20 399 20", "0 44 399 44", "0 68 399 68", "0 92 399 92", "0 116 399 116", "0 140 399 140",
                           "0 164 399 164", "0 188 399 188", "0 212 399 212", "0 236 399 236", "0 260 399 260",
                           "0 284 399 284", "0 308 399 308", "0 332 399 332", "0 356 399 356", "0 380 399 380",
                           "0 404 399 404", "0 428 399 428", "0 452 399 452", "0 476 399 476", "0 500 399 500",
                           "0 524 399 524", "0 548 399 548", "0 572 399 572", "0 596 399 596", "5 0 5 599",
                           "21 0 21 599", "37 0 37 599", "53 0 53 599", "69 0 69 599", "85 0 85 599", "101 0 101 599",
                           "117 0 117 599", "133 0 133 599", "149 0 149 599", "165 0 165 599", "181 0 181 599",
                           "197 0 197 599", "213 0 213 599", "229 0 229 599", "245 0 245 599", "261 0 261 599",
                           "277 0 277 599", "293 0 293 599", "309 0 309 599", "325 0 325 599", "341 0 341 599",
                           "357 0 357 599", "373 0 373 599", "389 0 389 599"))
