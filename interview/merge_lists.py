

def merge_lists(first: list, second: list) -> list:
    k=0
    l=0
    result = []

    first.sort()
    second.sort()

    if len(first) == 0:
        return second

    if len(second) == 0:
        return first

    while True:

        if k == len(first) and  l == len(second):
            break

        if l==len(second) or first[k] <= second[l]:
            result.append(first[k])
            k = k+1

        else:
            result.append(second[l])
            l = l+1

    return result


if __name__ == '__main__':

    a = [1,2,32,434]
    b = [1,4,6,2, 3]

    print(merge_lists(a,b))
