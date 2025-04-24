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

import matplotlib.pyplot as plt

# Убедимся, что нужные колонки существуют и приведены к нужному типу
if 'материал_несущих_конструкций' in df.columns and 'объем' in df.columns and 'type' in df.columns:
    df_filtered = df.dropna(subset=['материал_несущих_конструкций', 'объем', 'type']).copy()
    df_filtered['объем'] = pd.to_numeric(df_filtered['объем'], errors='coerce')

    # Группировка: по материалу и IFC-классу
    grouped = df_filtered.groupby(['материал_несущих_конструкций', 'type'])['объем'].sum().unstack(fill_value=0)

    # Построение stacked bar chart
    ax = grouped.plot(kind='bar', stacked=True, figsize=(12, 7), colormap='tab20')

    plt.title('Суммарный объем по материалам и IFC-классам элементов')
    plt.xlabel('Материал несущих конструкций')
    plt.ylabel('Объем (м³)')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend(title='IFC-Класс', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
else:
    print("Не найдены все необходимые столбцы: 'материал_несущих_конструкций', 'объем', 'type'.")





