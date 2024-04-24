class Biblioteca:
    def __init__(self):
        self.libros = {}

    def añadir_libro(self, titulo, autor):
        self.libros[titulo] = autor
        print(f"Libro añadido: {titulo} por {autor}")

    def remover_libro(self, titulo):
        if titulo in self.libros:
            del self.libros[titulo]
            print(f"Libro removido: {titulo}")
        else:
            print("El libro no existe en la biblioteca.")

    def buscar_libro(self, titulo):
        if titulo in self.libros:
            print(f"Libro encontrado: {titulo} por {self.libros[titulo]}")
        else:
            print("Libro no encontrado.")

# Uso de la clase Biblioteca
biblioteca = Biblioteca()
biblioteca.añadir_libro("Cien años de soledad", "Gabriel García Márquez")
biblioteca.añadir_libro("1984", "George Orwell")
biblioteca.buscar_libro("1984")
biblioteca.remover_libro("Cien años de soledad")
