class UnionFind:

    def __init__(self, k):
        self.len = k
        self.size = [0] * k

        # index in id array has the index of the element's root
        self.id = []
        for i in range(k):
            self.id.append(i)

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def merge(self, p, q):

        # find the size of each tree and make the smaller tree a child of the larger tree
        px = self.root(p)
        qx = self.root(q)

        if px == qx:
            return

        if self.size[px] < self.size[qx]:
            self.id[px] = qx
            self.size[qx] += self.size[px]
        else:
            self.id[qx] = px
            self.size[px] += self.size[qx]

    """
    This is a two pass variant.
    You first find out the root in the first loop
    Then you traverse each node and reset the parent to the root in the second loop.
   
    def root(self, i):

        # 2 pass variant
        # find the root first
        x = i
        while i != self.id[i]:
            i = self.id[i]
        # variable i is now the root

        # reset the root value in all nodes
        while x != i:
            # get the root value
            parent = self.id[x]
            self.id[x] = i
            x = parent
            
    """

    """
    this is a one pass variant
    This is much simpler, the tree height is reduced by half at the end.
    Each parent is pointed to it's grandparent
    
    def root(self, i):
        
        # 1 pass variant
        
        while i != self.id[i]:
            id[i] = id[id[i]]
            i = id[i]
        return i

    """


    def root(self, i):
        if i == self.id[i]:
            return i
        self.id[i] = self.root(self.id[i])
        return self.id[i]


