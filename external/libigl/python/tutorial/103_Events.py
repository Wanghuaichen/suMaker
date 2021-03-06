# Add the igl library to the modules search path
import sys, os
sys.path.insert(0, os.getcwd() + "/../")

import pyigl as igl

V1 = igl.eigen.MatrixXd()
F1 = igl.eigen.MatrixXi()

V2 = igl.eigen.MatrixXd()
F2 = igl.eigen.MatrixXi()

def key_pressed(viewer, key, modifier):
    print("Key: ", chr(key))

    if key == ord('1'):
        # # Clear should be called before drawing the mesh
        viewer.data.clear();
        # # Draw_mesh creates or updates the vertices and faces of the displayed mesh.
        # # If a mesh is already displayed, draw_mesh returns an error if the given V and
        # # F have size different than the current ones
        viewer.data.set_mesh(V1, F1);
        viewer.core.align_camera_center(V1,F1);
    elif key == ord('2'):
        viewer.data.clear();
        viewer.data.set_mesh(V2, F2);
        viewer.core.align_camera_center(V2,F2);
    return False


#  Load two meshes
igl.readOFF("../../tutorial/shared/bumpy.off", V1, F1);
igl.readOFF("../../tutorial/shared/fertility.off", V2, F2);

print("1 Switch to bump mesh")
print("2 Switch to fertility mesh")

viewer = igl.viewer.Viewer()

# Register a keyboard callback that allows to switch between
# the two loaded meshes
viewer.callback_key_pressed = key_pressed
viewer.data.set_mesh(V1, F1)
viewer.launch()
