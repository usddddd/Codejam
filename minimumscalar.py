infile = open('a2','r')
outfile = open('google2.txt', 'w')
count = 1
cases = infile.readlines()[1:]
for i in range(1, len(cases), 3):
    sum = 0
    v1_old = cases[i].split()
    v2_old = cases[i + 1].split()
    v1 = []
    v2 = []
    for i in range(len(v1_old)):
        v1.append(int(v1_old[i]))
        v2.append(int(v2_old[i]))
    
    v1.sort()
    v2.sort()
    
    for i in range(len(v1)):
        sum += v1[i] * v2[-1 -i]
    print sum
    outfile.write(("Case #%i: " % count) + str(sum) + "\n") 
    count += 1
