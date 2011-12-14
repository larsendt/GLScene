from Image import open

def load_texture(self, image_name):
		im = open(image_name)
		try:
			ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
		except SystemError:
			ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)

		ID = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, ID)
		glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
		return ID

