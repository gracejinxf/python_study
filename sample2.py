def ball_trajectory(x):
    location = 10*x - 5*(x**2)
    return (location)

import matplotlib.pyplot as plt
xs= [x/100 for x in list (range(201))]
ys= [ball_trajectory(x) for x in xs]
plt.plot(xs,ys)
plt.title ('The Trajectory of a thrown ball')
plt.xlabel ('Horizontal Position of ball')
plt.ylabel('Vertical Position of ball')
plt.axhline(y=0)
plt.show()