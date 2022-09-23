# torre_control.py
# Ejercicio 9.12: Torre de Control

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0



class TorreDeControl(Cola):
    def __init__(self):
        self.items = []
        self.items_con_prioridad = []

    def nuevo_arribo(self, x):
        self.items_con_prioridad.append(x)
    
    def nueva_partida(self, x):
        self.items.append(x)

    def asignar_pista(self):
        if len(self.items_con_prioridad) != 0:
            print(f'El vuelo {self.items_con_prioridad[0]} aterrizó con éxito')
            self.items_con_prioridad.pop(0)
        else:
            if self.esta_vacia():
                print('No hay vuelos en espera.') 
            else:
                print(f'El vuelo {self.items[0]} despegó con éxito')
                self.items.pop(0)

    def ver_estado(self):
        v_aterrizar = ", ".join( [ vuelo for vuelo in self.items_con_prioridad ] )
        v_despegar = ", ".join( [ vuelo for vuelo in self.items ] )
        print(f'Vuelos esperando para aterrizar: {v_aterrizar}\nVuelos esperando para despegar: {v_despegar}')



def main():
    import torre_control
    torre = torre_control.TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    torre.ver_estado()
    torre.asignar_pista()
    torre.asignar_pista()
    torre.asignar_pista()
    torre.asignar_pista()