data = [5, 1, 3, 7, 9, 8, 10]
print("Data awal:", data)
d = 1
n = len(data) - 1

while d <= n:
    print("d:", d)
    titip = data[d]
    c = d

    while c >= 1 and data[c - 1] > titip:
        print("\tC-->", c, "&", data[c])
        print("\t[C-1]-->", c - 1, "&", data[c - 1])
        print("\ttitip:", titip)
        data[c] = data[c - 1]
        c -= 1

    data[c] = titip
    print("D-->", d, "&", data[d])
    d += 1

print("Bilangan setelah diurutkan dengan Insertion Sort adalah:", data)
