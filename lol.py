def make_queue():
    return []

def enqueue(q, item):
    q.append(item)
    return

def dequeue(q):
    if q == []:
        return None
    else:
        