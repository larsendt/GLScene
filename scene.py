import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

import objects
import lighting
import meshobj



class Scene(object):
	def __init__(self):
		self.light = lighting.Light(GL_LIGHT0)

		self.sphere = self.create_sphere()
		self.ring1 = self.create_ring(3)
		self.ring2 = self.create_ring(6)
		self.ring3 = self.create_ring(9)
		
		self.counter = 0
		self.monkey = meshobj.MeshObject("meshes/cube.obj").display_handle
		
	
	def create_ring(self, scale):
		glPushMatrix()
		ring = glGenLists(1)
		glNewList(ring, GL_COMPILE)
		mat_specular = (0.5, 0.5, 0.3, 1.0);
		mat_diffuse = (0.3, 0.3, 0.3, 1.0);
		mat_emission = (0.0, 0.0, 0.0, 0.0);
		glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
		glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
		glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
		glColor3f(0.0, 0.2, 0.5)
		glScalef(scale, scale, scale)
		glColor3f(0.5, 0.3, 0.0)		
		objects.ring()
		glEndList()
		glPopMatrix()
		return ring
		
	def create_sphere(self):
		glPushMatrix()
		sphere = glGenLists(1)
		glNewList(sphere, GL_COMPILE)
		mat_specular = (0.0, 0.0, 0.0, 1.0);
		mat_diffuse = (0.3, 0.3, 0.3, 1.0);
		mat_emission = (0.0, 0.0, 0.0, 0.0);
		glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
		glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
		glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
		glColor3f(0.2, 0.2, 0.2)
		objects.sphere()
		glEndList()
		glPopMatrix()
		return sphere
		
	def update(self):
		self.counter = (self.counter + 1) % 360
		self.light.update()
		
		
	def draw(self):				
		self.light.illuminate()
		glPushMatrix()
		#glCallList(self.sphere)
		glPopMatrix()
		glPushMatrix()
		glRotatef(self.counter, 1, 0, 0)
		glCallList(self.ring1)
		glPopMatrix()
		glPushMatrix()
		glRotatef(self.counter, 0, 1, 0)
		glCallList(self.ring2)
		glPopMatrix()
		glPushMatrix()
		glRotatef(self.counter, 1, 1, 0)
		glCallList(self.ring3)
		glPopMatrix()
		glPushMatrix()
		glScale(.5,.5,.5)
		glColor(.3,.5,1)
		glCallList(self.monkey)
		
		glPopMatrix()
		

