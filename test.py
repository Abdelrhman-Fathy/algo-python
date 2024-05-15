#find the moving avegage
import collections
class MovingAverage:

    def __init__(self, size: int):
        #intialize the windowsize, total, queue to monitor the stream
        self.maxSize = size
        self.total = 0
        self.window = collections.dequeue
    def next(self, val: int) -> float:
        #add new item to the queue
        self.window.append(val)
        self.total += val
        if len(self.window) > self.maxSize:
            popped = self.window.popLeft()
            self.total -= popped
        return float(self.total/len(self.window))
        #if queue size is bigger than max size, remove item
        #subtract the popped item from the total
        #return total/queue length
