from src.lists.list import List


def main():
    list_test = [] * 10
    list_test.append(7)
    list_test.insert(2, 1)
    print(list_test)


if __name__ == "__main__":
    main()
