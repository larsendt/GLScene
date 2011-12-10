import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

def sin(theta):
	return math.sin(math.radians(theta))
	
def cos(theta):
	return math.cos(math.radians(theta))

def sphere():
	glPushMatrix()
	inc = 10
	
	for phi in range(-90, 90, inc):
		glBegin(GL_QUAD_STRIP)
		
		for theta in range(0, 360, 2*inc):
			vertex(theta, phi)
			vertex(theta, phi+inc)
		
		glEnd()
		
	glPopMatrix()
			
			
def vertex(th, ph):
	x = sin(th)*cos(ph)
	y = cos(th)*cos(ph)
	z = sin(ph)
	
	glNormal3f(x, y, z)
	glVertex3f(x, y, z)

