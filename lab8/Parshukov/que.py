import sys
import queue

class StacksQueue (queue.Queue):
    left = []
    right = []
    me = 0;

    def __init__ (self):
        pass

    def pop (self):
        if len (self.right) > 0:
            return self.right.pop()
        while len (self.left) > 0:
            self.right.append (self.left.pop())
        if len (self.right) > 0:
            return self.right.pop()
        return "empty"

    def last (self):
        if self.size() == 0:
            return "empty"
        if len (self.left) > 0:
            return self.left[len(self.left) - 1]
        return self.right[0]

    def size (self):
        return len (self.left) + len (self.right)

    def push (self, x):
        self.left.append (x)

class MaxElementQueue (queue.Queue):
    que = StacksQueue()
    cmax = 0

    def max(self):
        if self.que.size() == 0:
            return "empty"
        if len (self.que.left) > 0:
            return self.que.left[len (self.que.left) - 1][1]
        else:
            return self.que.right[len (self.que.right) - 1][1]

    def pop(self):
        if self.que.size() == 0:
            return "empty"
        if len (self.que.right) > 0:
            return self.que.right.pop()[0]
        while len (self.que.left) > 0:
            if (len (self.que.right) == 0):
                x = self.que.left.pop()[0]
                self.que.right.append ([x, x])
            else:
                x = self.que.left.pop()[0]
                self.que.right.append ([x, max (self.que.right[len (self.que.right) - 1][1], x)])
        if len (self.que.right) > 0:
            return self.que.right.pop()[0]
        return "empty"

    def push(self, x):
        if self.que.size() == 0:
            self.cmax = x
        if x > self.cmax:
            self.cmax = x
        self.que.push ([x, self.cmax])


s = MaxElementQueue()
while (True):
    k = sys.stdin.readline()
    if (k == "max\n"):
        print (s.max())
        continue
    if (k == "pop\n"):
        print (s.pop())
        continue
    k = k.split (' ')
    s.push (int (k[1]))
    print ("ok")
