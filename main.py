import matplotlib.pyplot as plt

# Top left diagonal is even squares
# Bottom right diagonal is odd squares -1
#

N_SEQUENCES = 10

value = 1

# size = sum([2 * l for l in range(1, N_SEQUENCES + 1)])
x = [0]
y = [0]


for length in range(1, N_SEQUENCES+1):
    for i in range(length):
        x.append(value)
    for i in range(length):
        y.append(value)
    value *= -1

summed_vals_x = []
summed_vals_y = []
for i in range(len(x)):
    summed_vals_x.append(sum(x[:i]))
    summed_vals_y.append(sum(y[:i]))

fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect('equal', adjustable='box')
plt.plot(summed_vals_x, summed_vals_y)
plt.show()
