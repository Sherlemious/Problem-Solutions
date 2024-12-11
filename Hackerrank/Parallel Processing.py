def minTime(files, numCores, limit):
    time = 0
    files.sort(reverse=True)
    while limit > 0:

        try:
            m = files[0]
        except:
            break

        if m % numCores == 0:
            time += (m//numCores)
            limit -= 1
        else:
            time += m
        del files[files.index(m)]

    for num in files:
        time += num

    return time
