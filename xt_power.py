import re


fh = open("work_dir/post_synth_power.rpt", "r+")

text = fh.read()

fh.close

regx = "\|\s*(u0)\s*\|\s*([\d.]*)\s*\|"

x = re.search(regx, text)

# print(x.group(1))
# print(x.group(2))

print(f"DESIGN POWER: {x.group(2)} watt")
