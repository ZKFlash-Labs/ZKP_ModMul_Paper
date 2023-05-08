import re


fh = open("work_dir/post_synth_timing_summary.rpt", "r+")

text = fh.read()

fh.close

regx = "(Max Delay)[\s\S]*?\s*(slack)\s*([-\d.]*)"

x = re.search(regx, text)

# print(x.group(1))
# print(x.group(2))
# print(x.group(3))
clk_period = 1.0

print(f"DESIGN SLACK: {x.group(3)} ns")
print(f"DESIGN FMAX: {10**9 * 10**(-6) / (clk_period - float(x.group(3)))} MHz")
