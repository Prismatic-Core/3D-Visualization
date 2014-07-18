from bpy import *
import bpy, random
import csv
import os
import math
import re

class DataVisTool(bpy.types.Panel):
    bl_label = "Data Visualization"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    
        
    def draw(self, context):
        layout = self.layout 
               
        scn = context.scene 
        
        
        row =layout.row()      
        row.prop(scn, "obj_name")
        row =layout.row()
        row.label("------------------------------------------------------------------")
        layout.label("Generate your data")
        row = layout.row()
        row.operator("", text="")
        row = layout.row()
        row.operator( "generate3.data" ) 
        row = layout.row()
        row.operator( "generate4.data" ) 
        row = layout.row()
        row.operator( "generate5.data" ) 
        
        row =layout.row()
        row.label("------------------------------------------------------------------") 
        row =layout.row()
        layout.label("Edit Object")
        row =layout.row()
        row.alignment = 'LEFT'
        row.operator("redmore.button")
        row.alignment = 'CENTER'
        row.operator("redless.button")
        row = layout.row()
        row.alignment = 'LEFT'
        row.operator("greenmore.button")
        row.alignment = 'CENTER'
        row.operator("greenless.button")
        row = layout.row()
        row.alignment = 'LEFT'
        row.operator("bluemore.button")
        row.alignment = 'CENTER'
        row.operator("blueless.button")
        row = layout.row()
        row = layout.row()
        row.operator( "random.button" ) 
        
        
        
######## End of Interface #######################
        
                
class setFourElements(bpy.types.Operator):
    bl_idname ='4.elements'
    bl_label ='4'
    bl_description ='Four variables used per object'
    
    def execute(self, context):
        varObject = 4
        return{'FINISHED'}
    
class RandomButton(bpy.types.Operator):
    bl_idname = "random.button"
    bl_label = "Randomize Color"
 
    def execute(self, context):
         mat = context.object.data.materials[0]
         for i in range(3):
             mat.diffuse_color[i] = random.random()
         return{'FINISHED'} 
     
class RedMoreButton(bpy.types.Operator):
    bl_idname = "redmore.button"
    bl_label = "Red +"
 
    def execute(self, context):
         mat = context.object.data.materials[0]
         for i in range(1):
             mat.diffuse_color[0] += .075
         return{'FINISHED'}
      
class RedLessButton(bpy.types.Operator):
    bl_idname = "redless.button"
    bl_label = "Red -"
 
    def execute(self, context):
         mat = context.object.data.materials[0]
         for i in range(1):
             mat.diffuse_color[0] -= .075
         return{'FINISHED'}
   
class BlueMoreButton(bpy.types.Operator):
    bl_idname = "bluemore.button"
    bl_label = "Blue +"
 
    def execute(self, context):
         mat = context.object.data.materials[0]
         for i in range(1):
             mat.diffuse_color[2] += .075
         return{'FINISHED'}
     
class BlueLessButton(bpy.types.Operator):
    bl_idname = "blueless.button"
    bl_label = "Blue -"
 
    def execute(self, context):
         mat = context.object.data.materials[0]
         for i in range(1):
             mat.diffuse_color[2] -= .075
         return{'FINISHED'}
     
class GreenMoreButton(bpy.types.Operator):
    bl_idname = "greenmore.button"
    bl_label = "Green +"
 
    def execute(self, context):
         mat = context.object.data.materials[0]
         for i in range(1):
             mat.diffuse_color[1] += .075
         return{'FINISHED'}
     
class GreenLessButton(bpy.types.Operator):
    bl_idname = "greenless.button"
    bl_label = "Green -"
 
    def execute(self, context):
         mat = context.object.data.materials[0]
         for i in range(1):
             mat.diffuse_color[1] -= .075
         return{'FINISHED'}

     
################### 3 Variables ###################### 

