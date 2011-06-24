infile = open('C-large-practice.in', 'r')
outfile = open('google.txt', 'w')
messages = infile.readlines()

mapped_keys = { 'a':'2', 'b' :'22', 'c' : '222',
                'd' : '3', 'e' : '33', 'f' : '333',
                'g' : '4', 'h' :'44', 'i':'444','j': '5', 
                'k':'55', 'l' :'555', 'm': '6', 'n': '66', 'o' :'666',
                'p' : '7', 'q' : '77', 'r': '777', 's' : '7777', 't' : '8',
                'u' : '88', 'v' : '888', 'w': '9', 'x' : '99', 'y': '999',
                'z' : '9999', ' ': '0'}
count = 1
char_prev = ' '
for message in messages[1:]:
    outfile.write("Case #%i: " % count),
    for char in message:
        if char == "\n": 
            outfile.write("\n")
            break 
        elif mapped_keys[char][0] == mapped_keys[char_prev][0]:
            outfile.write(" " + mapped_keys[char],)
        else:    outfile.write(mapped_keys[char],)
        char_prev = char
    count += 1

