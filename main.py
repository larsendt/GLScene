#!/usr/bin/env python

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import shader
import time
import random
import objects

class GLWrapper(object):
	def __init__(self):
		glutInit(len(sys.argv), sys.argv)
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
		glutInitWindowSize(800, 600)
		glutCreateWindow('Dynamic Skybox')
		glutDisplayFunc(self.draw)
		glutMotionFunc(self.mouse_drag)
		glutKeyboardFunc(self.keyboard)
		glutMouseFunc(self.mouse_press)
		glutReshapeFunc(self.reshape)
		glutIdleFunc(self.idle)
		
		self.time = time.clock()
		self.screen_width = 1.0
		self.shader = shader.Shader("./shaders/skybox.vert", "./shaders/skybox.frag")
		self.seed = random.uniform(0, 5000)
	
	def begin(self):
		glutMainLoop()

	def idle(self):
		self.time = time.clock()
		glutPostRedisplay();
	
	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glLoadIdentity();
		
		#self.shader.bind()
		#self.shader.setUniform1f("time", self.time)
		#self.shader.setUniform1f("seed", self.seed)
				
		glColor3f(1, 1, 1)
		objects.sphere()

		#self.shader.release()
	
		glFlush();
		glutSwapBuffers();
	
	def reshape(self, width, height):
		if height > 0:
			self.screen_width = float(width)/height
		else:
			self.screen_width = 1.0
		
		glViewport(0,0, width,height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(-self.screen_width,+self.screen_width, -1.0,+1.0, -1.0,+5.0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
	
	def mouse_drag(self, x, y):
		print "mouse_drag"
	
	def mouse_press(self, button, state, x, y):
		print "mouse press"
	
	def keyboard(self, key, x, y):
		if key == '\x1b': #escape key
			print "quit"
			sys.exit(0)
	
		print "keyboard"
	
def main():
	print "Initializing OpenGL..."
	gl_wrapper = GLWrapper()
	gl_wrapper.begin()
	
if __name__ == "__main__":
	main()
