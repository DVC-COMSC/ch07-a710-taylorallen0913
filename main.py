import matplotlib.pyplot as plt

data1 = [100, 90, 80, 60]
data2 = [90, 80, 70, 100]
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

fig, ax = plt.subplots()

ax.bar(labels, data1, 0.8, label='Bill')
ax.bar(labels, data2, 0.8, label='Mary')
ax.set_title("Stacked graph for scores")
ax.legend()

fig.savefig('A10.png')
