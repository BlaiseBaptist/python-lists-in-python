from statistics import median
import random
from time import thread_time


class linked_list():
    def __init__(self, contents=[], first=None):
        self.first = linked_list.__node(None,first)
        self.last = self.first
        self.len = 0
        for e in contents:
            self.append(e)

    class __node():
        def __init__(self, item, next=None):
            self.item = item
            self.next = next

        def getItem(self):
            return (self.item)

        def getNext(self):
            return (self.next)

        def setNext(self, next):
            self.next = next

        def setItem(self, item):
            self.item = item

    def append(self, item):
        self.len += 1
        node = linked_list.__node(item)
        self.last.setNext(node)
        self.last = node

    def __iter__(self):
        spot = self.first.getNext()
        while spot is not None:
            yield spot.getItem()
            spot = spot.getNext()

    def __str__(self):
        s = '['
        for i in self:
            s += str(i) + ','
        s = s.rstrip(',') + ']'
        return (s)

    def __getitem__(self, index):
        if index >= 0 and index < self.len:
            spot = self.first.getNext()
            for _ in range(index):
                spot = spot.getNext()
            return (spot.getItem())
        raise IndexError('thats not a good spot')

    def __setitem__(self, index, val):
        if index >= 0 and index < self.len:
            spot = self.first.getNext()
            for _ in range(index):
                spot = spot.getNext()
            spot.setItem(val)
        else:
            raise IndexError('thats not a good spot')

    def __contains__(self, item):
        for i in self:
            if i == item:
                return (True)
        return (False)

    def __eq__(self, other):
        if type(self) != type(other):
            return (False)
        if self.len != other.len:
            return (False)
        spot1 = self.first.getNext()
        spot2 = other.first.getNext()
        for _ in range(self.len):
            if spot1.getItem() != spot2.getItem():
                return (False)
            spot1 = spot1.getNext()
            spot2 = spot2.getNext()
        return (True)

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError('how would you do that')
        new_list = linked_list()
        for i in self:
            new_list.append(i)
        for e in other:
            new_list.append(e)
        return (new_list)

    def insert(self, item, index):
        if index > self.len:
            raise IndexError('out of range')
        spot = self.first.getNext()
        for _ in range(index):
            spot = spot.getNext()
        new_node = linked_list.__node(item, spot.getNext())
        spot.setNext(new_node)
        self.len += 1

    def __delitem__(self, index):
        if index > self.len:
            raise IndexError('out of range')
        spot = self.first
        for _ in range(index):
            spot = spot.getNext()
        spot.setNext(spot.getNext().getNext())
        self.len -= 1

    def __len__(self):
        return (self.len)

    def is_sorted(self):
        spot = self.first.getNext()
        for _ in range(self.len - 1):
            if spot.getItem() > spot.getNext().getItem():
                return (False)
            spot = spot.getNext()
        return (True)

    def swap(self, i, j):
        i_val = self[i]
        self[i] = self[j]
        self[j] = i_val

    def bubble_sort(self):
        while not self.is_sorted():
            for i in range(self.len - 1):
                if self[i] > self[i + 1]:
                    self.swap(i, i + 1)

    def bubble_sort_2(self):
        times = 0
        swaps = True
        while swaps:
            times += 1
            swaps = False
            for i in range(self.len - times):
                if self[i] > self[i + 1]:
                    self.swap(i, i + 1)
                    swaps = True

    def bubble_sort_3(self):
        swaps = True
        while swaps:
            swaps = False
            spot = self.first.getNext()
            while spot.getNext() is not None:
                if spot.getItem() > spot.getNext().getItem():
                    old_spot = spot.getItem()
                    spot.setItem(spot.getNext().getItem())
                    spot.getNext().setItem(old_spot)
                    swaps = True
                spot = spot.getNext()

    def merge_sort(self):
        if self.len <= 1:
            return
        right = self.split()
        self.merge_sort()
        right.merge_sort()
        self.merge(right)

    def split(self):
        spot = self.first
        if self.len <= 1:
            raise Exception("list too short")
        for i in range(self.len//2):
            spot = spot.getNext()
        right_node = spot.getNext()
        spot.setNext(None)
        right = linked_list(first = right_node)
        right.last = self.last
        right.len = self.len - i - 1
        self.len = i + 1
        self.last = spot
        return(right)

    def merge(self,right):
        left = linked_list(first=self.first)
        del left[0]
        rspot = right.first.getNext()
        lspot = left.first.getNext()
        self.first = linked_list.__node(None)
        self.last = self.first
        self.len = 0
        done = False
        while not done:
            if rspot.getItem() < lspot.getItem():
                self.append(rspot.getItem())
                if rspot.getNext() is None:
                    while lspot is not None:
                        self.append(lspot.getItem())
                        lspot = lspot.getNext()
                    done = True
                else:
                    rspot = rspot.getNext()
            else:
                self.append(lspot.getItem())
                if lspot.getNext() is None:
                    while rspot is not None:
                        self.append(rspot.getItem())
                        rspot = rspot.getNext()
                    done = True
                else:
                    lspot = lspot.getNext()

        
def time_bubble(to_sort):
    link_list = linked_list(to_sort)
    time = thread_time()
    link_list.merge_sort()
    return (thread_time() - time)


def test_bubble(n, shuffle_amount, f):
    for i in range(2, n):
        time_list = []
        for x in range(5):
            bad_time_list = [
                time_bubble(make_list_reverse(i)),
                time_bubble(make_list_almost(i, shuffle_amount)),
                time_bubble(make_list_shuffle(i)),
                time_bubble(list(range(i)))
            ]
            time_list.append(bad_time_list)
        print(i)
        good_time_list = median(time_list)
        f.write('\n')
        f.write(str(i))
        for h in good_time_list:
            f.write(',')
            f.write(str(h))


def make_list_almost(size, shuffle_amount):
    stuff = linked_list()
    for i in range(size):
        stuff.append(i)
    for i in range(shuffle_amount):
        stuff.swap(random.randint(0, size - 1), random.randint(0, size - 1))
    return (stuff)


def make_list_shuffle(size):
    stuff = list(range(size))
    random.shuffle(stuff)
    stuff_list = linked_list()
    for i in stuff:
        stuff_list.append(i)
    return (stuff_list)


def make_list_reverse(size):
    stuff = list(range(size, 1, -1))
    return (stuff)


def main():
    size = 302
    f = open('data' + str(size) + '.csv', 'w')
    f.write("number of elments,reverse,almost sorted,shuffed,sorted")
    test_bubble(size, 25, f)
    f.close()
    
def test():
    link_list = linked_list(range(10,0,-1))
    print(link_list)
    link_list.merge_sort()
    print(link_list)
#test()
main()
