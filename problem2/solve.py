def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    x = [str(l).rstrip() for l in lines]
    return x

def find_res(x):
    min = int(x.split(": ")[0].split(" ")[0].split("-")[0])
    max = int(x.split(": ")[0].split(" ")[0].split("-")[1])
    val = x.split(": ")[0][-1]
    pas = x.split(": ")[1]
    return pas.count(val) >= min and pas.count(val) <= max

def find_res2(x):
    min = int(x.split(": ")[0].split(" ")[0].split("-")[0])
    max = int(x.split(": ")[0].split(" ")[0].split("-")[1])
    val = x.split(": ")[0][-1]
    pas = x.split(": ")[1]
    return (pas[min-1] == val or pas[max-1] == val) and not (pas[min-1] == val and pas[max-1] == val)

if __name__ == "__main__":
    passwords = read_input('input.txt')
    
    # Part 1
    res = [find_res(x) for x in passwords if find_res(x)]
    print(len(res))

    # Part 2
    res = [find_res2(x) for x in passwords if find_res2(x)]
    print(len(res))