class stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def pop_n(self, n):
    return [self.items.pop() for _ in range(0, n)]
    # return self.items.pop()

  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)
  
  def clear_contents(self):
    self.items.clear()

  def is_empty(self):
    return (self.size == 0)
