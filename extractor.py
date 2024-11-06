import xml.etree.ElementTree as ET
try:
    tree = ET.parse('model.xmi')
    root = tree.getroot()

    ns = {'uml': 'http://www.omg.org/spec/UML/20090901'}

    for class_element in root.findall('.//uml:Class', ns):
        class_name = class_element.get('name')
        print(f"Class: {class_name}")

        for attribute in class_element.findall('.//uml:Property', ns):
            attr_name = attribute.get('name')
            attr_type = attribute.get('type')
            print(f"{attr_name}:{attr_type}")

except ET.ParseError as e:
    print(f"Error parsing XML: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
