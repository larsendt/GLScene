import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

import shader

class PostProcessor(object):
	def __init__(self, width, height, scr_width, scr_height):
		self.width = width
		self.height = height	
		self.scr_width = scr_width
		self.scr_height = scr_height
		self.gen_buffers()
		
	def resize(self, width, height, scr_width, scr_height):
		self.width = width
		self.height = height
		self.scr_width = scr_width
		self.scr_height = scr_height
		self.gen_buffers()
		
	def gen_buffers(self):
		self.fbo = glGenFramebuffers(1)
		glBindFramebuffer(GL_FRAMEBUFFER, self.fbo)
		
		self.tex = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, self.tex)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, self.scr_width, self.scr_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, 0);
			
		self.depthbuf = glGenRenderbuffers(1)
		glBindRenderbuffer(GL_RENDERBUFFER, self.depthbuf)
		glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, self.scr_width, self.scr_height)

		glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, self.tex, 0);
		glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, self.depthbuf)

		fbo_status = glCheckFramebufferStatus(GL_FRAMEBUFFER);
		
		if fbo_status != GL_FRAMEBUFFER_COMPLETE:
			print "ERROR"

		glBindFramebuffer(GL_FRAMEBUFFER, 0)
		glBindTexture(GL_TEXTURE_2D, 0);
		glBindRenderbuffer(GL_RENDERBUFFER, 0); 
		
	def delete_buffers(self):
		glDeleteRenderBuffers(1, self.colorbuf)
		glDeleteRenderBuffers(1, self.depthbuf)
		glDeleteFramebuffers(1, self.fbo)
		
	def bind(self):
		glBindFramebuffer(GL_FRAMEBUFFER, self.fbo)
		
	def release(self):
		glBindFramebuffer(GL_FRAMEBUFFER, 0)
		
	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		
		glLoadIdentity()
		glBindTexture(GL_TEXTURE_2D, self.tex)
		glColor3f(1, 1, 1)
		
		glBegin(GL_POLYGON)
		glTexCoord2f(0, 0)
		glVertex3f(-self.width, -self.height, -3)
		glTexCoord2f(1, 0)
		glVertex3f(self.width, -self.height, -3)
		glTexCoord2f(1, 1)
		glVertex3f(self.width, self.height, -3)
		glTexCoord2f(0, 1)
		glVertex3f(-self.width, self.height, -3)
		glEnd()
		
		glBindTexture(GL_TEXTURE_2D, 0)
		
		glFlush();
		
		
