import time
from progressbar import ProgressBar

pb = ProgressBar("Example Progress Bar")
pb.start()

for i in range(10):
    pb.move_ten()
    time.sleep(.5)
