varying vec2 pos;

void main()
{
	gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
	pos = vec2(gl_Position);
}
