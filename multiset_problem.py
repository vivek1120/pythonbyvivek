class Multiset:
    def __init__(self):
        self.elements = {}

    def add(self, val):
        if val in self.elements:
            self.elements[val] += 1
        else:
            self.elements[val] = 1

    def remove(self, val):
        if val in self.elements:
            if self.elements[val] > 1:
                self.elements[val] -= 1
            else:
                del self.elements[val]

    def __contains__(self, val):
        return val in self.elements

    def __len__(self):
        return sum(self.elements.values())

if __name__ == '__main__':
    multiset = Multiset()

    multiset.add(5)
    multiset.add(5)
    multiset.add(3)

    print(5 in multiset)  # Output: True
    print(2 in multiset)  # Output: False

    multiset.remove(5)

    print(5 in multiset)  # Output: True
    print(len(multiset))   # Output: 2
