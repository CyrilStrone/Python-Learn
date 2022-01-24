def add(n):
    def do_add(m):
        return m+n
    return do_add

sum = add(2)
print(sum)
result = sum(20)
print(result)