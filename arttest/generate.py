import bpy
import os
import sys

from bpy.types import ViewLayer

blend_file_path = bpy.data.filepath
directory = os.path.dirname(blend_file_path)
base_name = os.path.basename(blend_file_path).removesuffix(".blend")
out_path = directory + "/out"
cache_path = directory + "/cache"
sql_path = directory + "/sql"

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"
color = ""
for arg in argv:
    color = arg

if color == "":
    print("no color passed")
    exit(1)
if color != "green" and color != "blue" and color != "pink" and color != "black":
    print("invalid color: "+color)
    exit(1)

print("generating "+color+" map")

light_data = bpy.data.lights.new(name="lightdata", type='POINT')
light_data.energy = 30

light_collection = bpy.data.collections.new("lights")
bpy.context.scene.collection.children.link(light_collection)

object_collection = bpy.data.collections.new("objects")
bpy.context.scene.collection.children.link(object_collection)

bpy.data.objects["Cube"].data.materials[0] = bpy.data.materials[color]

for i in range(0, 398):
    light_object = bpy.data.objects.new(name="light."+str(i), object_data=light_data)
    light_collection.objects.link(light_object)
    #bpy.context.collection.objects.link(light_object)
    bpy.context.view_layer.objects.active = light_object
    light_object.location = (i*5, 0, 4)

    o = bpy.data.objects.new(name="object."+str(i), object_data=None)
    o.location = (i*5, 3, 2)
    object_collection.objects.link(o)
    o["emit"] = i

bpy.ops.wm.save_as_mainfile(filepath=base_name+"_"+color+".blend")
