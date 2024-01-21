def flip_out(line1):
    line2 = ""
    count = len(line1) - 1
    while count >= 0:
        line2 = line2 + line1[count]
        count = count - 1
    line2 = list(line2)
    print(line2)
 
def cut_out(line2):
    line2 = list(line2)
    num = 0
    for i in range(len(line2) - 1):
        one = line2[num]
        line2[num] = line2[1]
        line2[1] = one
        num = num + 1
    line2 = " ".join(line2)
    print(line2)