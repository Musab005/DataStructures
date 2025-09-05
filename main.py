from src.lists.list import List


def main():
    list1 = List()
    list1.append(0)
    list1.append(4)
    list1.append(5)
    list1.append(9)
    list2 = List()
    list2.append(1)
    list2.append(3)
    list2.append(10)
    list2.append(40)
    list1.merge(list1, list2)


if __name__ == "__main__":
    main()
