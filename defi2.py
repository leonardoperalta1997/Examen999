
def contar_vocales(palabra):
  
  contador = 0
  
  palabra = palabra.lower()
  
  for letra in palabra:
    
    if letra in "aeiou":
      contador += 1
 
  return contador


palabra = input("Ingrese una palabra: ")

vocales = contar_vocales(palabra)

print(f"La palabra {palabra} tiene {vocales} vocales.")
