def display_distance_txt3d(dist, names, year):
    fig = plt.figure()
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=38, azim=104)
    plt.cla()
    # ax = fig.add_subplot(111, projection='3d')
    pos = compute_pos3d(dist)
    # ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])
    for x, y, z, s in zip(pos[:, 0], pos[:, 1], pos[:, 2], names):
        if year in s:
            ax.scatter(x, y, z)
            ax.text(x, y, z, s)
    plt.show()


def display_distance_txt2d(dist, names, year):

    xs, ys = compute_pos2d(dist)
    for x, y, name in zip(xs, ys, names):
        if year in name:
            color = 'orange' if year in name else 'skyblue'
            plt.scatter(x, y, c=color)
            plt.text(x, y, name)
        plt.show()