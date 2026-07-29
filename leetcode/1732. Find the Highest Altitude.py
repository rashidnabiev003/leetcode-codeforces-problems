gain = [-4,-3,-2,-1,4,3,2]
prefix_sum = [0]

for i in range(len(gain)):
    prefix_sum.append(prefix_sum[i] + gain[i])

print(max(prefix_sum))
