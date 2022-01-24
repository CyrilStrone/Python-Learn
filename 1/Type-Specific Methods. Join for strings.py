s = "".join(["a","b","c"])
print(s)

s = "_".join(["hello"])
print(s)

s = "_".join(['a','b','c']).split("_")
print(s)

s = "_".join('a_b_c'.split("_"))
print(s)

lines = []
for i in range(5):
    lines.append(str(i))
print(lines)
print("\n".join(lines))