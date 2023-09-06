from main import array, create_array, sorted_array

def test_vetor_size():
  numbers = create_array()

  quantity = len(numbers)
  assert quantity == 20000