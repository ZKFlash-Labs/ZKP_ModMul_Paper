import re


fh = open("work_dir/vivado.log", "r+")

text = fh.read()

fh.close

regx = "\|\s*(\d)\s*\|\s*(u0)\s*\|\s*(\w*)\s*\|\s*(\d*)\s*\|"

x = re.search(regx, text)

# print(x.group(1))
# print(x.group(2))
# print(x.group(3))
# print(x.group(4))
print(f"DESIGN AREA: {x.group(4)} cells")
