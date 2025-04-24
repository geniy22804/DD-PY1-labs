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
                    if hasattr(prop, "Name"):
                        prop_name = prop.Name
                        prop_value = prop.NominalValue.wrappedValue if hasattr(prop, "NominalValue") else None
                        element_data[prop_name] = prop_value

    data.append(element_data)

df = pd.DataFrame(data)
df.set_index("GlobalId", inplace=True)
df.columns = df.columns.str.lower().str.replace(' ', '_')

area_columns = [col for col in df.columns if 'площад' in col]

if area_columns:
    area_column = area_columns[0]
    df[area_column] = pd.to_numeric(df[area_column], errors='coerce')
    df['суммарная_площадь'] = df[area_column]
    print(f"Добавлен столбец 'суммарная_площадь' на основе '{area_column}'")
else:
    print("Не найден столбец, содержащий площадь.")

print(df[['type', 'name'] + (['суммарная_площадь'] if 'суммарная_площадь' in df.columns else [])].head())

