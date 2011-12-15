uniform sampler2D texture;
varying vec2 light_pos;

const int NUM_SAMPLES = 100;
const float Density = 0.8;
const float Weight = 0.05;
const float Decay = 0.95;
const float Exposure = 0.5;

void main()
{  
	vec2 texCoord = gl_TexCoord[0].xy;
	
	// Calculate vector from pixel to light source in screen space.  
	vec2 deltaTexCoord = (texCoord - light_pos);  
	
	// Divide by number of samples and scale by control factor.  
	deltaTexCoord *= 1.0 / float(NUM_SAMPLES) * Density;  
	
	// Store initial sample.  
	vec4 color = texture2D(texture, texCoord);  
	
	// Set up illumination decay factor.  
	float illuminationDecay = 1.0;  
	
	// Evaluate summation from Equation 3 NUM_SAMPLES iterations.  
	for(int i = 0; i < NUM_SAMPLES; i++)  
	{  
		// Step sample location along ray.  
		texCoord -= deltaTexCoord;  
		
		// Retrieve sample at new location.  
		vec4 sample = texture2D(texture, texCoord); 
		 
		// Apply sample attenuation scale/decay factors.  
		sample *= illuminationDecay * Weight;  
		
		// Accumulate combined color.  
		color += sample;  
		
		// Update exponential decay factor.  
		illuminationDecay *= Decay;  
	}  
	// Output final color with a further scale control factor.  
	gl_FragColor = color * Exposure;
}  
