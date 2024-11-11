import xml.etree.ElementTree as ET

try:
    tree = ET.parse('model.xmi')
    root = tree.getroot()
    ns = {'uml': 'http://www.omg.org/spec/UML/20090901'}

    # Dictionary to map class IDs to their names
    class_id_to_name = {}

    # Open the output file in write mode
    with open('model.use', 'w') as use_file:
        use_file.write("model ExtractedModel\n\n")

        # Extract Classes and write to the file
        for class_element in root.findall('.//uml:Class', ns):
            class_name = class_element.get('name')
            class_id = class_element.get('{http://www.omg.org/XMI}id')
            class_id_to_name[class_id] = class_name  # Map ID to class name

            use_file.write(f"class {class_name}\nattributes\n")
            
            # Extract Attributes and write to the file
            for attribute in class_element.findall('.//uml:Property', ns):
                attr_name = attribute.get('name')
                attr_type = attribute.get('type')
                if attr_type == "Float":
                    attr_type = "Real"  # Convert Float to Real for USE tool compatibility
                if attr_type is None:
                    attr_type = "Unknown"  # Handle cases where type is not specified
                use_file.write(f"  {attr_name}:{attr_type}\n")
            
            # Extract Operations and write to the file
            use_file.write("operations\n")
            for operation in class_element.findall('.//uml:Operation', ns):
                operation_name = operation.get('name')
                use_file.write(f"  {operation_name}()\n")
            
            use_file.write("end\n\n")

        # Extract Associations and write to the file
        use_file.write("-- associations\n\n")
        for association in root.findall('.//uml:Association', ns):
            assoc_id = association.get('{http://www.omg.org/XMI}id')
            member_ends = association.get('memberEnd')
            owned_ends = association.findall('uml:ownedEnd', ns)

            if member_ends and owned_ends:
                use_file.write(f"association Association_{assoc_id} between\n")
                for end in owned_ends:
                    end_type = end.get('type')
                    if end_type in class_id_to_name:
                        end_type_name = class_id_to_name[end_type]
                    else:
                        end_type_name = "UnknownClass"

                    lower_value = end.find('.//uml:lowerValue', ns)
                    upper_value = end.find('.//uml:upperValue', ns)
                    multiplicity = f"[{lower_value.get('value') if lower_value else '0'}..{upper_value.get('value') if upper_value else '*'}]"

                    # Generate a unique role name
                    role_name = f"role {end_type_name.lower()}Role"

                    # Write to file with correct indentation and format
                    use_file.write(f"  {end_type_name} {multiplicity} {role_name}\n")

                use_file.write("end\n\n")

        #use_file.write("end\n")

    print("Data successfully written in USE tool format to 'model.use'")

except ET.ParseError as e:
    print(f"Error parsing XML: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
