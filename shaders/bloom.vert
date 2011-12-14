uniform vec4 light_pos;
uniform float screen_width;
varying vec2 light_scr_pos;

void main()
{
	gl_Position = ftransform();
	gl_TexCoord[0] = gl_MultiTexCoord0;
	light_scr_pos = (gl_ModelViewProjectionMatrix * light_pos).xy * 0.5 + 0.5;
	light_scr_pos.x *= screen_width;
}
