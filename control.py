import sys
a = sys.argv[1]
b = sys.argv[2]

from py1 import sum
from py2 import min

print('Sum = ',sum(int(a), int(b)))
print('Min = ',min(int(a), int(b)))