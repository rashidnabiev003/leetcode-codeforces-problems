sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
max_len = 0

for i in sentences:
    max_len = max(max_len, len(list(map(str, i.split()))))

print(max_len)