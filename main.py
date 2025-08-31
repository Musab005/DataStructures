from src.lists.list import List


def main():
    fruits = List()
    fruits.append('orange')
    fruits.append('apple')
    fruits.append('pear')
    fruits.append('banana')
    fruits.append('kiwi')
    fruits.append('apple')
    fruits.append('banana')
    print(fruits.count('apple'))  # 2
    print(fruits.count('tangerine'))  # 0
    print(fruits.index('banana'))  # 3
    print(fruits.index('banana', 4))  # 6
    fruits.reverse()
    print(fruits)  # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
    fruits.append('grape')
    print(fruits)  # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
    print(fruits.pop())  # 'grape'


if __name__ == "__main__":
    main()
