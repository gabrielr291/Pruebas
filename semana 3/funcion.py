fhad = open('test.txt')
for line in fhad:
    line = line.rstrip()
    if not '@gmail.com' in line:
        continue
    print(line)
