def build_heap(data):
    n = len(data)
    swaps = []

    def sift_down(i):
        nonlocal swaps
        min_index = i
        left = 2 * i + 1
        if left < n and data[left] < data[min_index]:
            min_index = left
        right = 2 * i + 2
        if right < n and data[right] < data[min_index]:
            min_index = right
        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)

    for i in range(n // 2, -1, -1):
        sift_down(i)
    assert len(swaps) <= 4 * len(data)
    return swaps


def main():
    print("Enter Input type:")
    input_type = input().strip()
    if "I" in input_type:
        print("Enter data:")
        n = int(input().strip())
        data = list(map(int, input().strip().split()))
    else:
        filename = input("Enter filename: ").strip()
        folder = './tests/'
        with open(folder + filename, 'r') as test:
            n = int(test.readline().strip())
            data = list(map(int, test.readline().strip().split()))
    assert len(data) == n
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
