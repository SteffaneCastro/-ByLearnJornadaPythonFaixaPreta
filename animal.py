# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vZ63vPRVnLtgPtq2Ns2sR_Vghl37IvbQ
"""

animais = []

animal = input("Digite o nome do seu animal de estimação ou digite 0 se não tiver nenhum:")

while animal != '0':
    especie = input("Digite a Espécie desse animal: ")
    animais.append([animal, especie])
    animal = input('Se tiver mais animais, digite o nome dele. Ou digite 0 se não tiver: ')

if len(animais) == 0:
  print("\n\nVocê tem os seguintes animais:")
  for animal in animais:
      print(" - nome:", animal[0], "| Espécie:", animal[1])

