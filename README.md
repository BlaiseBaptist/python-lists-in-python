
# Linked Lists
## Data Structure
### Nodes
Nodes have a number in them and point to another node
```
class linked_list():
    def __init__(self, contents=[], first=None):
        self.first = linked_list.__node(None,first)
        self.last = self.first
        self.len = 0
        for e in contents:
            self.append(e)
```

## Sorting Algorithms
### Bubble
  O(n<sup>2</sup>) time complexity for both
### Selection and Insertion
also O(n<sup>2</sup>) time complexity for both
### Merge and Quick
O(n log n) time complexity for both
