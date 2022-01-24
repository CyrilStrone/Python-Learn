line_list = ['line 1\n', 'line 2\n',...]

# Generator expression -- returns iterator
splitted_iter = (line.split(\n) for line in line_list)
# List comprehension -- returns 
splitted_list = [line.split(\n) for line in line_list]


for x in range(5, 10):
    if x % 2 == 0:
        x *=2
    else:
        x += 1
a = [x * 2 if x % 2 == 0 else x + 1 for x in range(5, 10)]
print(a)