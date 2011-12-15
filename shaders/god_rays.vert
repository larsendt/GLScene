uniform vec4 light_coords;
varying vec2 light_pos;

void main()
{
	gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
	gl_TexCoord[0] = gl_MultiTexCoord0;
	light_pos = vec2(gl_ModelViewProjectionMatrix * light_coords) * 0.5 + 0.5;
}
