with open('goats.txt') as f, open('answer.txt', 'w') as g:
    t = f.readline()
    my_dict = {}
    while True:
        s = (f.readline()).strip()
        if s == 'GOATS':
            break
        my_dict[s] = 0
    c = 0
    for i in f:
        i = i.strip()
        my_dict[i] += 1
        c += 1
    k = []
    for i in sorted(my_dict):
        if my_dict[i]/c >= 0.07:
            k.append(i+'\n')
    g.writelines(k)