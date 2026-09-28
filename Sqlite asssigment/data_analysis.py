def calc_average(l):
    return sum(l)/len(l)

def calc_median(l):
    l.sort()
    n = len(l)

    if n % 2 == 1:
        return l[n // 2]
    else:
        middle_right=l[n//2]
        middle_left=l[(n//2)-1]
        return (middle_left+middle_right)/2

def calc_mode(l):
    frequencies = {}
    for num in l:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1

    highest_count = 0
    mode = None

    for num in frequencies:
        count = frequencies[num]
        if count > highest_count:
            highest_count = count
            mode = num

    return mode


def calc_frequency(l):
    
    frequencies = {}

    for i in l:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1

    return frequencies


def calc_range(l):
    return max(l)-min(l)