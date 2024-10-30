# Linked Lists
## Description
Code that defines a custom list class (linked lists) and implements four sorting algorithms; then records their runtimes when sorting lists with increasing number of elements.
## Data Structure
List of nodes
https://github.com/BlaiseBaptist/python-lists-in-python/blob/56f69acb4e32dd789924055915159e869c0ba158/main.py#L7-L9
### Nodes
Nodes have a item in them and point to another node
https://github.com/BlaiseBaptist/python-lists-in-python/blob/56f69acb4e32dd789924055915159e869c0ba158/main.py#L15-L18
## Sorting Algorithms
||Bubble|Selection|Merge|Quick
|:--|:--|:--|:--|:--
|Time Complexity|O(n<sup>2</sup>)|O(n<sup>2</sup>)|O(n log n)|O(n log n)
### Bubble
Compares pairs of elements and swaps them if they are out of order.
### Selection
Takes the smallest element of the main list and adds it to a sub-list until it get to the end of the list.
### Merge
Splits the list into elements, then merges pairs of sub-lists keeping, the elements in order until it is one list again.
### Quick
Selects a pivot and moves all smaller elements to one side of the list then does the same to each side of the list.
