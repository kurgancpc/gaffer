//////////////////////////////////////////////////////////////////////////
//  
//  Copyright (c) 2013-2014, Image Engine Design Inc. All rights reserved.
//  
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are
//  met:
//  
//      * Redistributions of source code must retain the above
//        copyright notice, this list of conditions and the following
//        disclaimer.
//  
//      * Redistributions in binary form must reproduce the above
//        copyright notice, this list of conditions and the following
//        disclaimer in the documentation and/or other materials provided with
//        the distribution.
//  
//      * Neither the name of John Haddon nor the names of
//        any other contributors to this software may be used to endorse or
//        promote products derived from this software without specific prior
//        written permission.
//  
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
//  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
//  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
//  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
//  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
//  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
//  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
//  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
//  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//  
//////////////////////////////////////////////////////////////////////////

surface typedCoshaderParameters(

	shader coshaderParameter = null;
#pragma annotation "coshaderParameterType1.coshaderType" "type1"
	shader coshaderParameterType1 = null;
#pragma annotation "coshaderParameterType2.coshaderType" "type2"
	shader coshaderParameterType2 = null;
#pragma annotation "coshaderParameterType3.coshaderType" "type3"
	shader coshaderParameterType3 = null;
	
	shader coshaderArrayParameter[4] = { null, null, null, null };
#pragma annotation "coshaderArrayParameterType1.coshaderType" "type1"
	shader coshaderArrayParameterType1[4] = { null, null, null, null };
#pragma annotation "coshaderArrayParameterType2.coshaderType" "type2"
	shader coshaderArrayParameterType2[4] = { null, null, null, null };
#pragma annotation "coshaderArrayParameterType3.coshaderType" "type3"
	shader coshaderArrayParameterType3[4] = { null, null, null, null };

)
{
	Ci = 1;
	Oi = 1;
}