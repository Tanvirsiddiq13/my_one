a = int(input())
for i in range(0,a):
    B = int(input())
    clube = list(map(int,input().split()))
    status = "Yes"
    pile = []

    while len(clube) > 0:
        first = clube[0]
        last = clube[-1]

        if first >= last :
            if len(pile) > 0 and pile[-1] < first:
                status = "No"
                break
            else:
                pile.append(first)
                del(clube[-1])
        else:
            if len(pile) > 0 and pile[-1] < last:
                status = "No"
                break
            else:
                pile.append(last)
                del(clube[-1])
    print(status)