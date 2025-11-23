from src.maps import map


def main():
    map1 = map.Map()
    map1['A'] = 7
    map1['B'] = 8
    map1['C'] = 9
    print(map1)
    # print(math.ceil(6 / -132)) - TODO: google doc


if __name__ == "__main__":
    main()
