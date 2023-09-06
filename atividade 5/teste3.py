def test_converter_massa_lunar():
  massa_terrestre = 10
  massa_lunar_esperada = 1.6666666666666667
  massa_lunar_obtida = converter_massa_lunar(massa_terrestre)

  assert massa_lunar_obtida == massa_lunar_esperada


def test_converter_distancia_marte():
  distancia_terrestre = 1000
  distancia_marte_esperada = 1028
  distancia_marte_obtida = converter_distancia_marte(distancia_terrestre)

  assert distancia_marte_obtida == distancia_marte_esperada