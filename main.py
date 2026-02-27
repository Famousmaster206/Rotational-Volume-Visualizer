import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import axes3d

def calculate_volume(func_string, bound1, bound2):
    #conver the string to a function
    func = lambda x: eval(func_string)
    x_values = np.linspace(bound1, bound2, 1000)
    dx = (bound2 - bound1) / 1000
    
    #disk method
    volumes = np.pi * func(x_values)**2 * dx
    sum_volume = np.sum(volumes)
    return sum_volume

def plot_solid_disk(func_string, bound1, bound2):
    #convert the string to a function
    fun = lambda x: eval(func_string)

    #set up the x-axis and rotation angle
    xAxis = np.linspace(bound1, bound2, 100)
    rotationAngle = np.linspace(0, 2 * np.pi, 60)

    #create a meshgrid for x and rotation angle
    XA, RA = np.meshgrid(xAxis, rotationAngle)

    #calculate the y and z values for the surface
    yValue = fun(XA) * np.cos(RA)
    zValue = fun(XA) * np.sin(RA)

    #plot the surface
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot(111, projection='3d')
    axis.plot_surface(XA, yValue, zValue, alpha=0.8)

    #calculate the volume and set the title
    volume = calculate_volume(func_string, bound1, bound2)
    axis.set_title(f"Solid of Revolution: {func_string}\nVolume: {volume:.4f}")
    
    plt.show()
    
def plot_solid_washer(outerFunc, innerFunc, bound1, bound2):
    #convert the strings to functions
    outer = lambda x: eval(outerFunc)
    inner = lambda x: eval(innerFunc)

    #calculate the volumes of the outer and inner solids
    vol_outer = calculate_volume(outerFunc, bound1, bound2)
    vol_inner = calculate_volume(innerFunc, bound1, bound2)
    total_volume = vol_outer - vol_inner

    #set up the x-axis and rotation angle
    xAxis = np.linspace(bound1, bound2, 100)
    rotationAngle = np.linspace(0, 2 * np.pi, 60)
    XA, RA = np.meshgrid(xAxis, rotationAngle)

    #calculate the y and z values for the outer and inner surfaces
    outerY, outerZ = outer(XA) * np.cos(RA), outer(XA) * np.sin(RA)
    innerY, innerZ = inner(XA) * np.cos(RA), inner(XA) * np.sin(RA)

    #plot the surfaces
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot(111, projection='3d')

    #set title and labels
    axis.plot_surface(XA, outerY, outerZ, alpha=0.8, color='blue', label='Outer Surface')
    axis.plot_surface(XA, innerY, innerZ, alpha=0.8, color='red', label='Inner Surface')
    axis.set_title(f"Washer Method: Outer: {outerFunc}, Inner: {innerFunc}\nVolume: {total_volume:.4f}")
    plt.show()
