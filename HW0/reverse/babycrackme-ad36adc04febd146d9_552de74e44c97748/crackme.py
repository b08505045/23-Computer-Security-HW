from Crypto.Util.number import bytes_to_long, long_to_bytes
s1 = ''
a2 = 36
a3 = 3134107660
v5 = v8 = v9 = v10 = v11 = 0
v12 = 12616
l_8 = 255
byte_2020 = [74, 60, 102, 208, 199, 75, 198, 183, 27, 13, 192, 86, 184, 215, 211, 71, 180, 230, 103, 14, 182, 80, 146, 140, 34, 92, 99, 139, 7, 9, 246, 241, 100, 138, 139, 242, 0, 0, 0, 0]

for i in range(a2):
    v5 = byte_2020[i]
    s1 += long_to_bytes((a3 & l_8) ^ byte_2020[i]).decode()
    # a3 = a2 - i + (v5 ^ (a3 >> 1))
    a3 = a2 - i + (v5 ^ (a3 >> 1) | ((a3 & 1) << 31))

print(s1)
print(len(s1))