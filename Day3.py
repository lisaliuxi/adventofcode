def cal_via_mul(matches):
    val = 0
    for x, y in matches:
        val += float(x)*float(y)
    
    return val

# task 1
matches = re.findall(r"mul\((\d+),(\d+)\)", memory)
print(cal_via_mul(matches))

# task 2
do_dont_list = re.findall(r"do\(\)|don't\(\)", memory) #find all do() and dont()

before_sections = after_sections = ''

before_sections = re.findall(r"(.*?)" + re.escape(do_dont_list[0]), memory, re.DOTALL)[0] # extract before the first do() or dont()
if do_dont_list[-1] == "do()":
    after_sections = re.findall(r"do\(\)(.*?)(?=do\(\)|$)", memory, re.DOTALL)[-1]

do_dont_sections = re.findall(r"do\(\)(.*?)don't\(\)", memory, re.DOTALL) # extract between each pair of do() and donts()
do_dont_sections.extend([before_sections, after_sections])

matches = []
for section in do_dont_sections:
    matches.extend(re.findall(r"mul\((\d+),(\d+)\)", section))

print(cal_via_mul(matches))
