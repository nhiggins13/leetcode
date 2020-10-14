def partitionLabels(S):
    lengths = []
    intervals = {}

    for i, letter in enumerate(S):
        if letter in intervals:
            intervals[letter][1] = i
        else:
            intervals[letter] = [i, i]

    mx = 0
    mn = 0

    for k, interval in intervals.items():

        if interval[0] <= mx:
            mx = max(mx, interval[1])
        else:
            lengths.append(mx - mn + 1)
            mn, mx = interval

    lengths.append(mx - mn + 1)

    return lengths