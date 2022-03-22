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
    
def main():
  link_list = linked_list(range(100))
  print(link_list)
  print(link_list[3])
  link_list[99] = 100
  print(link_list)

main()