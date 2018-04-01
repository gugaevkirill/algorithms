import time
from typing import List, Tuple
from collections import namedtuple
import numpy as np


car_park = namedtuple('car_park', ['x', 'y', 'distance'])

class Parking:
    def minTime(self, park_raw: List[str]) -> int:
        start_time = time.time()
        
        # Build 2d-array from input
        park = self.read_input(park_raw)
        
        # Step 1: collect all the cars
        cars = []
        count_parks = 0
        
        it = np.nditer(park, flags=['multi_index'], op_flags=['readonly'])
        while not it.finished:
            # If we find car,
            if it[0] == 'C':
                cars.append(it.multi_index)
            elif it[0] == 'P':
                count_parks += 1
            it.iternext()
        
        if count_parks != len(cars):
            return -1
        
        # Step 2: for each car find possible parks
        car_parks_map = []
        for car in cars:
            car_parks = self.find_parks(park, car)
            if not len(car_parks):
                return -1

            car_parks_map.append(car_parks)
        
        # Step 3: run binary search to find optimal pairs
        result_time = self.get_min_time(park)
        
        eval_time = time.time() - start_time
        print(f'{eval_time} sec', end='\n\n')

        return result_time
        
    def read_input(self, park: List[str]) -> np.ndarray:
        pass
    
    def find_parks(self, park: np.ndarray, car: Tuple(int, int)) -> List[car_park]:
        """
        Find all the parks available to given car standing on (i, j).
        """
        pass
    
    def get_min_time(self, park: np.ndarray, car_parks_map: List[List[car_park]]) -> int:
        pass


parking = Parking()


# Every car just drives to the opposite parking spot.
park = [
    "C.....P",
    "C.....P",
    "C.....P",
]
assert 6 == parking.minTime(park)

# The slalom takes the car 16 units of time.
park = [
    "C.X.....",
    "..X..X..",
    "..X..X..",
    ".....X.P",
]
assert 16 == parking.minTime(park)

# This would take 11 instead of 5 units of time if the car on the bottom drove to its nearest parking spot.
park = [
    "XXXXXXXXXXX",
    "X......XPPX",
    "XC...P.XPPX",
    "X......X..X",
    "X....C....X",
    "XXXXXXXXXXX",
]
assert 5 == parking.minTime(park)

# While driving, the cars can be on the same empty spot or parking spot, but they have to finish on different parking spots.
park = [
    ".C.",
    "...",
    "C.C",
    "X.X",
    "PPP",
]
assert 4 == parking.minTime(park)

# There are not enough parking spots for all the cars.
park = [
    "CCCCC",
    ".....",
    "PXPXP",
]
assert -1 == parking.minTime(park)

# The car can't reach the parking spot.
park = [
    "..X..",
    "C.X.P",
    "..X..",
]
assert -1 == parking.minTime(park)
