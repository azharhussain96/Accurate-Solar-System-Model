# __author__ = 'azharhussain'
# CS 1
# 10/18/15
# Program to create a Class system

from cs1lib import *
from body import *
from math import *

# Define gravity constant
G = 6.67384e-11

class System:

    # Consructor for System class
    def __init__(self, body_list):
        self.body_list = body_list

    # called to update the position, acceleration, and velocity of object
    def update(self, timestep):
        # update method for each object in the system list
        for n in range(0,len(self.body_list)):
            self.compute_acceleration(n,timestep)

    # method that computes the actual acceleration and adds up to total directional accleration
    def compute_acceleration(self,n,timestep):

        # Create total directional acceleration variables
        total_ax = 0
        total_ay = 0

        # iterate through the list of objects
        for i in self.body_list:
            # if object is not the same as the original object we are comparing
            if i != self.body_list[n]:

                # Compute radus squared to be used in the acceleration equation
                radius_squared = ((i.get_x() - self.body_list[n].get_x()) ** 2) + ((i.get_y() - self.body_list[n].get_y()) **2)

                # Compute total acceleration
                a = (G * i.get_mass())/radius_squared

                # break down accleration to directional components
                ax = a * ((i.get_x() - self.body_list[n].get_x()))/(sqrt(radius_squared))
                ay = a * ((i.get_y() - self.body_list[n].get_y()))/(sqrt(radius_squared))

                # Update total directional acceleration
                total_ax += ax
                total_ay += ay

        # call function to update velocity and position based on directional acceleration
        self.body_list[n].update_velocity(total_ax,total_ay,timestep)
        self.body_list[n].update_position(timestep)



    # Function to call craw on entire list of objects
    def draw(self, cx, cy, pixels_per_meter):
        for n in self.body_list:
            n.draw(cx,cy,pixels_per_meter)