class ThreeDataVis(bpy.types.Operator):
    bl_idname ='generate3.data'
    bl_label ='Generate from dataset using 3 var'
    bl_description ='Data will be used to generate a 3D visualization'
    
    def execute(self, context):
        
        file=open('\\compareGas.csv', 'r+')
        listme=file.read() #List that will take in everything from csv
        count = 0 #counter
        listme = re.sub('\n', ',', listme)#clean out soft returns (\n)
        
        exValues = [0] #new list to extract values from csv
        
        exValues = listme.split(',')
        
        objColorRand1 = random.random()
        objColorRand2= random.random()
        objColorRand3 = random.random()  
         
        while (count + 3) <= (len(exValues)):#creating sphere objects from read data
         x = float(exValues[count])
         x = x+ 1 #modified for compareGas.csv
         count += 1
         y = float(exValues[count])
         count += 1
         z = float(exValues[count])
         z = z *3 #modified for file
         count += 0
         r = float(exValues[count])
         count += 1
         objColorFinish = float(exValues[count])
         objColorFinish = (objColorFinish / 36)
         #count += 1
         q = (r / 3.1415) #reduce scale of radius for visibility, can be altered
         q = math.sqrt(q)
         r = q / 2
         
         
         newObj = bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=1, view_align=False, enter_editmode=False, location=(x, y, z), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
         bpy.ops.transform.resize(value=(r, r, r), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
         ##########color objects######
         objColor = bpy.data.materials.new('Obj Material')
         objColor.diffuse_color = .05, .05, .05 #simple default
         newObj = bpy.context.active_object
         mesh = newObj.data
         mesh.materials.append(objColor)
         newObj = context.object.data.materials[0]
         for i in range(1):            
             newObj.diffuse_color = objColorFinish - objColorRand1, objColorFinish -objColorRand2, objColorFinish - objColorRand3
            
         #Object finished, returned to while
        file.close()
        #End of generating objects
        return{'FINISHED'}
    
####### 4 Variables ###############
    
class FourDataVis(bpy.types.Operator):
    bl_idname ='generate4.data'
    bl_label ='Generate from dataset using 4 var'
    bl_description ='Data will be used to generate a 3D visualization'
    
    def execute(self, context):
        
        file=open('\\BestJobs.csv', 'r+')
        listme=file.read() #List that will take in everything from csv
        count = 0 #counter
        listme = re.sub('\n', ',', listme)#clean out soft returns (\n)
        
        exValues = [0] #new list to extract values from csv
        
        exValues = listme.split(',')
        objColorRand1 = random.random()
        objColorRand2= random.random()
        objColorRand3 = random.random() 
         
        while (count + 4) <= (len(exValues)):#creating sphere objects from read data
         x = float(exValues[count])
         x = x / 10000
         count += 1
         y = float(exValues[count])
         count += 1
         z = 1 #float(exValues[count])
         #count += 1
         r = float(exValues[count])
         count += 1
         objColorFinish =  float(exValues[count])
         objColorFinish = (objColorFinish / 5)
         objColorFinish = objColorFinish * 1.25 # modified for bestjobs
         count += 1
         q = (r / 3.1415) #reduce scale of radius for visibility, can be altered
         q = math.sqrt(q)
         r = q
         r = r / 80
         
         newObj = bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=1, view_align=False, enter_editmode=False, location=(x, y, z), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
         bpy.ops.transform.resize(value=(r, r, r), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
         #color objects
         objColor = bpy.data.materials.new('Obj Material')
         objColor.diffuse_color = .05, .05, .05 #simple default
         newObj = bpy.context.active_object
         mesh = newObj.data
         mesh.materials.append(objColor)
         objColor.diffuse_color = objColorFinish - objColorRand1, objColorFinish -objColorRand2, objColorFinish - objColorRand3
         #Object finished, returned to while
        file.close()
        #End of generating objects
        return{'FINISHED'}
    
####### 5 Variables ######################

class FiveDataVis(bpy.types.Operator):
    bl_idname ='generate5.data'
    bl_label ='Generate from dataset using 5 var'
    bl_description ='Data will be used to generate a 3D visualization'
    
    def execute(self, context):
        
        file=open('\\TopGamedataset.csv', 'r+')
        
        
        listme=file.read() #List that will take in everything from csv
        count = 0 #counter
        listme = re.sub('\n', ',', listme)#clean out soft returns (\n)
        
        exValues = [0] #new list to extract values from csv
        
        exValues = listme.split(',')
        
        objColorRand1 = random.random()
        objColorRand2= random.random()
        objColorRand3 = random.random()        
         
        while (count + 5) <= (len(exValues)):#creating sphere objects from read data
         x = float(exValues[count])
         count += 1
         y = float(exValues[count])
         count += 1
         z = float(exValues[count])
         z = z /2
         count += 1
         r = float(exValues[count])
         count += 1
         objColorFinish = float(exValues[count])
         objColorFinish = (objColorFinish / 10) 
         count += 1
         q = (r / 3.1415) #reduce scale of radius for visibility, can be altered
         q = math.sqrt(q)
         r = q / 2
         
         
         newObj = bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=1, view_align=False, enter_editmode=False, location=(x, y, z), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
         bpy.ops.transform.resize(value=(r, r, r), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
         #color objects
         objColor = bpy.data.materials.new('Obj Material')
         objColor.diffuse_color = .05, .05, .05 #simple default
         newObj = bpy.context.active_object
         mesh = newObj.data
         mesh.materials.append(objColor)
         objColor.diffuse_color = (objColorFinish - objColorRand1) * -1, (objColorFinish -objColorRand2) * -1, (objColorFinish - objColorRand3) * -1
         #Object finished, returned to while
        file.close()
        #End of generating objects
        return{'FINISHED'}  

bpy.utils.register_module(__name__)
