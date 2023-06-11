def make_queue():
    return []

def enqueue(q, item):
    q.append(item)
    return

def dequeue(q):
    if q == []:
        return None
    else:
        return q.pop(0)

def size(q):
    return len(q)

def below_4(p1,p2):
    if age(p1) < 4 and age(p2) >= 4:
        return True
    else:
        return False

def priority_enqueue(q, fn, p):
    position_reached = False
    counter = len(q) + 1
    while not position_reached:
        if fn(p, q[counter - 1]):
            position_reached = True
        else:
            counter += -1
    q.insert(counter, p)
    return


def valid_heap(node):
    if node.value == None:
        return True
    if node.parent != None and node.value > node.parent.value:
        return False
    else:
        left =  valid_heap(node.left)
        right =  valid_heap(node.right)
    if left and right:
        return True