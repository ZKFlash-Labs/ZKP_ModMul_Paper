import re


fh = open("work_dir/post_synth_util.rpt", "r+")

text = fh.read()

fh.close

regx = "(Slice LUTs)[\*\s]*\|\s*(\d*)[\s\S]*(Slice Registers)\s*\|\s*(\d*)[\s\S]*(Block RAM Tile)\s*\|\s*(\d*)[\s\S]*(DSPs)\s*\|\s*(\d*)"

x = re.search(regx, text)

# print(x.group(1))
# print(x.group(2))
# print(x.group(3))
# print(x.group(4))
print(f"DESIGN UTIL:- ")
print(f"    LUTs: {x.group(2)}    Registers: {x.group(4)}   BRAMs: {x.group(6)}   DSPs: {x.group(8)}")
