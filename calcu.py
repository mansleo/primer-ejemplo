#import sysd
import ply.lex as lex


#Lista de tokens
tokens = ['NUMERO', 'SUM', 'RES', 'MUL', 'DIV', 'APAREN', 'CPAREN','PUNTO','COMA','EXPONENTE']


#Reglas de expresiones regulares para tokens simples
t_ignore = ' \t'
t_SUM    = r'\+'
t_RES    = r'-'
t_MUL    = r'\*'
t_DIV    = r'/'
t_APAREN = r'\('
t_CPAREN = r'\)'
t_PUNTO  =r'\.'
t_EXPONENTE=r'\E'
t_NUMERO = r'-?E?-?[1-9][0-9]*([.][1-9][0-9]*)?([E](-)?[1-9][0-9]*([.][1-9][0-9]*)?)?'




#Definicion de error que se va a mostrar cuando un caracter ingresado no es valido
def t_error(t):
	print("******Caracter no valido: {}".format(t.value[0]))
	t.lexer.skip(1)
	return t

lex.lex()


#Funcion para recibir la operacion a calcular y
#definir donde hay errores lexicos segun los caracteres ingresados
while True:
	try:
		s = raw_input('operacion > ')
	except EOFError:
		break
	if not s:
		continue


# Almacena la operacion en s
	lex.input(s)


# Muestra todos los tokens en la operacion
	while True:
		tok = lex.token()
		if not tok:
			break
		print(tok)
