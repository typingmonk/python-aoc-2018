"""
from datetime import datetime, timedelta

fmt = "%Y-%m-%d %H:%M"

d1 = "1518-11-01 23:58"
d2 = "1518-11-02 00:08"

diff = datetime.strptime(d2, fmt) - datetime.strptime(d1, fmt)
print("minutes:", int(diff.seconds/60))
"""

for i in range(2,5):
    print("Test ",i)