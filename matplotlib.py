import matplotlib.pyplot as plt

# if using Jupyter
%matplotlib inline
#or if not
plt.show() # will ddisplay your plots when not using jupyter

# two approaches
# functional approach
import numpy as np
x = np.linspace(0, 10, 20)  # genereate 20 datapoints between 0 and 10
y = x**2                    # generate array 'y' from square of 'x'
plt.plot(x,y)
plt.title['Our first Plot']
plt.xlabel('x label')
plt.ylabel('y label')

plt.show()


'''
the .subplot method needs three parameterrs:

 nrows: the number of rows the figure should have
 ncols: the number of columns the figure should have
 plot_number: which refers to the specific plot in the figure
'''
# plt.subplot(mrpws, ncols, plot_number)
plt.subplot(1,2,1)
plt.plot(x,y,'red')

plt.subplot(1,2,2)
plt.plot(y,x,'green')

# 2 Object oriented interface
fig = plt.figure()
ax = fig.add_axes([0.1, 0.2, 0.8, 0.9])

ax. plot(x,y,'purple')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title('Our first plot usinmg object oriented approach')

# can use two plots on the same figure
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
axes1.plot(x,y)
axes2.plot(y.x)

# use .subplots(nrows, ncols)
fig, ax = plt.subplots(nrows=3, ncols=3)
ax[0,1].plot(x,y)
ax[1,2].plot(y,x)
plt.tight_layout()

# adding figsize and dpi
fig = plt.figure(figsize=(8,2), dpi=100)
ax[0].plot(x,y)
ax[1].plot(y,x)
plt.tight_layout()

# Saving a plot to disk
fig.savefig('my_figure.png')

# to display the saved figure
import matplotlib.image as mping
plt.imshow(mping.imread('my_figure.ping'))

# legends for multiple plots
fig = plt.figure(figsize=(8.6), dpi=60)
ax = fig.add_axes(0,0,1,1)
ax.plot(x,x**2, label='X square plot')
ax.plot(x,x**3, 'red', label='X cube plot')

ax.legend()