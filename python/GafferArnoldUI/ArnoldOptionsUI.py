##########################################################################
#  
#  Copyright (c) 2012, John Haddon. All rights reserved.
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#  
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#  
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
##########################################################################

import Gaffer
import GafferUI
import GafferSceneUI
import GafferArnold

GafferUI.PlugValueWidget.registerCreator(
	
	GafferArnold.ArnoldOptions.staticTypeId(),
	"options",
	GafferSceneUI.SectionedParameterListPlugValueWidget,
	sections = (
		(
			"Sampling",
			(
				( "ai:AA_samples", "AA Samples" ),
				( "ai:GI_diffuse_samples", "Diffuse Samples" ),
				( "ai:GI_glossy_samples", "Glossy Samples" ),
				( "ai:GI_refraction_samples", "Refraction Samples" ),
			),
		),
		(
			"Features",
			(
				( "ai:ignore_textures", "Ignore Textures" ),
				( "ai:ignore_shaders", "Ignore Shaders" ),
				( "ai:ignore_atmosphere", "Ignore Atmosphere" ),
				( "ai:ignore_lights", "Ignore Lights" ),
				( "ai:ignore_shadows", "Ignore Shadows" ),
				( "ai:ignore_subdivision", "Ignore Subdivision" ),
				( "ai:ignore_displacement", "Ignore Displacement" ),
				( "ai:ignore_bump", "Ignore Bump" ),
				( "ai:ignore_motion_blur", "Ignore Motion Blur" ),
				( "ai:ignore_sss", "Ignore SSS" ),
			),
		),
		(
			"Error Colours",
			(
				( "ai:error_color_bad_texture", "Bad Texture" ),
				( "ai:error_color_bad_mesh", "Bad Mesh" ),
				( "ai:error_color_bad_pixel", "Bad Pixel" ),
				( "ai:error_color_bad_shader", "Bad Shader" ),
			),
		),
	),	
	
)
