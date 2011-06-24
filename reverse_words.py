cases = open('B-large-practice.in', 'r').readlines()
outfile = open('google.txt', 'w')
count = 1
for line in cases[1:]:
    outfile.write("Case #" + str(count)+ ": ")
    count += 1
    for word in line.split()[::-1]:
        outfile.write(word + " ",)
    outfile.write("\n")
outfile.close()


