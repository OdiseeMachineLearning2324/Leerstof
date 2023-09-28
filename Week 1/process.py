
output = "["
with open('data.txt') as fp:
    lines = fp.readlines()
    
    for index, line in enumerate(lines):
        cols = line.strip().split(" ", 1)
        #print(cols[1])
        output += "'" + cols[1] + "',"
        
output = list(output)
output[-1] = "]"
output = "".join(output)

print(output)


with open('data_processed.txt', "w") as fp:
    fp.write(output)