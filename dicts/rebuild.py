with open('1.txt', 'r') as f:
    anss = {}
    for line in f.readlines():
        if '. ' in line:
            ind = line.index('. ')
            
            n, ans = line[:ind], line[ind:]
            anss[n] = ans

print(anss)
