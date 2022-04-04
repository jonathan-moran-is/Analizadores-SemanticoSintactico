import lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
    'GET',
    'CADENA',
    'RETURN',
    'VOID',
    'INT',
    'ENDL',
)
tokens = reservada + (
    'ID',
    'INT',
    'ASIGN',

    'ADD',
    'SUBSTRACT',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULE',

    'MINUSMINUS',
    'PLUSPLUS',

    #Condiones
    'IF',
    'IFNOT',
    #Ciclos
   'WHILE',
   'FOR',
    #logica
    'AND',
    'OR',
    'NOT',
    'LESSTHAN',
    'LESSEQUAL',
    'MORETHAN',
    'MOREEQUAL',
    'EQUAL',
    'NOTEQUAL',
    # Symbolos
    'NUMB',

    'PEFT',
    'PRIGHT',
    'BLEFT',
    'BRIGHT',
    'SBLEFT',
    'SBRIGHT',

    # Otros
    'SEMICOLON',
    'COMMA',
    'DCOMMA',
    'DLEFT', #<<
    'DRIGHT', #>>
)

# Reglas de Expresiones Regualres para token de Contexto simple

t_ADD = r'\+'
t_SUBSTRACT = r'-'
t_MINUSMINUS = r'\-\-'
# t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULE = r'\%'
t_POTENCIA = r'(\*{2} | \^)'
t_ASIGN = r'='
# Expresiones Logicas
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_LESSTHAN = r'<'
t_MORETHAN = r'>'
t_SEMICOLON = ';'
t_COMMA = r','
t_PLEFT = r'\('
t_PRIGHT = r'\)'
t_SBLEFT = r'\['
t_SBRIGHT = r'\]'
t_BLEFT = r'{'
t_BRIGHT = r'}'



def t_INCLUDE(t):
    r'include'
    return t

def t_USING(t):
    r'using'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_STD(t):
    r'std'
    return t

def t_COUT(t):
    r'cout'
    return t

def t_CIN(t):
    r'cin'
    return t

def t_GET(t):
    r'get'
    return t

def t_ENDL(t):
    r'endl'
    return t

def t_IFNOT(t):
    r'else'
    return t

def t_IF(t):
    r'if'
    return t

def t_RETURN(t):
   r'return'
   return t

def t_VOID(t):
   r'void'
   return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_STRING(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_NUM(t):
    r'\#'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_MOREEQUAL(t):
    r'>='
    return t

def t_EQUAL(t):
    r'=='
    return t

def t_DLEFT(t):
    r'<<'
    return t

def t_DRIGHT(t):
    r'>>'
    return t

def t_NOTEQUAL(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
     r'\/\/(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")
t_ignore =' \t'

def t_error( t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

file = open ('content.txt')

data = file.read()

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break

        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

analizador = lex.lex()

analizador.input(data)

while True:
    tok = analizador.token()
    prueba(data)
    if not tok:
        break
    print("---------------------------------------------------------------------------")
    print("                   RESULTADO DEL ANALIZADOR LEXICO")
    print("---------------------------------------------------------------------------")
    print(resultado_lexema)
    break
