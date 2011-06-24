infile= open('numbers.txt', 'r')
outfile = open('google.txt', 'w')

cases = infile.readlines()
num_cases = int(cases[0])
cases= cases[1:]
count = 1
for i in range(num_cases):
    total = 0
    total = (3 + 5 ** 0.5) ** int(cases[i])
    answer = int(total) % 1000
    if len(str(answer)) < 3:
        answer = "0" + str(answer)
    print total, answer
    outfile.write("Case #%i: %s\n" % (count, str(answer)))
    count += 1

    # off by one handling of floats is wrong
