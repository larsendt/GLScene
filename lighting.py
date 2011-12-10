import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

import objects
import math

class Light(object):
	def __init__(self, light_id):
		self.ambient = (0.3, 0.3, 0.3, 1.0)
		self.diffuse = (0.5, 0.5, 0.5, 1.0)
		self.specular = (1.0, 1.0, 1.0, 1.0)
		self.position = (2.0, 0.0, 2.0, 1.0)
		self.light_id = light_id
		self.mat_specular = (0.0, 0.0, 0.0, 1.0);
		self.mat_diffuse = (0.3, 0.3, 0.3, 1.0);
		self.mat_emission = (1.0, 1.0, 1.0, 1.0);
		self.mat_shininess = (128);
		self.counter = 0
		glEnable(light_id)
		self.scene_ambient = (0.3, 0.3, 0.3, 1.0);
		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.scene_ambient);
		
		self.sphere = glGenLists(1)
		glNewList(self.sphere, GL_COMPILE)
		
		glMaterialfv(GL_FRONT, GL_DIFFUSE, self.mat_diffuse)
		glMaterialfv(GL_FRONT, GL_SHININESS, self.mat_shininess)
		glMaterialfv(GL_FRONT, GL_SPECULAR, self.mat_specular)
		glMaterialfv(GL_FRONT, GL_EMISSION, self.mat_emission)
		glScalef(0.1, 0.1, 0.1)
		glColor3f(1, 1, 1)
		objects.sphere()
		
		glEndList()

		
	def update(self):
		self.counter =  (self.counter + 1) % 360
		
	def illuminate(self):
		glPushMatrix()
		glRotatef(30, 0, 0, 1)
		glRotatef(self.counter, 0, 1, 0)
		
		glPushMatrix()
		glTranslatef(self.position[0], self.position[1], self.position[2])
		glCallList(self.sphere)
		glPopMatrix()
	
		glLightfv(self.light_id, GL_AMBIENT, self.ambient)
		glLightfv(self.light_id, GL_DIFFUSE, self.diffuse)
		glLightfv(self.light_id, GL_SPECULAR, self.specular)
		glLightfv(self.light_id, GL_POSITION, self.position)

		glPopMatrix()
