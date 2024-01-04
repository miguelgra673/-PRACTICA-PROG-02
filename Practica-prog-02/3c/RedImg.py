# Haz un programa que le pida al usuario un nombre de imagen, la cargue y, si existe, le pida
# continuamente tamaños a los que la quiera escalar (ancho y alto), y guarde una copia de la imagen
# original con ese tamaño. El nombre de cada imagen escalada tendrá el patrón
# ancho_alto_nombreFicheroOriginal. El proceso terminará cuando el usuario ponga la anchura o altura a
# 0.


from PIL import Image
import os

def redimensionar_imagen(imagen, ancho, alto, nombre_original):
    nueva_imagen = imagen.resize((ancho, alto))
    nuevo_nombre = f"{ancho}_{alto}_{nombre_original}"
    nueva_imagen.save(nuevo_nombre)
    print(f"Imagen redimensionada y guardada como {nuevo_nombre}")

def main():
    nombre_imagen = input("Introduce el nombre de la imagen (con la extensión): ")

    if not os.path.isfile(nombre_imagen):
        print(f"Error: La imagen {nombre_imagen} no existe.")
        return

    imagen_original = Image.open(nombre_imagen)

    while True:
        try:
            ancho = int(input("Introduce el nuevo ancho (0 para salir): "))
            if ancho == 0:
                break

            alto = int(input("Introduce el nuevo alto (0 para salir): "))
            if alto == 0:
                break

            redimensionar_imagen(imagen_original, ancho, alto, os.path.splitext(nombre_imagen)[0])

        except ValueError:
            print("Error: Debes introducir un valor numérico.")

if __name__ == "__main__":
    main()
