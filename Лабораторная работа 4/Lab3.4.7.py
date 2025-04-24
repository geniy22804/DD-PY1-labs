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

df.set_index("GlobalId", inplace=True)

df.columns = df.columns.str.lower().str.replace(' ', '_')

print(df.head())
df.info()

import matplotlib.pyplot as plt

if 'материал_несущих_конструкций' in df.columns and 'объем' in df.columns:
    df_filtered = df.dropna(subset=['материал_несущих_конструкций', 'объем'])

    df_filtered['объем'] = pd.to_numeric(df_filtered['объем'], errors='coerce')

    grouped = df_filtered.groupby('материал_несущих_конструкций')['объем'].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    grouped.plot(kind='bar', color='teal')
    plt.title('Суммарный объем по материалам несущих конструкций')
    plt.xlabel('Материал')
    plt.ylabel('Объем (м³)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()
else:
    print("Колонки 'материал_несущих_конструкций' и/или 'объем' отсутствуют в DataFrame.")

