import matplotlib.pyplot as plt

N_SEQUENCES = 10

value = 1

# size = sum([2 * l for l in range(1, N_SEQUENCES + 1)])
size = 1000
x = [0] * size
y = [0] * size

length = 1
idx = 0
while length <= N_SEQUENCES:
    for i in range(length):
        x[idx] = value
        idx += 1
    for i in range(length):
        y[idx] = value
        idx += 1
    value *= -1
    length += 1

summed_vals_x = [0] * 1000
summed_vals_y = [0] * 1000
for i in range(len(x)):
    summed_vals_x[i] = sum(x[:i])
    summed_vals_y[i] = sum(y[:i])

fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect('equal', adjustable='box')
plt.plot(summed_vals_x[:idx], summed_vals_y[:idx])
plt.show()
