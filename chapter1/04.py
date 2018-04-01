s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
d = {}
for i,j in enumerate(s.split()):
    if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        d[i+1] = j[0]
    else:
        d[i+1] = j[0:2]
print(d)
