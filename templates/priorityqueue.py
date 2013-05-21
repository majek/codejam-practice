import bintrees


class PriorityQueue(object):
    def __init__(self):
        self.d = {}
        self.i = bintrees.FastAVLTree()

    def get(self, key, default=None):
        return self.d.get(key, default)

    def __setitem__(self, key, value):
        prev_v = self.d.get(key, None)
        if prev_v is not None:
            self.i[prev_v].remove( key )
            if not self.i[prev_v]:
                del self.i[prev_v]
        self.d[key] = value
        self.i.setdefault(value, set()).add( key )

    def pop(self):
        v, list_of_keys = self.i.min_item()
        key = list_of_keys.pop()
        if not list_of_keys:
            del self.i[v]
        del self.d[key]
        return key, v

    def __len__(self):
        return len(self.d)
