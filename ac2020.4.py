with open("ac2020.4.txt") as f:
    txt = f.read()
    ans = []
    for pp in txt.split("\n\n"):
        obj = []
        for item in pp.split():
            key, val = item.split(":")
            if key == "byr":
                obj.append(1920 <= int(val) <= 2002)
            if key == "iyr":
                obj.append(2010 <= int(val) <= 2020)
            if key == "eyr":
                obj.append(2020 <= int(val) <= 2030)
            if key == "hgt":
                unit = val.lstrip("0123456789")
                num = val[:(len(val) - len(unit))]
                if unit == "cm":
                    obj.append(150 <= int(num) <= 193)
                elif unit == "in":
                    obj.append(59 <= int(num) <= 76)
                else:
                    obj.append(False)
            if key == "hcl":
                obj.append(val[0] == "#" and all((_ in "0123456789abcdef" for _ in val[1:])) and len(val) == 7)
            if key == "ecl":
                obj.append(val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
            if key == "pid":
                obj.append(all((_ in "0123456789" for _ in val)) and len(val) == 9)
        ans.append(obj)
        
def p1():
    return sum([len(a) == 7 for a in ans])
    
def p2():
    return sum([len(a) == 7 and all(a) for a in ans])

print(p1())
print(p2())
