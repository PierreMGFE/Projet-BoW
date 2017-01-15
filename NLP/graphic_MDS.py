import matplotlib.pyplot as plt
from sklearn.manifold import MDS

mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
xs, ys = pos[:, 0], pos[:, 1]

names = [os.path.basename(fn).replace('/Users/florianmante/Documents/matieres/ponts/3A/TDLOG/projet/data/texte_source/pdftotext', '') for fn in filenames]

# color-blind-friendly palette
for x, y, name in zip(xs, ys, names):
    if "2016" in name:
        color = 'orange' if "2016" in name else 'skyblue'
        plt.scatter(x, y, c=color)
        plt.text(x, y, name)


plt.show()


mds = MDS(n_components=3, dissimilarity="precomputed", random_state=1)

pos = mds.fit_transform(dist)
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])
#Out[48]: <mpl_toolkits.mplot3d.art3d.Path3DCollection at 0x2b96c03c1470>

for x, y, z, s in zip(pos[:, 0], pos[:, 1], pos[:, 2], names):
    if "2003" in s:
            ax.text(x, y, z, s)

plt.show()
