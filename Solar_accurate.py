# __author__ = 'azharhussain'
# CS 1
# 10/23/15
# EXTRA CREDIT PROGRAM TO CREATE MORE ACCURATE TIMESTEP

from cs1lib import *
from system_accurate import *
from body import Body

# Window size
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# Time scale to set the motion of the objects and how often the new location is computed
TIME_SCALE = 10000000        # how many real seconds for each second of simulation
PIXELS_PER_METER = .008 / 1e7  # distance scale for the simulation

# How smoothly the drawing of the planets is done is determined by frame rate and timestep
FRAME_RATE = 30             # frames per second
TIMESTEP = 1.0 / FRAME_RATE # time between drawing each frame

# Constants for distance of planet from sun and mass of planet based on the earth
AU = 1.49598e11
EU = 5.9736e24


def main():

    # Create the body object for each planet
    mercury = Body(.06*EU, .3871*AU, 0, 0, 47890, 3, 1,.28,0 )    # orange mercury
    venus = Body(.82*EU, .7233*AU, 0,0,35040, 5, 0,1,0)         #green venus
    earth = Body(EU, AU, 0, 0, 29790, 6, 0, 0, 1)            # blue earth
    mars = Body(.11*EU, 1.524*AU, 0, 0, 24140, 4, 1, 0, 0)      #red mars
    sun = Body(1.98892e30, 0, 0, 0, 0, 18, 1, 1, 0)            # yellow sun

    # create system object with all the body objects
    earth_moon = System([sun, mercury, venus, earth, mars])

    set_clear_color(0, 0, 0)    # black background
    enable_smoothing()

    while not window_closed():
        clear()

        # Draw the system in its current state.
        earth_moon.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

        # Update the system for its next state.
        earth_moon.update(TIMESTEP * TIME_SCALE)

        # Draw the frame and take a brief nap.
        request_redraw()
        sleep(TIMESTEP)

start_graphics(main, "Solar System simulation", WINDOW_WIDTH, WINDOW_HEIGHT)
