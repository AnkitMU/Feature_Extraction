import xml.etree.ElementTree as ET

try:
    tree = ET.parse('model.xmi')
    root = tree.getroot()
    ns = {'uml': 'http://www.omg.org/spec/UML/20090901'}

    # Extract Classes 
    for class_element in root.findall('.//uml:Class', ns):
        class_name = class_element.get('name')
        print(f"Class: {class_name}")

        # Extract Attributes 
        for attribute in class_element.findall('.//uml:Property', ns):
            attr_name = attribute.get('name')
            attr_type = attribute.get('type')
            print(f"{attr_name}:{attr_type}")

        # Extract Operations 
        for operation in class_element.findall('.//uml:Operation', ns):
            operation_name = operation.get('name')
            print(f"  Operation: {operation_name}")

   # print("\nAssociations and Multiplicities:")

    for association in root.findall('.//uml:Association', ns):
        assoc_id = association.get('{http://www.omg.org/XMI}id')  
        member_ends = association.get('memberEnd')

        print(f"Association ID: {assoc_id}")

        
        if member_ends:
            member_classes = member_ends.split()
            print(f"  Connected Classes: {member_classes}")

        
        for owned_end in association.findall('uml:ownedEnd', ns):
            end_type = owned_end.get('type')
            lower_value = owned_end.find('.//uml:lowerValue', ns)
            upper_value = owned_end.find('.//uml:upperValue', ns)

           
            lower = lower_value.get('value') if lower_value is not None else '0'
            upper = upper_value.get('value') if upper_value is not None else '*'

            print(f"  Class: {end_type}, Multiplicity: {lower}..{upper}")

except ET.ParseError as e:
    print(f"Error parsing XML: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

