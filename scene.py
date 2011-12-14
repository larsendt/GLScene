import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

import lighting
import meshobj

class Scene(object):
	def __init__(self):
		self.light = lighting.Light(GL_LIGHT0)
		self.scale_counter = 0
		self.rotate_counter = 0
		self.monkey = meshobj.load_mesh("meshes/cube.obj")
		self.increasing = True
		self.change_speed = 1000.0
		
	def update(self):
		if self.increasing:
			self.scale_counter += 1
			if self.scale_counter > self.change_speed:
				self.scale_counter = self.change_speed
				self.increasing = False
		else:
			self.scale_counter -= 1
			if self.scale_counter < 0:
				self.scale_counter = 0
				self.increasing = True
				
		self.rotate_counter = (self.rotate_counter + 0.1) % 360

		self.light.update()
		
	def draw(self):				
		self.light.illuminate()

		glPushMatrix()
		glRotatef(-self.rotate_counter, 0, 1, 0)
		glScalef(1, self.scale_counter/self.change_speed, 1)
		glColor3f(0.1, 0.1, 0.1)		
		glCallList(self.monkey)
		glPopMatrix()
		

