#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
fname = input("Enter file name: ")
fh = open(fname)
count = 0
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    a = float(line[20:])
    add = add + a
avg = add/count
print("Average spam confidence:",avg)
