# Example using Blender's Python API
import bpy
import bmesh

# Get active object
obj = bpy.context.active_object

# Ensure it's a mesh
if obj.type == 'MESH':
    # Get a BMesh representation
    bm = bmesh.from_edit_mesh(obj.data)
    
    # Get UV layer
    uv_layer = bm.loops.layers.uv.verify()
    
    # Modify UV coordinates
    for face in bm.faces:
        for loop in face.loops:
            loop[uv_layer].uv.x *= 0.5  # Scale UVs in U direction
            loop[uv_layer].uv.y *= 0.5  # Scale UVs in V direction
    
    # Update the mesh
    bmesh.update_edit_mesh(obj.data)
