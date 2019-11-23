#!/usr/bin/env python
# coding: utf-8

# In[7]:




#bob.fd(100)bob.lt(90)bob.fd(100)bob.lt(90)bob.fd(100)bob.lt(90)bob.fd(100)

#turtle.mainloop()


# In[17]:


for i in range(4):
    print("hello")


# In[15]:


import turtle 


# In[16]:


def square (t):
    t = turtle.Turtle()
    for i in range(4):
        t.fd(100)
        t.lt(90)
    
    turtle.mainloop()
    


# In[ ]:


def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


# In[ ]:


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# In[17]:


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


# In[18]:


def arc(t, r, angle):

    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


# In[ ]:




