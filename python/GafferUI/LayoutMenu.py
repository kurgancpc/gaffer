##########################################################################
#  
#  Copyright (c) 2011-2012, John Haddon. All rights reserved.
#  Copyright (c) 2012-2013, Image Engine Design Inc. All rights reserved.
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

import os
import re

import IECore

import GafferUI

## Appends a submenu of the given name to the specified IECore.MenuDefinition. The submenu
# contains commands to facilitate the administration of different UI layouts.
def appendDefinitions( menuDefinition, name="" ) :

	menuDefinition.append( name, { "subMenu" : __layoutMenu } )

## A function suitable as the command for a Layout/Name menu item which restores a named layout.
# It must be invoked from a menu which has a ScriptWindow in its ancestry. 
def restore( menu, name ) :
	
	scriptWindow = menu.ancestor( GafferUI.ScriptWindow )	
	layout = GafferUI.Layouts.create( name, scriptWindow.scriptNode() )
		
	scriptWindow.setLayout( layout )

## A function suitable as the command for a Layout/Delete/LayoutName menu item.
def delete( name, menu ) :
	
	GafferUI.Layouts.remove( name )

	scriptWindow = menu.ancestor( GafferUI.ScriptWindow )	
	__saveLayouts( scriptWindow.scriptNode().applicationRoot() )
			
## A function suitable as the command for a Layout/Save... menu item. It must be invoked from
# a menu which has a ScriptWindow in its ancestry. 
def save( menu ) :

	scriptWindow = menu.ancestor( GafferUI.ScriptWindow )	

	layoutNames = GafferUI.Layouts.names()
	i = 1
	while True :
		layoutName = "Layout " + str( i )
		i += 1
		if "user:" + layoutName not in layoutNames :
			break  

	d = GafferUI.TextInputDialogue( initialText=layoutName, title="Save Layout", confirmLabel="Save" )
	t = d.waitForText( parentWindow = scriptWindow )
	d.setVisible( False )
	
	if t is None :
		return

	layout = scriptWindow.getLayout()
	
	GafferUI.Layouts.add( "user:" + t, layout )
	
	__saveLayouts( scriptWindow.scriptNode().applicationRoot() )
	
def __saveLayouts( applicationRoot ) :

	f = open( os.path.join( applicationRoot.preferencesLocation(), "layouts.py" ), "w" )
	f.write( "# This file was automatically generated by Gaffer.\n" )
	f.write( "# Do not edit this file - it will be overwritten.\n\n" )
	
	GafferUI.Layouts.save( f, re.compile( "user:.*" ) )

def __fullScreenKeyPress( scriptWindow, event ) :

	if event.key=="Escape" and scriptWindow.getFullScreen() :
		scriptWindow.setFullScreen( False )
		return True
		
	return False
	
def fullScreen( menu, checkBox ) :

	scriptWindow = menu.ancestor( GafferUI.ScriptWindow )	
	scriptWindow.setFullScreen( checkBox )
	scriptWindow.__fullScreenKeyPressConnection = scriptWindow.keyPressSignal().connect( __fullScreenKeyPress )
	
def fullScreenCheckBox( menu ) :

	scriptWindow = menu.ancestor( GafferUI.ScriptWindow )	
	return scriptWindow.getFullScreen()	
	
def __layoutMenu() :

	menuDefinition = IECore.MenuDefinition()
	
	layoutNames = GafferUI.Layouts.names()
	
	if layoutNames :
		
		def restoreWrapper( name ) :
		
			return lambda menu : restore( menu, name )
		
		for name in layoutNames :
		
			label = name
			if label.startswith( "user:" ) :
				label = label[5:]
					
			menuDefinition.append( label, { "command" : restoreWrapper( name ) } )			
	
		menuDefinition.append( "/SetDivider", { "divider" : True } )

	def deleteWrapper( name ) :
		
		return lambda menu, : delete( name, menu )

	for name in layoutNames :
	
		if name.startswith( "user:" ) :
			
			menuDefinition.append( "/Delete/%s" % name[5:], { "command" : deleteWrapper( name ) } )

	menuDefinition.append( "/Save...", { "command" : save } )

	menuDefinition.append( "/SaveDivider", { "divider" : True } )
	
	menuDefinition.append( "/Full Screen", { "command" : fullScreen, "checkBox" : fullScreenCheckBox, "shortCut" : "`" } )
	
	return menuDefinition
