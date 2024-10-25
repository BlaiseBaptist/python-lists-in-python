from statistics import median
import random
from time import thread_time
from math import log


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
            raise TypeError('haha i got to make the error mesage \n btw cant add differnt types')
        if self == other:
            raise ReferenceError("cant add self to self") 
        if other.len <= 0:
            return(self)
        self.last.setNext(other.first.getNext())
        self.last = other.last
        self.len += other.len
        return(self)
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
        
    def minimiun(self,spot):
        min_spot = spot
        while spot is not None:
            if spot.getItem() < min_spot.getItem():
                min_spot = spot
            spot = spot.getNext()
        return(min_spot)
    def is_sorted(self):
        spot = self.first.getNext()
        for _ in range(self.len - 1):
            if spot.getItem() > spot.getNext().getItem():
                return (False)
            spot = spot.getNext()
        return (True)

    def swap_spots(self,i,j):
        i_val = i.getItem()
        i.setItem(j.getItem())
        j.setItem(i_val)
    def swap(self,i,j):
        i_val = self[i]
        self[i] = self[j]
        self[j] = i_val
    def bubble_sort_1(self):
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

    def bubble_sort(self):
        swaps = True
        while swaps:
            swaps = False
            spot = self.first.getNext()
            while spot.getNext() is not None:
                if spot.getItem() > spot.getNext().getItem():
                    self.swap_spots(spot,spot.getNext())
                    swaps = True
                spot = spot.getNext()
                
    def merge_sort(self,check_sort=False):
        if check_sort:
            if self.is_sorted():
                return
        if self.len <= 1:
            return
        right = self.split()
        self.merge_sort(False)
        right.merge_sort(False)
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
    def sel_sort(self):
        spot = self.first.getNext()
        while not self.is_sorted():
            min_spot = self.minimiun(spot)
            self.swap_spots(min_spot,spot)
            spot = spot.getNext()
            
    def quick_sort(self):
        starting_len = self.len
        if self.len <= 1:
            return()
        spot = self.first.getNext()
        pivot = spot.getItem()
        lower = linked_list()
        higher = linked_list()
        while spot.getNext() is not None:
            spot = spot.getNext()
            if spot.getItem() < pivot:
                lower.append(spot.getItem())
            else:
                higher.append(spot.getItem())
        #order todo things 
        #quick sort sides
        #make self lower
        #merge together
        higher.quick_sort()
        lower.quick_sort()
        lower + linked_list(contents=[pivot])
        lower + higher
        self.first = lower.first
        self.last = lower.last
        self.len = lower.len
        
    def validate(self):
        spot = self.first
        for i in range(self.len):
            if spot.getNext() is None:
                raise AttributeError('len not equal to len \n too short')
            spot = spot.getNext()
        if spot.getNext() is not None:
            raise AttributeError('len not equal to len \n too long')
        if spot != self.last:
            raise AttributeError('last not equal to last')
            
def time_sort(to_sort,function):
    time = thread_time()
    function(to_sort)
    return (thread_time()- time)
    
def test_sort(file,function,shuffle_amount=25,size=200,step=1,times=5,all=True):
    for i in range(2, size+1,step):
        total_time = thread_time()
        time_list = []
        for x in range(times):
            if all:
                bad_time_list = [
                    time_sort(make_list_reverse(i),function),
                    time_sort(make_list_almost(i, shuffle_amount),function),
                    time_sort(make_list_shuffle(i),function),
                    time_sort(linked_list(list(range(i))),function)
                ]
            else:
                bad_time_list = [time_sort(make_list_reverse(i),function)]
            time_list.append(bad_time_list)
        print(i)
        good_time_list = median(time_list)
        file.write('\n')
        file.write(str(i))
        for h in good_time_list:
            file.write(',')
            file.write(str(h))
        file.flush()
        print('other stuff time ',end = "")
        print(thread_time()-total_time-sum(good_time_list)*times)
        print('total time ',end = "")
        print(thread_time()-total_time)


def make_list_almost(size, shuffle_amount):
    stuff = linked_list()
    for i in range(size):
        stuff.append(i)
    for i in range(shuffle_amount):
        stuff.swap(random.randint(0, size - 1), random.randint(0, size - 1))
    return(linked_list(stuff))


def make_list_shuffle(size):
    stuff = list(range(size))
    random.shuffle(stuff)
    return (linked_list(stuff))


def make_list_reverse(size):
    stuff = list(range(size-1, -1, -1))
    good_stuff = linked_list(stuff)
    return(linked_list(stuff))
def main():
    size = 1000
    step = 10
    do_all = False
    fun_string = "quick_sort" #does fun things 
    name = "{fun}{size:G}.csv"
    function = getattr(linked_list,fun_string)
    f = open(name.format(fun=fun_string,size=size), 'w')
    if do_all:
        f.write("number of elements,reverse,almost sorted,shuffled,sorted")
    else:
        f.write("number of elements,reverse")
    test_sort(file=f,function=function,shuffle_amount=25,size=size,step=step,times=1,all=False)
    f.close()
    
def test():
    stuff = 6000000
    l_stuff = log(stuff)
    print('10^',round(l_stuff),sep='')
print('\n'*2)
main()
#test()
