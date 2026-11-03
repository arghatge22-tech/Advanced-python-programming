import gc
import tracemalloc

class Node:
    def __init__(self):
        self.ref = None
        self.data = [0] * 1000

def create_objects():
    for _ in range(1000):
        a = Node()
        b = Node()
        a.ref = b
        b.ref = a

def show_memory(label):
    current, peak = tracemalloc.get_traced_memory()
    print(label, ":", round(current / 1024, 2), "KB")

tracemalloc.start()
gc.disable()
show_memory("Initial memory usage")
create_objects()
show_memory("Memory after creating objects")
gc.set_debug(gc.DEBUG_STATS)
collected = gc.collect()
gc.set_debug(0)
print("Garbage collector: collected", collected, "objects")
show_memory("Memory after garbage collection")
