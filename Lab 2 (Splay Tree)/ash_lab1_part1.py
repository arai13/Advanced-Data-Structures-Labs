"""
Ash Rai
CS 335, Lab 1: Part 1
ash_lab1_part1.py
"""

from maps import MapBase
from trees import LinkedBinaryTree

class TreeMap(LinkedBinaryTree, MapBase):
  
  class Position(LinkedBinaryTree.Position):
    def key(self):
      return self.element()._key

    def value(self):
      return self.element()._value

  def _subtree_search(self, p, k):
    if k == p.key():                                   # found match
      return p                                         
    elif k < p.key():                                  # search left subtree
      if self.left(p) is not None:
        return self._subtree_search(self.left(p), k)   
    else:                                              # search right subtree
      if self.right(p) is not None:
        return self._subtree_search(self.right(p), k)
    return p                                           # unsucessful search

  def _subtree_first_position(self, p):
    walk = p
    while self.left(walk) is not None:                 # keep walking left
      walk = self.left(walk)
    return walk

  def _subtree_last_position(self, p):
    walk = p
    while self.right(walk) is not None:                # keep walking right
      walk = self.right(walk)
    return walk
  
  def first(self):
    return self._subtree_first_position(self.root()) if len(self) > 0 else None

  def last(self):
    return self._subtree_last_position(self.root()) if len(self) > 0 else None

  def before(self, p):
    self._validate(p)                            # inherited from LinkedBinaryTree
    if self.left(p):
      return self._subtree_last_position(self.left(p))
    else:
      walk = p
      above = self.parent(walk)
      while above is not None and walk == self.left(above):
        walk = above
        above = self.parent(walk)
      return above

  def after(self, p):
    self._validate(p)                            # inherited from LinkedBinaryTree
    if self.right(p):
      return self._subtree_first_position(self.right(p))
    else:
      walk = p
      above = self.parent(walk)
      while above is not None and walk == self.right(above):
        walk = above
        above = self.parent(walk)
      return above

  def find_position(self, k):
    if self.is_empty():
      return None
    else:
      p = self._subtree_search(self.root(), k)
      self._rebalance_access(p)                  # hook for balanced tree subclasses
      return p

  def delete(self, p):
    self._validate(p)                            # inherited from LinkedBinaryTree
    if self.left(p) and self.right(p):           # p has two children
      replacement = self._subtree_last_position(self.left(p))
      self._replace(p, replacement.element())    # from LinkedBinaryTree
      p =  replacement
    parent = self.parent(p)
    self._delete(p)                              # inherited from LinkedBinaryTree
    self._rebalance_delete(parent)               # if root deleted, parent is None
      

  def __getitem__(self, k):
    if self.is_empty():
      raise KeyError('Key Error: ' + repr(k))
    else:
      p = self._subtree_search(self.root(), k)
      self._rebalance_access(p)                  # hook for balanced tree subclasses
      if k != p.key():
        raise KeyError('Key Error: ' + repr(k))
      return p.value()

  def __setitem__(self, k, v):
    if self.is_empty():
      leaf = self._add_root(self._Item(k,v))     # from LinkedBinaryTree
    else:
      p = self._subtree_search(self.root(), k)
      if p.key() == k:
        p.element()._value = v                   # replace existing item's value
        self._rebalance_access(p)                # hook for balanced tree subclasses
        return
      else:
        item = self._Item(k,v)
        if p.key() < k:
          leaf = self._add_right(p, item)        # inherited from LinkedBinaryTree
        else:
          leaf = self._add_left(p, item)         # inherited from LinkedBinaryTree
    self._rebalance_insert(leaf)                 # hook for balanced tree subclasses

  def __delitem__(self, k):
    if not self.is_empty():
      p = self._subtree_search(self.root(), k)
      if k == p.key():
        self.delete(p)                           # rely on positional version
        return                                   # successful deletion complete
      self._rebalance_access(p)                  # hook for balanced tree subclasses
    raise KeyError('Key Error: ' + repr(k))

  def __iter__(self):
    p = self.first()
    while p is not None:
      yield p.key()
      p = self.after(p)

  def __reversed__(self):
    p = self.last()
    while p is not None:
      yield p.key()
      p = self.before(p)

  def find_min(self):
    if self.is_empty():
      return None
    else:
      p = self.first()
      return (p.key(), p.value())

  def find_max(self):
    if self.is_empty():
      return None
    else:
      p = self.last()
      return (p.key(), p.value())

  def find_le(self, k):
    if self.is_empty():
      return None
    else:
      p = self.find_position(k)
      if k < p.key():
        p = self.before(p)
      return (p.key(), p.value()) if p is not None else None

  def find_lt(self, k):
    if self.is_empty():
      return None
    else:
      p = self.find_position(k)
      if not p.key() < k:
        p = self.before(p)
      return (p.key(), p.value()) if p is not None else None

  def find_ge(self, k):
    if self.is_empty():
      return None
    else:
      p = self.find_position(k)                   # may not find exact match
      if p.key() < k:                             # p's key is too small
        p = self.after(p)
      return (p.key(), p.value()) if p is not None else None

  def find_gt(self, k):
    if self.is_empty():
      return None
    else:
      p = self.find_position(k)
      if not k < p.key():                   
        p = self.after(p)
      return (p.key(), p.value()) if p is not None else None
  
  def find_range(self, start, stop):
    if not self.is_empty():
      if start is None:
        p = self.first()
      else:
        p = self.find_position(start)
        if p.key() < start:
          p = self.after(p)
      while p is not None and (stop is None or p.key() < stop):
        yield (p.key(), p.value())
        p = self.after(p)

  def _rebalance_insert(self, p):
    pass

  def _rebalance_delete(self, p):
    pass

  def _rebalance_access(self, p):
    pass

  def _relink(self, parent, child, make_left_child):
    if make_left_child:                           # make it a left child
      parent._left = child
    else:                                         # make it a right child
      parent._right = child
    if child is not None:                         # make child point to parent
      child._parent = parent

  def _rotate(self, p):
    x = p._node
    y = x._parent                                 # we assume this exists
    z = y._parent                                 # grandparent (possibly None)
    if z is None:            
      self._root = x                              # x becomes root
      x._parent = None        
    else:
      self._relink(z, x, y == z._left)            # x becomes a direct child of z
    if x == y._left:
      self._relink(y, x._right, True)             # x._right becomes left child of y
      self._relink(x, y, False)                   # y becomes right child of x
    else:
      self._relink(y, x._left, False)             # x._left becomes right child of y
      self._relink(x, y, True)                    # y becomes left child of x

  def _restructure(self, x):
    y = self.parent(x)
    z = self.parent(y)
    if (x == self.right(y)) == (y == self.right(z)):  # matching alignments
      self._rotate(y)                                 # single rotation (of y)
      return y                                        # y is new subtree root
    else:                                             # opposite alignments
      self._rotate(x)                                 # double rotation (of x)     
      self._rotate(x)
      return x                                        # x is new subtree root