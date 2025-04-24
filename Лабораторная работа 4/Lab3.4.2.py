import ifcopenshell

ifc_file = ifcopenshell.open("Sample model.ifc")

all_entities = ifc_file

print(f"Найдено элементов: {len(all_entities)}")

for all_entities in all_entities[:10]:  # Пример: вывод первых 10
    print(f"{all_entities} | GlobalId: {all_entities.GlobalId} | Name: {all_entities.Name}")