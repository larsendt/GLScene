import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from ctypes import *

import shader

class PostProcessor(object):
	def __init__(self, width, height, scr_width, scr_height):
		self.width = width
		self.height = height	
		self.scr_width = scr_width
		self.scr_height = scr_height
		self.light_pos = (0, 0, 0, 1)
		self.gen_buffers()
		
		self.bloom_shader = shader.Shader("./shaders/bloom.vert", "./shaders/bloom.frag")
		
	def resize(self, width, height, scr_width, scr_height):
		self.width = width
		self.height = height
		self.scr_width = scr_width
		self.scr_height = scr_height
		self.delete_buffers()
		self.gen_buffers()
		
	def gen_buffers(self):
		self.tex = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, self.tex)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.scr_width, self.scr_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, None)
		glBindTexture(GL_TEXTURE_2D, 0)

		self.depthbuf = glGenRenderbuffers(1)
		glBindRenderbuffer(GL_RENDERBUFFER, self.depthbuf)
		glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, self.scr_width, self.scr_height)
		glBindRenderbuffer(GL_RENDERBUFFER, 0)

		self.fbo = glGenFramebuffers(1)
		glBindFramebuffer(GL_FRAMEBUFFER, self.fbo)
		glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, self.tex, 0)
		glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, self.depthbuf)

		fbo_status = glCheckFramebufferStatus(GL_FRAMEBUFFER)
		if fbo_status != GL_FRAMEBUFFER_COMPLETE:
			print "Frame buffer cannot be generated!"

		glBindFramebuffer(GL_FRAMEBUFFER,0)
		
	def delete_buffers(self):
		glDeleteTextures(self.tex)
		glDeleteRenderbuffers(1, byref(c_int(self.depthbuf)))
		glDeleteFramebuffers(1, byref(c_int(self.fbo)))
		
	def bind(self):
		glBindFramebuffer(GL_FRAMEBUFFER, self.fbo)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		
	def release(self):
		glBindFramebuffer(GL_FRAMEBUFFER, 0)
		
	def draw(self):
		glViewport(0, 0, self.scr_width, self.scr_height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(-self.width, self.width, -1, 1, -1, 5)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
	
		self.bloom_shader.bind()
		glActiveTexture(GL_TEXTURE0)
		glBindTexture(GL_TEXTURE_2D, self.tex)
		self.bloom_shader.setUniform1i("texture", 0)
		self.bloom_shader.setUniform1f("screen_width", self.width)
		self.bloom_shader.setUniform4f("light_pos", self.light_pos[0], self.light_pos[1], self.light_pos[2], self.light_pos[3])
		glDisable(GL_LIGHTING)
		glColor3f(1, 1, 1)
		
		glBegin(GL_POLYGON)
		glTexCoord2f(0, 0)
		glVertex3f(-self.width, -self.height, 0)
		glTexCoord2f(1, 0)
		glVertex3f(self.width, -self.height, 0)
		glTexCoord2f(1, 1)
		glVertex3f(self.width, self.height, 0)
		glTexCoord2f(0, 1)
		glVertex3f(-self.width, self.height, 0)
		glEnd()
		
		self.bloom_shader.release()
		
		glEnable(GL_LIGHTING)
		glBindTexture(GL_TEXTURE_2D, 0)
		
		glViewport(0, 0, self.scr_width, self.scr_height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(45, self.width, 0.5, 10)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		
		
