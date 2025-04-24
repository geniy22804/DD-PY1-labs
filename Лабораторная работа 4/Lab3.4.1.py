import ifcopenshell

# Путь к файлу IFC (укажите актуальный путь к файлу)
file_path = "Sample model.ifc"

ifc_file = ifcopenshell.open(file_path)

#вывод количества объектов в файле
print(f"Количество объектов в IFC-файле: {len(ifc_file)}")

#вывод информации о первых 5 объектах
for entity in ifc_file[:5]:
    print(entity)