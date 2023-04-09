import bpy

bl_info = {
    "name": "Emulate MB 3",
    "author": "ZuneDai",
    "version": (0,0, 3),
    "location": "View 3D > Object Mode > Tool Shelf",
    "blender": (3, 5, 0),
    "description": "Quickly enable or disable the 'Emulate 3rd Mouse Button' option.",
    "warning": "",
    "category": "System",
    }

class Emulate3ButtonMouseToggle(bpy.types.Operator):
    bl_idname = "view3d.emulate_3_button_mouse_toggle"
    bl_label = "Emulate 3 Button Mouse"
    
    def execute(self, context):
        prefs = context.preferences.inputs
        
        if prefs.use_mouse_emulate_3_button:
            prefs.use_mouse_emulate_3_button = False
        else:
            prefs.use_mouse_emulate_3_button = True
        
        return {'FINISHED'}

class Emulate3ButtonMousePanel3dView(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_emulate_3_button_mouse_panel"
    bl_label = "Emulate 3 Button Mouse"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'View'
    
    def draw(self, context):
        layout = self.layout
        
        if context.preferences.inputs.use_mouse_emulate_3_button:
            label = "Emulate 3 Button Mouse ON"
        else:
            label = "Emulate 3 Button Mouse OFF"
        
        layout.operator("view3d.emulate_3_button_mouse_toggle", text=label)
        
class Emulate3ButtonMousePanelNode(bpy.types.Panel):
    bl_idname = "NODE_PT_emulate_3_button_mouse_panel"
    bl_label = "Emulate 3 Button Mouse"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'View'
    
    def draw(self, context):
        layout = self.layout
        
        if context.preferences.inputs.use_mouse_emulate_3_button:
            label = "Emulate 3 Button Mouse ON"
        else:
            label = "Emulate 3 Button Mouse OFF"
        
        layout.operator("view3d.emulate_3_button_mouse_toggle", text=label)
        
        
class Emulate3ButtonMousePanelSQE(bpy.types.Panel):
    bl_idname = "SQE_PT_emulate_3_button_mouse_panel"
    bl_label = "Emulate 3 Button Mouse"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'View'
    
    def draw(self, context):
        layout = self.layout
        
        if context.preferences.inputs.use_mouse_emulate_3_button:
            label = "Emulate 3 Button Mouse ON"
        else:
            label = "Emulate 3 Button Mouse OFF"
        
        layout.operator("view3d.emulate_3_button_mouse_toggle", text=label)

def register():
    bpy.utils.register_class(Emulate3ButtonMouseToggle)
    bpy.utils.register_class(Emulate3ButtonMousePanel3dView)
    bpy.utils.register_class(Emulate3ButtonMousePanelNode)
    bpy.utils.register_class(Emulate3ButtonMousePanelSQE)

def unregister():
    bpy.utils.unregister_class(Emulate3ButtonMouseToggle)
    bpy.utils.unregister_class(Emulate3ButtonMousePanel3dView)
    bpy.utils.unregister_class(Emulate3ButtonMousePanelNode)
    bpy.utils.unregister_class(Emulate3ButtonMousePanelSQE)

if __name__ == "__main__":
    register()