# __author__ = 'azharhussain'
# CS 1
# 10/18/15
# Program to create a Class body

from cs1lib import *

class Body:

    # Constructor for planet body
    def __init__(self, mass, x, y, vx, vy, image):

        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = image

    # method to update the velocity based on directional acceleration and time
    def update_velocity(self, ax, ay, timestep):
        self.vx = (ax * timestep) + self.vx
        self.vy = (ay * timestep) + self.vy

    # method to update position based on directional velocity and time
    def update_position(self, timestep):
        self.x = (self.vx * timestep) + self.x
        self.y = (self.vy * timestep) + self.y

    # draw method to create circular planets
    def draw(self, cx, cy, pixels_per_meter):
        #set_fill_color(self.r,self.g,self.b)
        draw_image(self.image, ((self.x * pixels_per_meter) + cx), ((self.y * pixels_per_meter) + cy))
        #draw_circle(((self.x * pixels_per_meter) + cx), ((self.y * pixels_per_meter) + cy), self.pixel_radius)

    # returns mass of object
    def get_mass(self):
        return self.mass

    # returns x coordinate of object
    def get_x(self):
        return self.x

    # returns y coordinate of object
    def get_y(self):
        return self.y
