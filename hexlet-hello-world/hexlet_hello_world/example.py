from more_itertools import collapse, chunked

# Пример flattening (свертки) вложенных структур
nested_data = [1, [2, 3], [4, [5, 6]]]
flat = list(collapse(nested_data))

# Пример разбиения на чанки
numbers = range(1, 11)
chunks = list(chunked(numbers, 3))

print(f"Hello from python project!")
print(f"Flattened data: {flat}")
print(f"Chunked data: {chunks}")
