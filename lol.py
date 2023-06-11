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
    if a