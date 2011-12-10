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
	inc = 5
	
	for phi in range(-90, 90, inc):
		glBegin(GL_QUAD_STRIP)
		
		for theta in range(0, 360+inc, 2*inc):
			vertex(theta, phi)
			vertex(theta, phi+inc)
		
		glEnd()
		
	glPopMatrix()
	

def ring():
	glPushMatrix()
	
	inc = 5
	w = 0.02
	r = 0.5
	inr = r - 0.01
		
	glBegin(GL_QUADS)
			
	for i in range(0, 360, inc):
		glNormal3f(cos(i), sin(i), 0.0)
		glVertex3f(cos(i)*r, sin(i)*r, -w)
		
		glNormal3f(cos(i+inc), sin(i+inc), 0.0)
		glVertex3f(cos(i+inc)*r, sin(i+inc)*r, -w)
		glVertex3f(cos(i+inc)*r, sin(i+inc)*r, +w)
		
		glNormal3f(cos(i), sin(i), 0.0)
		glVertex3f(cos(i)*r, sin(i)*r, +w)
		
	glEnd()
	glBegin(GL_QUADS)
	for i in range(0, 360, inc):
		glNormal3f(-cos(i), -sin(i), 0.0)
		glVertex3f(cos(i)*inr, sin(i)*inr, -w)
		
		glNormal3f(-cos(i+inc), -sin(i+inc), 0.0)
		glVertex3f(cos(i+inc)*inr, sin(i+inc)*inr, -w)
		glVertex3f(cos(i+inc)*inr, sin(i+inc)*inr, +w)
		
		glNormal3f(-cos(i), -sin(i), 0.0)
		glVertex3f(cos(i)*inr, sin(i)*inr, +w)
		
	glEnd()
	glBegin(GL_QUADS)
			
	for i in range(0, 360, inc):
		glNormal3f(0.0, 0.0, 1.0)
		glVertex3f(cos(i)*inr, sin(i)*inr, +w)
		glVertex3f(cos(i+inc)*inr, sin(i+inc)*inr, +w)
		glVertex3f(cos(i+inc)*r, sin(i+inc)*r, +w)
		glVertex3f(cos(i)*r, sin(i)*r, +w)
		
	glEnd()
	glBegin(GL_QUADS)
			
	for i in range(0, 360, inc):
		glNormal3f(0.0, 0.0, -1.0)
		glVertex3f(cos(i)*inr, sin(i)*inr, -w)
		glVertex3f(cos(i+inc)*inr, sin(i+inc)*inr, -w)
		glVertex3f(cos(i+inc)*r, sin(i+inc)*r, -w)
		glVertex3f(cos(i)*r, sin(i)*r, -w)
		
	glEnd()
	glPopMatrix()
		
			
			
def vertex(th, ph):
	x = sin(th)*cos(ph)
	y = cos(th)*cos(ph)
	z = sin(ph)
	
	glNormal3f(x, y, z)
	glVertex3f(x, y, z)

