infile = open('A-large-practice.in', 'r')
outfile = open('google.txt', 'w')

cases = infile.readlines()
num_cases = cases[0]
cases = cases[1:]
count = 1
for i in range(0, len(cases), 3):
    cred = cases[i]
    num_items = cases[i + 1]
    items = cases[i + 2].split()
    for j in range(len(items)):
        for k in range(j + 1, len(items)):
            if int(items[j]) + int(items[k]) == int(cred):
                if j < k:
                    # indices for this test are output beginning at 1 
                    outfile.write("Case #" + str(count) + ": %i %i" % (j + 1, k + 1) + "\n")
                else:
                    outfile.write("Case #" + str(count) + ": %i %i" % (k + 1, j + 1) + "\n")
                break
    count += 1
            
            



