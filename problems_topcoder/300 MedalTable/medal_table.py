import time
from collections import defaultdict
import numpy as np


class MedalTable:
    def generate(self, results):
        countries = defaultdict(lambda: defaultdict(int))
        for result in results:
            winners = result.split()
            countries[winners[0]]['g'] += 1
            countries[winners[1]]['s'] += 1
            countries[winners[2]]['b'] += 1
        
        ndarray = np.array(
            [
                (country, 1 / (medals['g'] + 1), 1 / (medals['s'] + 1), 1 / (medals['b'] + 1))
                for country, medals in countries.items()
            ],
            dtype=[('name', 'S3'), ('g', np.float16), ('s', np.float16), ('b', np.float16)]
        )

        ndarray.sort(order=['g', 's', 'b', 'name'])
        
        return tuple(self.get_item_string(item) for item in ndarray)
    
    def get_item_string(self, item):
        return item['name'].decode('utf-8') \
               + ' ' \
               + str(int(round(-1 + 1 / item['g']))) \
               + ' ' \
               + str(int(round(-1 + 1 / item['s']))) \
               + ' ' \
               + str(int(round(-1 + 1 / item['b'])))
               

start_time = time.time()
mt = MedalTable()

# These are the results of the archery competitions.
result = mt.generate(('ITA JPN AUS', 'KOR TPE UKR', 'KOR KOR GBR', 'KOR CHN TPE'))
assert ('KOR 3 1 0', 'ITA 1 0 0', 'TPE 0 1 1', 'CHN 0 1 0', 'JPN 0 1 0', 'AUS 0 0 1', 'GBR 0 0 1', 'UKR 0 0 1') == result


result = mt.generate(('USA AUT ROM',))
assert ('USA 1 0 0', 'AUT 0 1 0', 'ROM 0 0 1') == result

result = mt.generate(('GER AUT SUI', 'AUT SUI GER', 'SUI GER AUT'))
assert ('AUT 1 1 1', 'GER 1 1 1', 'SUI 1 1 1') == result


print('--- %s seconds ---' % (time.time() - start_time))