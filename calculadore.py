# >>>Victor Andres Barilin<<<
from pile_tail import Tail

def op_pre_pos(cola, op):
    val = float(cola.quit_tail())
    val1 = ''
    if op == '+':
        while val != 'No hay datos en la cola' and val1 != 'No hay datos en la cola':
            val1 = cola.quit_tail()

            if val1 != 'No hay datos en la cola':
                val += float(val1)

        return val
    elif op == '-':
        while val != 'No hay datos en la cola' and val1 != 'No hay datos en la cola':
            val1 = cola.quit_tail()

            if val1 != 'No hay datos en la cola':
                val -= float(val1)

        return val
    elif op == '*':
        while val != 'No hay datos en la cola' and val1 != 'No hay datos en la cola':
            val1 = cola.quit_tail()

            if val1 != 'No hay datos en la cola':
                val *= float(val1)

        return val
    elif op == '/':
        while val != 'No hay datos en la cola' and val1 != 'No hay datos en la cola':
            val1 = cola.quit_tail()

            if val1 != 'No hay datos en la cola':
                val /= float(val1)

        return val
        
def op_infija(val1, val2, op):
    if op == '*':
        return val1 * val2
    elif op == '/':
        return val1 / val2

def notation(string):
    # quito los espacios que pueda tener el string para revisar al inicio y al final en busca de operaciones, lo que indicara si esta es (prefija, infija, postfija)
    string = string.strip()

    init = string[: 2]
    end = string[-2 :]
    
    if init in '/ ' or init in '* ' or init in '+ ' or init in '- ' :
        return 'prefija'

    elif end in ' /' or end in ' *' or end in ' +' or end in ' -' :
        return 'postfija'

    else:
        return 'infija'

def div_mult (posi_op, op_current, op):
    # obtengo los 2 numeros a los que se les aplicara la operacion (/*) a partir de la posicion de la operacion
    val1 = op_current[op_current.rfind(' ', 0,posi_op-1)+1 : posi_op-1]
    val2 = op_current[posi_op+2 : op_current.find(' ',posi_op+2)]
    
    # realizo la operacion y la reincorporo al fragmento en el lugar correspondiente para retornar el fragmento completo
    res = op_infija(float(val1), float(val2), str(op))
    op_current = op_current[: op_current.rfind(' ', 0,posi_op-1)+1] + str(res) + op_current[op_current.find(' ',posi_op+2) :]

    return op_current
        
def calculation(string, notacion):
    # quioto espacios que puedan existir al inicio o final del string 
    string = string.strip()
    # coloco parentesis para poder manejarlo con mi metodo
    string =  '( ' + string + ' )'

    if '(' in string:
        while '(' in string:

            # reviso cual es el ultimo parentesis abierto y a partir de ahi busco el siguiente cerrado
            posi_i = string.rfind('(')
            posi_f = string.find(')', posi_i)

            # cuando tengo las 2 posiciones puedo obtener el fragmento con mas privilegio de la operacion "op_current"
            op_current = string[posi_i+1 : posi_f]

            # reviso si hay operaciones para realizar en op op_current
            while('/' in op_current) or ('*'in op_current) or (' + ' in op_current) or (' - ' in op_current):
                if notacion == 'infija':

                    #controlo si el fragmento de operacion contiene divicion o multiplicacion 
                    if '*'in op_current or'/' in op_current:
                        #si contiene alguna de estas operaciones corrobora cual se encuentra primero / existente
                        mult = op_current.find('*')
                        div = op_current.find('/')

                        
                        #en caso de existir ambas operaciones o mas de una las realiza de izquierda a derecha
                        if mult != -1 and div != -1:
                            if mult > div:
                                op_current = div_mult(div, op_current, '/')

                            elif mult < div:
                                op_current = div_mult(mult, op_current, '*')

                        elif mult != -1 and div == -1:
                            op_current = div_mult(mult, op_current, '*')
                        
                        elif mult == -1 and div != -1:
                            op_current = div_mult(div, op_current, '/')
                            
                    # cuando en el fragmento solo se encuentren sumas y restas lo resuelvo de la siguiente manera...
                    else:
                        # instancio una cola y le ingreso todos los valores que contenga el fragmento
                        cola = Tail()
                        op_list = op_current.split()
                        for i in op_list:
                            cola.add_tail(i)
                        
                        op = ''
                        val = float(cola.quit_tail())
                        # le otorgo un valor inicial a las variables antes de entrar el loop

                        while op != 'No hay datos en la cola':
                            # esta se ejecutara por unica vez al inicio del loop para optener una operacion
                            if op == '':
                                op = cola.quit_tail()
                            
                            # val1 es el valor que se sumara o restara a val
                            val1 = cola.quit_tail()

                            # corroboro si la lista aun tiene elementos
                            if op != 'No hay datos en la cola' and val1 != 'No hay datos en la cola':
                                if op == '+':
                                    val += float(val1)
                                    
                                elif op == '-':
                                    val -= float(val1)
                                # antes de reiniciar el loop extraigo el proximo valor de operacion el cual podria terminar con el loop en caso de no haber mas valores
                                op = cola.quit_tail()
                        
                        # le doy el valor final al fragmento antes de reincorporarlo al string para volver a iniciar el loop principal en caso de tener parentesis
                        op_current = str(val)
                
                elif notacion == 'prefija':
                        cola = Tail()
                        op_list = op_current.split()

                        for i in op_list:
                            cola.add_tail(i)
                        
                        op = cola.quit_tail()
                        op_current = str(op_pre_pos(cola, op))
                        
                elif notacion == 'postfija':
                    cola = Tail()
                    op_list = op_current.split()
                    op = op_list.pop(-1)
                    for i in op_list:
                        cola.add_tail(i)
                    
                    op_current = str(op_pre_pos(cola, op))

            op_current = op_current.strip()
            string = string[: posi_i] + op_current + string[posi_f + 1 :]

    return string

#prueba de desarrollo
# inicio de app    
#print('ingrese la operacion con espacios para separar los elementos: ')
#operacion = input('> ')
#operacion = '/ ( - 2 4 9 ) ( * 9 3 )' #prefija
#operacion = '( 2 - 4 - 9 ) / ( 9 * 3 )' #infija
#operacion = '( 2 4 9 - ) ( 9 3 * ) /' #postfija
# try:
#     notacion = notation(operacion)
#     res = str(calculation(operacion , notacion))
#     if res == 'None':
#         print('Es posible que olvidara un espacio...')
#     else:
#         print('notacion:',notacion)
#         print('resultado:',res)
# except :
#     print('ERROR. corrobore que la sintaxis es correcta')
