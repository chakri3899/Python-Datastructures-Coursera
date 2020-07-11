name = input("Enter file:")
handle = open(name)

lst = list()
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    mail = words[1]
    lst.append(mail)


counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1


bigkey = None
bigvalue = None
for k,v in counts.items():
    if bigvalue is None or v > bigvalue:
        bigkey = k
        bigvalue = v
print(bigkey,bigvalue)
