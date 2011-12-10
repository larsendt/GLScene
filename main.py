#!/usr/bin/env python

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import shader
import time
import random
import scene

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
		
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glShadeModel(GL_SMOOTH)
		glEnable(GL_NORMALIZE)
		glEnable(GL_LIGHTING)
		glColorMaterial(GL_FRONT,GL_AMBIENT_AND_DIFFUSE)
		glEnable(GL_COLOR_MATERIAL)
		
		self.time = time.clock()
		self.screen_width = 1.0
		self.shader = shader.Shader("./shaders/plain.vert", "./shaders/plain.frag")
		self.seed = random.uniform(0, 5000)
		self.last_mouse_pos = 0, 0
		self.x_rotation = 0
		self.y_rotation = 0
		self.scene = scene.Scene()
		self.zoom = 0
		self.fps = 60
		self.idle_tick = 1.0/self.fps
	
	def begin(self):
		glutMainLoop()

	def idle(self):
		if (time.clock() - self.time) > self.idle_tick:
			self.time = time.clock()
			self.scene.update()
			glutPostRedisplay();
	
	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity();
		
		glTranslatef(0.0, 0.0, -2.0)
		glRotatef(self.x_rotation, 1, 0, 0)
		glRotatef(self.y_rotation, 0, 1, 0)
		glScalef(0.4-self.zoom, 0.4-self.zoom, 0.4-self.zoom)
		
		self.shader.bind()
		self.shader.setUniform1f("time", self.time)
		self.shader.setUniform1f("seed", self.seed)
		self.scene.draw()
		self.shader.release()
	
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
		gluPerspective(45, self.screen_width, 0.5, 10)
		#glOrtho(-self.screen_width, self.screen_width, -1, 1, -1, 5)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		
	def mouse_drag(self, x, y):
		dx = x - self.last_mouse_pos[0]
		dy = y - self.last_mouse_pos[1]
		self.x_rotation += dy
		self.y_rotation += dx
		self.last_mouse_pos = x, y
	
	def mouse_press(self, button, state, x, y):
		if button == 0:
			self.last_mouse_pos = x, y
		elif (button == 3 or button == 4) and state == GLUT_DOWN:
			if button == 3:
				self.zoom -= 0.01
			else:
				self.zoom += 0.01
	
	def keyboard(self, key, x, y):
		if key == '\x1b': #escape key
			print "quit"
			sys.exit(0)
			
	
def main():
	print "Initializing OpenGL..."
	gl_wrapper = GLWrapper()
	gl_wrapper.begin()
	
if __name__ == "__main__":
	main()
