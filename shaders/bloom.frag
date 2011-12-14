uniform sampler2D texture;
varying vec2 light_scr_pos;

const float cutoff = 0.2;

void main()
{
	float dist = distance(gl_TexCoord[0].xy, light_scr_pos);
	
	if(dist > cutoff)
	{
		dist = cutoff;
	}
	
	gl_FragColor = texture2D(texture, gl_TexCoord[0].xy) + vec4(cutoff-dist, cutoff-dist, cutoff-dist, 1.0);;
}

