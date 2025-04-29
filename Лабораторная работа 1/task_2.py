# TODO Найдите количество книг, которое можно разместить на дискете
Disk_size = 1.44
Disk_size_in_bytes = Disk_size * 1024**2
Lists = 100
clean_lines = 50
symbols = 25
one_symbol_size = 4

Books = Disk_size_in_bytes/(Lists * clean_lines * symbols * one_symbol_size)
print("Количество книг, помещающихся на дискету:", round(Books,))
