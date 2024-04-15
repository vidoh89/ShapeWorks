import bpy

class VIEW3D_PT_my_custom_panel(bpy.types.Panel): 
    
    #where to add the panel in the UI
    bl_space_type="VIEW_3D" #3D viewport
    bl_region_type= "UI" #Sidebar region
    
    #add labels
    bl_category = "My Custom Panel category"
    bl_label = "My Custom Panel label"
    #creates the layout of the UI
    def draw(self,context):
        """define the layout of the panel"""
        #create the row layout for the buttons
        #button to add sphere
        row = self.layout.row()
        row.operator("mesh.primitive_cube_add", text="Add Cube")
        
        #button to add Ico Sphere
        row = self.layout.row()
        row.operator("mesh.primitive_ico_sphere_add",text="Add Ico Sphere")
        #add shade smooth row and operator button
        row = self.layout.row()
        row.operator("object.shade_smooth", text="Shade Smooth")
        #add quick explode button
        row = self.layout.row()
        row.operator("object.quick_explode", text="Explode Effect")
        #add fur
        row = self.layout.row()
        row.operator()
        
#register the panel with blender
def register():
    bpy.utils.register_class(VIEW3D_PT_my_custom_panel)
#unregister the panel with blender
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)
if __name__== "__main__":
    register()