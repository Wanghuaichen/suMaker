#include "suMeshViewer.h"

#include <iostream>
#include <suMesh.h>
#include "plugin/plugin_extend_selection.h"
#include "plugin/plugin_export_inp.h"

/**
 * A framework for volume optimization
 * The GUI is based on Wenzel Jakob's NanoGUI and  igl lib
 */

int main(int argc, char *argv[])
{
	//todo: if argc > 1 then run as console command
	//else

	suMeshViewer viewer;
	//load plugins first
	igl::viewer::plugin_extend_selection es; viewer.plugins.push_back(&es);
	igl::viewer::plugin_export_inp exp_inp; viewer.plugins.push_back(&exp_inp);
	
	//build UI
	viewer.build_UI();

	viewer.launch();
}

