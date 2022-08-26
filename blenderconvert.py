import bpy
import os


path = 'D:/Airport/Umodel'
print('<<<<<<<<<<<START>>>>>>>>>>')

for root, dirs, files in os.walk(path):
    for currentFile in files:
        exts = ('.pskx')
        if currentFile.lower().endswith(exts):
            mesh_file = os.path.join(root, currentFile)
            fbx_file = os.path.splitext(mesh_file)[0] + ".fbx"
            if (not(os.path.exists(fbx_file))):
                bpy.ops.object.select_all(action='SELECT')
                bpy.ops.object.delete()
                bpy.ops.import_scene.psk(filepath=mesh_file)
                bpy.ops.object.select_all(action='SELECT')
                for obj in bpy.data.objects:
                    if obj.type == 'MESH':
                        obj.data.use_auto_smooth = 1
                        obj.data.auto_smooth_angle = 0.872665
                bpy.ops.object.shade_smooth()
                bpy.ops.export_scene.fbx(filepath=fbx_file)

print('<<<<<<<<<<<DONE>>>>>>>>>>')