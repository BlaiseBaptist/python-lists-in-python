class linked_list():
  def __init__(self, contents = []):
    self.first = linked_list.__node(None)
    self.last = self.first
    self.len = 0

    for e in contents:
      self.append(e)

  class __node():
    def __init__(self,item,next=None):
      self.item = item
      self.next = next

    def getItem(self):
      return(self.item)

    def getNext(self):
      return(self.next)

    def setNext(self,next):
      self.next = next

    def setItem(self,item):
      self.item = item

  def append(self,item):
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
      s += str(i)+','
    s = s.rstrip(',') + ']'
    return(s)

  def __getitem__(self,index):
    if index >= 0 and index < self.len:
      spot = self.first.getNext()
      for _ in range(index):
        spot = spot.getNext()
      return(spot.getItem())
    raise IndexError('thats not a good spot')

  def __setitem__(self,index,val):
    if index >= 0 and index < self.len:
      spot = self.first.getNext()
      for _ in range(index):
        spot = spot.getNext()
      spot.setItem(val)
    else:
      raise IndexError('thats not a good spot')

  def __contains__(self,item):
    for i in self:
      if i == item:
        return(True)
    return(False)

  def __eq__(self,other):
    if type(self) != type(other):
      return(False)
    if self.len != other.len:
      return(False) 
    spot1 = self.first.getNext()
    spot2 = other.first.getNext()
    for _ in range(self.len):
      if spot1.getItem() != spot2.getItem():
        return(False)
      spot1 = spot1.getNext()
      spot2 = spot2.getNext()
    return(True)

  def __add__(self,other):
    if type(self) != type(other):
      raise TypeError('how would you do that')
    new_list = linked_list()
    for i in self:
      new_list.append(i)
    for e in other:
      new_list.append(e)
    return(new_list)

  def insert(self,item,index):
    if index > self.len:
      raise IndexError('out of range')
    spot = self.first.getNext()
    for _ in range(index):
      spot = spot.getNext()
    new_node = linked_list.__node(item,spot.getNext())
    spot.setNext(new_node)
    self.len += 1

  def __delitem__(self,index):
    if index > self.len:
      raise IndexError('out of range')
    spot = self.first
    for _ in range(index):
      spot = spot.getNext()
    spot.setNext(spot.getNext().getNext())
    self.len -= 1

  def __len__(self):
    return(self.len)

  def is_sorted(self):
    spot=self.first.getNext()
    for _ in range(self.len-1):
      if spot.getItem() > spot.getNext().getItem():
        return(False)
      spot = spot.getNext()
    return(True)
    
def main():
  link_list = linked_list(range(100))
  link_list2 = linked_list(range(100))
  link_list.insert(10,1)
  print(link_list)
  print(link_list.is_sorted())


main()