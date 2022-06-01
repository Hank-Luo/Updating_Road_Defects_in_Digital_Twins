import pyvista as pv
mesh = pv.read("Data/Feb9,full_scan/textured.obj")
mesh.texture_map_to_plane(inplace=True)
tex = pv.read_texture("Data/Feb9,full_scan/orthographic_new_flipped.png")
mesh.plot(texture=tex)

"""
import ifcopenshell
import uuid
model = ifcopenshell.open("../Data/test.ifc")
project = model.by_type("IfcSlab")
prop_set_guid = ifcopenshell.guid.compress(uuid.uuid1().hex)
property_values = [model.createIfcPropertySingleValue("Potholes", "Bounding boxes for potholes", model.create_entity("IfcText", "[[(1,1),(0,0),(1,0)]]"), None)]
property_set = model.createIfcPropertySet(prop_set_guid, project[0].OwnerHistory, "RoadDefectInformation", None, property_values)
rel_guid = ifcopenshell.guid.compress(uuid.uuid1().hex)
model.createIfcRelDefinesByProperties(rel_guid, project[0].OwnerHistory, None, None, [project[0]], property_set)
model.write("../Data/properties_added.ifc") 

import ast
model = ifcopenshell.open("../Data/properties_added.ifc")
project = model.by_type("IfcSlab")
for product in project:
  definitions = product.IsDefinedBy
  for definition in definitions:
    property_definition = definition.RelatingPropertyDefinition
    print(property_definition.HasProperties[0])
    print(property_definition.HasProperties[0].NominalValue[0])
    # list_of_bounding_boxes = property_definition.HasProperties[0].NominalValue[0].strip("[]").split(", ")
    list_of_bounding_boxes = ast.literal_eval(property_definition.HasProperties[0].NominalValue[0])
    print(list_of_bounding_boxes[0])
    # print(list_of_bounding_boxes[0].strip("()").split(","))
    print(list_of_bounding_boxes[0][0])

import cv2
img = cv2.imread("orthographic_new_flipped.png")
crop_img = img[min(list_of_bounding_boxes[0], key=lambda x:x[0]):max(list_of_bounding_boxes[0], key=lambda x:x[0]), min(list_of_bounding_boxes[0], key=lambda x:x[1]):max(list_of_bounding_boxes[0], key=lambda x:x[1])]
cv2.imshow("cropped", crop_img)
"""