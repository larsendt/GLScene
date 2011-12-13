import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

def loadObj(filename):
	# vertices
	v = []
	# normals
	n = []
	# elements
	e = []
	# file object
	
	f = open(filename, 'r')
	for line in f:
		if line[0:2] == "v ":
			string = line[2:].split(" ")
			v.append([float(string[0]), float(string[1]), float(string[2])])
		elif line[0:2] == "f ":
			string = line[2:].split(" ")
			e.append(int(string[0])-1)
			e.append(int(string[1])-1)
			e.append(int(string[2])-1)
		else:
			continue
	
	n = [[0,0,0]]*len(v)
	i = 0
	while i < len(e):
		print i, len(e)
		ia = e[i]
		ib = e[i+1]
		ic = e[i+2]
		normal = cross(sub(v[ib], v[ia]), sub(v[ic], v[ib]))
		n[ic] = normal;
		n[ib] = normal;
		n[ia] = normal;
		i+=3
	return v, n, e
		

def cross(a, b):
	v = [0,0,0]
	v[0] = a[1]*b[2] - a[2]*b[1]
	v[1] = a[2]*b[0] - a[0]*b[2]
	v[2] = a[0]*b[1] - a[1]*b[0]
	return v
	
def sub(a, b):
	v = [0,0,0]
	v[0] = a[0]-b[0]
	v[1] = a[1]-b[1]
	v[2] = a[2]-b[2]
	return v
	
def compileMesh(v, n, e):
	a = glGenLists(1)
	glNewList(a, GL_COMPILE)
	mat_specular = (0,0,0, 1.0);
	mat_diffuse = (-.4, -.4, -.4, 1.0);
	mat_emission = (0.0, 0.0, 0.0, 0.0);
	glMaterialfv(GL_FRONT, GL_SHININESS, 0)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
	
	glBegin(GL_TRIANGLES)
	i = 0

	while i < (len(e)):
		first = e[i]
		second = e[i+1]
		third = e[i+2]
		glNormal(n[first][0],n[first][1],n[first][2])
		glVertex(v[first][0],v[first][1],v[first][2])
		
		glNormal(n[second][0],n[second][1],n[second][2])
		glVertex(v[second][0],v[second][1],v[second][2])
		
		glNormal(n[third][0],n[third][1],n[third][2])
		glVertex(v[third][0],v[third][1],v[third][2])
		i+=3
		
	glEnd()
	glEndList()
	return a
