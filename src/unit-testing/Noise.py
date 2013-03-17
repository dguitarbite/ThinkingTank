# Terrain generation based on noise.
# The terrain is a simple line grid.

# Noise generation using Casey Duncan's noise library:
# http://pypi.python.org/pypi/noise/1.0b1

# Use WASD to move through the scene
# Use Q and E to move up/down
# Use the mouse to look in the view
# Use the arrow keys to offset the noise grid
# Use I/K to increase/decrease noise scale
# Use O/L to increase/decrease noise amplitude


from math import sin, cos
from random import random, seed

import pyglet
from pyglet.window import key
from pyglet.gl import *

from noise.perlin import SimplexNoise

rotation_x = 0
rotation_y = 0
rotation_z = 0
translate_x = 0
translate_y = -1
translate_z = -10
noise_scale = 0.3
noise_amplitude = 0.4
noise_offset_x = 0.0
noise_offset_y = 0.0

try:
  # Try and create a window with multisampling (anti-aliasing)
  config = Config(sample_buffers=1, samples=4, depth_size=16, double_buffer=True)
  window = pyglet.window.Window(resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
  # Fall back to no multisampling for old hardware
  window = pyglet.window.Window(resizable=True)

noise = SimplexNoise()

@window.event
def on_resize(width, height):
  glViewport(0, 0, width, height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(60., width / float(height), .1, 1000.)
  glMatrixMode(GL_MODELVIEW)
  return pyglet.event.EVENT_HANDLED

def update(dt):
  global rotation_x, rotation_y, rotation_z
  global translate_x, translate_y, translate_z
  global noise_scale, noise_amplitude
  global noise_offset_x, noise_offset_y
  speed = 0.2
  value = 0.05
  update_terrain = False
  if keys[key.W]:
    translate_z += speed
  if keys[key.S]:
    translate_z -= speed
  if keys[key.A]:
    translate_x -= speed
  if keys[key.D]:
    translate_x += speed
  if keys[key.Q]:
    translate_y += speed
  if keys[key.E]:
    translate_y -= speed
  if keys[key.I]:
    noise_scale += value
    update_terrain = True
  if keys[key.K]:
    noise_scale -= value
    update_terrain = True
  if keys[key.O]:
    noise_amplitude += value
    update_terrain = True
  if keys[key.L]:
    noise_amplitude -= value
    update_terrain = True
  if keys[key.LEFT]:
    noise_offset_x -= 0.1
    update_terrain = True
  if keys[key.RIGHT]:
    noise_offset_x += 0.1
    update_terrain = True
  if keys[key.UP]:
    noise_offset_y -= 0.1
    update_terrain = True
  if keys[key.DOWN]:
    noise_offset_y += 0.1
    update_terrain = True

  if update_terrain:
    make_terrain()
pyglet.clock.schedule(update)

@window.event
def on_mouse_motion(x, y, dx, dy):
  global rotation_x, rotation_y
  cx = window.width/2-x
  cy = window.height/2-y
  rotation_y = cx/5.0
  rotation_x = cy/5.0

def float_range(begin, end, step):
  v = begin
  while v < end:
    yield v
    v += step

@window.event
def on_draw():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  glTranslatef(translate_x, translate_y, translate_z)
  glRotatef(rotation_x, 1, 0, 0)
  glRotatef(rotation_y, 0, 1, 0)
  glRotatef(rotation_z, 0, 0, 1)

  # Draw the grid
  global terrain_list
  for line_list in terrain_list:
    glBegin(GL_LINE_STRIP)
    for x, y, z in line_list:
      glVertex3f(x, y, z)
    glEnd()

def make_terrain():
  global terrain_list, noise_scale, noise_amplitude, noise_offset_x, noise_offset_y
  terrain_list = []
  seed(1)
  for z in float_range(-5, 5, 0.1):
    line_list = []
    for x in float_range(-5, 5, 0.1):
      y = noise.noise2(noise_offset_x + x*noise_scale, noise_offset_y + z*noise_scale)*noise_amplitude
      line_list.append((x, y, z))
    terrain_list.append(line_list)

def setup():
  # One-time GL setup
  glClearColor(0.9, 0.9, 1, 1)
  glColor3f(0, 0.6, 0)
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)

  # Wireframe view
  glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

setup()
keys = key.KeyStateHandler()
window.push_handlers(keys)
make_terrain()
pyglet.app.run()

