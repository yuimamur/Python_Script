import imageio.v2
filenames = ["pc.png","monitor.png"]
images = []

for filename in filenames:
	images.append(imageio.v2.imread(filename))
imageio.mimsave('movie.gif',images,'GIF',duration=1)
