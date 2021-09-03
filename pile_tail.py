# >>>Victor Andres Barilin<<<
class Tail():
    def __init__(self):
        self.tail = []
        self.length_tail = 0
    
    def add_tail(self, element):
        # agrego elemento a la lista e incremento el contador
        self.tail.append(element)
        self.length_tail += 1
    
    def quit_tail(self):
        # consulto para conocer si aun hay elementos
        if (self.length_tail > 0):
            res = self.tail.pop(0)
            self.length_tail -= 1 
        #en caso de no tener elementos reinicio la lista y la variable que almacena la longitud
        else:
            res = 'No hay datos en la cola'
            self.tail = []
            self.length_tail = 0
        return res
    
    # este metodo fue usado para desarrollo pero no me parecio mal dejarlo en la entrega ya que puede ser de utilidad para desarrollar
    def see_tail(self):
        return self.tail

class Pile():
    def __init__(self):
        self.pile = []
        self.length_pile = -1
    
    def add_pile(self, element):
        # agrego elemento a la lista e incremento el contador
        self.pile.append(element)
        self.length_pile += 1

    def quit_pile(self):
        # consulto para conocer si aun hay elementos
        if self.length_pile >= 0:
            res = self.pile.pop(self.length_pile)
            self.length_pile -= 1
        #en caso de no tener elementos reinicio la lista y la variable que almacena la longitud
        else:
            res = 'No hay datos en la pila'
            self.pile = []
            self.length_pile = -1
        
        return res
    
    # este metodo fue usado para desarrollo pero no me parecio mal dejarlo en la entrega ya que puede ser de utilidad para desarrollar
    def see_pile(self):
        return self.pile

# print('----PRUEBA DE PILAS----')
# # instancio una pila
# pile = Pile()
# # cargo elementos en la pila
# pile.add_pile('pepe')
# pile.add_pile(3)
# pile.add_pile(2.8)
# # muestro elementos
# print(pile.see_pile())
# # quito un elemento
# print(pile.quit_pile())
# # muestro elementos
# print(pile.see_pile())

# # separador
# print('-------------------')

# print('----PRUEBA DE COLA----')
# #  instancio una cola
# tail = Tail()
# # cargo elementos en la cola
# tail.add_tail('pepe')
# tail.add_tail(3)
# tail.add_tail(2.8)
# # muestro elementos
# print(tail.see_tail())
# # quito un elemento
# print(tail.quit_tail())
# # muestro elementos
# print(tail.see_tail())