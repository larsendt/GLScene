import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

def load_mesh(filename):
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
			verts.append(process_vertex(line))
		elif line[0:2] == "vn":
			norms.append(process_normal(line))
		elif line[0:2] == "f ":
			faces.append(process_face(line))
			
	display_handle = glGenLists(1)
	glNewList(display_handle, GL_COMPILE)
	
	mat_specular = (0.3, 0.3, 0.3, 1.0);
	mat_diffuse = (1.0, 1.0, 1.0, 1.0);
	mat_emission = (0.0, 0.0, 0.0, 1.0);
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
	
	glBegin(GL_TRIANGLES)

	for face in faces:
		for item in face:
			glNormal3f(norms[item[1]-1][0], norms[item[1]-1][1], norms[item[1]-1][2])
			glVertex3f(verts[item[0]-1][0], verts[item[0]-1][1], verts[item[0]-1][2])

	glEnd()
	glEndList()
	
	return display_handle

def process_vertex(line):
	v = [float(i) for i in line.split(" ")[1:]]
	return v
	
def process_normal(line):
	n = [float(i) for i in line.split(" ")[1:]]
	return n
	
def process_face(line):
	ret = []
	x = line.replace("\n", "").split(" ")[1:]
	for i in x:
		ret.append([int(a) for a in i.split("/") if a])
	return ret			
		
		
