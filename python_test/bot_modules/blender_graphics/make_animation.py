import  bpy
import mathutils
import bmesh
import os
path = os.path.expanduser('~')

scene = bpy.context.scene

# Create the cube
mesh = bpy.data.meshes.new('cube')
ob = bpy.data.objects.new('cube', mesh)

scene.objects.link(ob)

bm = bmesh.new()
bmesh.ops.create_cube(bm, size=1.0)
bm.to_mesh(mesh)
bm.free()

# Create a light
light_data = bpy.data.lamps.new('light', type='POINT')
light = bpy.data.objects.new('light', light_data)
scene.objects.link(light)
light.location = mathutils.Vector((3, -4.2, 5))


# Create the camera
cam_data = bpy.data.cameras.new('camera')
cam = bpy.data.objects.new('camera', cam_data)
scene.objects.link(cam)
scene.camera = cam

cam.location = mathutils.Vector((6, -3, 5))
cam.rotation_euler = mathutils.Euler((0.9, 0.0, 1.1))

# render settings
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = path
bpy.ops.render.render(write_still = 1)