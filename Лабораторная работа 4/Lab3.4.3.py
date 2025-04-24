import ifcopenshell
import pandas as pd

ifc_file = ifcopenshell.open("Sample model.ifc")

elements = ifc_file.by_type("IfcProduct")

data = []

for element in elements:
    element_data = {
        "GlobalId": element.GlobalId,
        "Type": element.is_a(),
        "Name": element.Name
    }

    for rel in getattr(element, "IsDefinedBy", []):
        if rel.is_a("IfcRelDefinesByProperties"):
            prop_set = rel.RelatingPropertyDefinition
            if prop_set.is_a("IfcPropertySet"):
                for prop in prop_set.HasProperties:
                    element_data[prop.Name] = prop.NominalValue.wrappedValue if hasattr(prop, "NominalValue") else None

    data.append(element_data)

df = pd.DataFrame(data)

print(df.head())