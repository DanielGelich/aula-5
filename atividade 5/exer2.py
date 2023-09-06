import array

def create_array():
  return array.array('i', range(1, 20001))

def is_sorted(array):
  array_list = list(array)
  return all(array_list[i] <= array_list[i + 1] for i in range(len(array_list) - 1))

array = create_array()


print(is_sorted(array))