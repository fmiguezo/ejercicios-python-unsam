# canguros_buenos.py
# Ejercicio 9.11: Canguros buenos y canguros malos
#%%
class Canguro():
    def __init__(self, nombre, contenido_marsupio=None):
        self.nombre = nombre
        if contenido_marsupio == None:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido_marsupio
        
    def __str__(self):
        if self.contenido_marsupio == []:
            return f'{self.nombre}'
        else:
            s = ", ".join( [ object.__str__(objeto) for objeto in self.contenido_marsupio ] )
            return f'{self.nombre} tiene {s}'

    def meter_en_marsupio(self, objeto):
        self.contenido_marsupio.append(str(objeto))
         

def f_principal(argv):
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('Cangurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)
    print(madre_canguro)


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)




# # canguro_malo.py
# """Este código continene un 
# bug importante y dificil de ver
# """

# class Canguro:
#     """Un Canguro es un marsupial."""

#     def __init__(self, nombre, contenido=None): ## se cambia el default [] por None
#         ## ## El error está en el init, porque toma como valor default de contenido una lista vacía, 
#         # que se llena para todos los objetos de la clase Canguro cuando se ejecuta la función 
#         # 'meter_en_marsupio'
#         # hay que agregar un "if" que evalúe si al objeto le ingresamos contenido, si no es así, debe
#         # devolver una lista vacía
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """     
#         self.nombre = nombre
#         if contenido == None: ##si el valor de contenido para el objeto es None devuelve una lista vacía
#             self.contenido_marsupio = []
#         else: ## sino agrega el contenido de "contenido"
#             self.contenido_marsupio = contenido

#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [ self.nombre + ' tiene en su marsupio:' ]
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)