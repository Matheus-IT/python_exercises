class SortedList(list):
    def add(self, el):
        i = 0

        while i < len(self):
            if self[i] > el:
                break
            i += 1
        self.insert(i, el)


def main():
    sl = SortedList()
    sl.add(10)
    sl.add(15)
    sl.add(5)
    sl.add(11)


if __name__ == "__main__":
    main()
