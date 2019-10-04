try:
    global_case = 1
    while True and global_case < 6:
        # Get Input
        k = int(input())
        temp = []
        a = []
        b = []
        for case in range(k):
            temp.extend(input().split())
            a.append(temp[0])
            b.append(temp[1])
            temp.clear()

        # print(a)
        # print(b)
        # Determining possible first indexes
        starting = []

        for case in range(k):
            if a[case].startswith(b[case]) or b[case].startswith(a[case]):
                starting.append(case)

        # print(starting)
        message = [ ]
        for start in range(len(starting)):
            message.append(['', ''])
        # print(message)
        truepositive_end = []
        # Building sequences
        for i, starr in enumerate(starting, start=0):
            ac = a.copy()
            bc = b.copy()

            message[i][0] = ac[starr]
            message[i][1] = bc[starr]

            ac.remove(ac[starr])
            bc.remove(bc[starr])

            case = 0
            while message[i][0] != message[i][1] and case < k * k:
                temp_message = [message[i][0], message[i][1]]
                # print(temp_message)
                temp_message[0] = temp_message[0] + (ac[case % (len(ac))])
                temp_message[1] = temp_message[1] + (bc[case % (len(bc))])
                if temp_message[0].startswith(temp_message[1]) or temp_message[1].startswith(temp_message[0]):
                    message[i][0] = temp_message[0]
                    message[i][1] = temp_message[1]
                    ac.remove(ac[case % (len(ac))])
                    bc.remove(bc[case % (len(bc))])
                    # starting.append([case])
                # print(temp_message)
                temp_message.clear()
                case += 1
            ac.clear()
            bc.clear()

            truepositive = True
            for rep in range(len(a)):
                if message[i][0] == a[rep]:
                    truepositive = False
            if message[i][0] != message[i][1]:
                truepositive = False

            if truepositive:
                truepositive_end.append(True)
            else:
                truepositive_end.append(False)

        fail = True
        for i, starr in enumerate(starting, start=0):
            if truepositive_end[i]:
                fail = False
        # Determining final message
        if fail:
            print(f'Case {global_case}: IMPOSSIBLE')
        elif len(message) > 0 :
            min = 100000000
            imin = 10
            for i, starr in enumerate(starting, start=0):
                if len(message[i][0]) < min and truepositive_end[i]:
                    min = len(message[i][0])
                    imin = i
            print(f'Case {global_case}: {message[imin][0]}')

        global_case += 1
except EOFError:
    pass
