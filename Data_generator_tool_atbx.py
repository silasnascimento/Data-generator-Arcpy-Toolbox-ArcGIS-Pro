import arcpy
import random

# Get the tool parameters
enclosing_polygon = arcpy.GetParameterAsText(0)
num_assignments = arcpy.GetParameter(1)
assignment_name = arcpy.GetParameterAsText(2)
min_tasks = arcpy.GetParameter(3)
max_tasks = arcpy.GetParameter(4)
min_geometries = arcpy.GetParameter(5)
max_geometries = arcpy.GetParameter(6)
min_parcels = arcpy.GetParameter(7)
max_parcels = arcpy.GetParameter(8)

# Set the path to the geodatabase file
geodatabase_path = r"D:\QGIS_db\UpWork\Ronda B\Data_Generator_Tool\Data_Generator_Tool.gdb"

# Create the Feature Dataset "Process_DataGen"
feature_dataset_name = "Process_DataGen"
feature_dataset_path = arcpy.CreateFeatureDataset_management(geodatabase_path, feature_dataset_name).getOutput(0)

# Divide the polygon into single parts
subdivided_polygons = arcpy.management.SubdividePolygon(enclosing_polygon, "in_memory/subdivided_polygons", "NUMBER_OF_EQUAL_PARTS", num_areas=num_assignments)


# Create the "VegAssignment" layer inside the Feature Dataset
veg_assignment_layer = arcpy.management.CopyFeatures(subdivided_polygons, feature_dataset_path + "/VegAssignment_layer")
arcpy.management.AddField(veg_assignment_layer, "NAME", "TEXT")
arcpy.management.CalculateField(veg_assignment_layer, "NAME", "'Name other test'", "PYTHON")


# Choose a random number for the number of tasks
num_tasks = random.randint(min_tasks, max_tasks)
num_geometries = random.randint(min_geometries, max_geometries)
num_parcels = random.randint(min_parcels, max_parcels)

# Divide the polygon into single parts to create the "VegTask" layer
veg_task_layer = arcpy.management.SubdividePolygon(enclosing_polygon, "in_memory/veg_task_layer", "NUMBER_OF_EQUAL_PARTS", num_areas=num_tasks)
veg_task_layer_output = arcpy.management.CopyFeatures(veg_task_layer, feature_dataset_path + "/VegTask_layer")

# Divide the polygon into single parts to create the "TaskParcel" layer
task_parcel_layer = arcpy.management.SubdividePolygon(enclosing_polygon, "in_memory/task_parcel_layer", "NUMBER_OF_EQUAL_PARTS", num_areas=num_parcels)
task_parcel_layer_output = arcpy.management.CopyFeatures(task_parcel_layer, feature_dataset_path + "/TaskParcel_layer")

# Divide the polygon into single parts to create the "VegTaskPoly" layer
veg_task_poly_layer = arcpy.management.SubdividePolygon(enclosing_polygon, "in_memory/veg_task_poly_layer", "NUMBER_OF_EQUAL_PARTS", num_areas=num_geometries)
veg_task_poly_layer_output = arcpy.management.CopyFeatures(veg_task_poly_layer, feature_dataset_path + "/VegTaskPoly_layer")

# Convert polygons to points to create the "VenTask Point" layer
veg_task_point_layer = arcpy.management.FeatureToPoint(veg_task_poly_layer, "in_memory/veg_task_point_layer")
veg_task_point_layer_output = arcpy.management.CopyFeatures(veg_task_point_layer, feature_dataset_path + "/VegTaskPoint_layer")

# Convert polygons to lines to create the "VegTaskLine" layer
veg_task_line_layer = arcpy.management.FeatureToLine(veg_task_poly_layer, "in_memory/veg_task_line_layer")
veg_task_line_layer_output = arcpy.management.CopyFeatures(veg_task_line_layer, feature_dataset_path + "/VegTaskLine_layer")

# Delete the temporary memory layers
arcpy.management.Delete("in_memory")

#Append
arcpy.env.workspace = "D:/QGIS_db/UpWork/Ronda B/Data_Generator_Tool/Data_Generator_Tool.gdb"
VegAssignment = "VegAssignment"
VegTask = "VegTask"
TaskParcel = "TaskParcel"
VegTaskPoly = "VegTaskPoly"
VegTaskPoint = "VegTaskPoint"
VegTaskLine = "VegTaskLine"


arcpy.management.Append(veg_assignment_layer, VegAssignment, "NO_TEST")
arcpy.management.Append(veg_task_layer_output, VegTask, "NO_TEST")
arcpy.management.Append(task_parcel_layer_output, TaskParcel, "NO_TEST")
arcpy.management.Append(veg_task_poly_layer_output, VegTaskPoly, "NO_TEST")
arcpy.management.Append(veg_task_point_layer_output, VegTaskPoint, "NO_TEST")
arcpy.management.Append(veg_task_line_layer_output, VegTaskLine, "NO_TEST")

#Calculate Field
#expression = f"'{assignment_name}'"
#fieldname = "NAME"
#arcpy.management.AddField(VegAssignment, "NAME", "TEXT")
#arcpy.management.CalculateField(VegAssignment, "NAME", "'Name test'", "PYTHON")

# Display the completion message
arcpy.AddMessage("Process completed successfully!")