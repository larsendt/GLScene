import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

class MeshObject(object):
	def __init__(self, filename):
		try:
			f = open(filename, 'r')
		except:
			print "Hey. Hey. Hey buddy. Hey buddy! %s doesn't exist!" % filename
			sys.exit(1)
			
		verts = []
		norms = []
		faces = []
			
		for line in f:
			if line[0:2] == "v ":
				verts.append(self.process_vertex(line))
			elif line[0:2] == "vn":
				norms.append(self.process_normal(line))
			elif line[0:2] == "f ":
				faces.append(self.process_face(line))
				
		self.display_handle = glGenLists(1)
		glNewList(self.display_handle, GL_COMPILE)
		glBegin(GL_TRIANGLES)

		for face in faces:
			for item in face:
				glNormal3f(norms[item[1]-1][0], norms[item[1]-1][1], norms[item[1]-1][2])
				glVertex3f(verts[item[0]-1][0], verts[item[0]-1][1], verts[item[0]-1][2])

		glEnd()
		glEndList()
	
	def process_vertex(self, line):
		v = [float(i) for i in line.split(" ")[1:]]
		return v
		
	def process_normal(self, line):
		n = [float(i) for i in line.split(" ")[1:]]
		return n
		
	def process_face(self, line):
		ret = []
		x = line.replace("\n", "").split(" ")[1:]
		for i in x:
			ret.append([int(a) for a in i.split("/") if a])
		return ret			
		
		
