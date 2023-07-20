import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Task 2 , plotting elliptical orbits

#solar system
from math import pi
from math import sqrt

# (u)- x-position of the center (v)- y-position of the center (a)-semi-major axis (b)- semi-minor axis



def ellipse(u,v,a,b):
    t=np.linspace(0, 2*pi,1000)
    plt.plot(u+a*np.cos(t),v+b*np.sin(t))
    
def ellipse_cent(u,v,a,b):
    t=np.linspace(0, 2*pi,1000)
    c = sqrt(a*a - b*b) #positions of focuses are (-c;0), (c;0)
    plt.plot(u+a*np.cos(t)+c,v+b*np.sin(t))
    



##
## Два меркурия. Как рисовали вы и сдвинутый
## функция ellipse_cent

# Sun

plt.plot(0, 0, 'bo')


# Mercury

ellipse(0
,0,0.39,0.37)

ellipse_cent(0
,0,0.39,0.37)


plt.xlabel('x/(AU)')
plt.ylabel('y/(AU)')
plt.title('orbits of five inner solar planets ')
plt.xlim(-1, 1)
plt.ylim(-1, 1)

plt.show()


##
## 4 орбиты отцентрованные по фокусу
## 

# Sun

plt.plot(0, 0, 'bo')


# Mercury

ellipse_cent(0
,0,0.39,0.37)

# Venus

ellipse_cent(0,0,0.72,0.72)

# Earth

ellipse_cent(0,0,1,1)

# Mars

ellipse_cent(0
,0,1.52,1.51)

plt.xlabel('x/(AU)')
plt.ylabel('y/(AU)')
plt.title('orbits of five inner solar planets ')
plt.xlim(-2, 2)
plt.ylim(-2, 2)



plt.show()


##
## Делаем картинку квадратной: меньше искажений
## plt.figure(figsize=(5, 5))


plt.figure(figsize=(5, 5))
# Sun

plt.plot(0, 0, 'bo')


# Mercury

ellipse_cent(0
,0,0.39,0.37)

# Venus

ellipse_cent(0,0,0.72,0.72)

# Earth

ellipse_cent(0,0,1,1)

# Mars

ellipse_cent(0
,0,1.52,1.51)

plt.xlabel('x/(AU)')
plt.ylabel('y/(AU)')
plt.title('orbits of five inner solar planets ')
plt.xlim(-2, 2)
plt.ylim(-2, 2)



plt.show()




