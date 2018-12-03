import random

exercicios=[
    {'pergunta1': "Qual a equação da reta que passa pelos pontos (2, 3) e (4, 5 )?"
        , 'pergunta2':''
        , '1': {'texto': 'y = x + 2', '?': 2}
        , '2': {'texto': 'y = x + 1', '?': 1}
        , '3': {'texto': 'y = x', '?': 2}
        , '4': {'texto': 'y = x + 4', '?': 2}
        , '5': {'texto': 'y = x + 3', '?': 2}},
    {'pergunta1': "Dado os pontos (2, -1) e (5, -13) qual a equação da reta?"
        , 'pergunta2':''
        , '1': {'texto': 'y = 4x - 7', '?': 2}
        , '2': {'texto': 'y = -7x + 4', '?': 2}
        , '3': {'texto': 'y = 7x + 4', '?': 2}
        , '4': {'texto': 'y = -4x + 7', '?': 1}
        , '5': {'texto': 'y = 4x + 7', '?': 2}},
    {'pergunta1': "Seja a função definida por f(x) = 3x-2:"
        , 'pergunta2':'determine o valor de f(5)+f(0)'
        , '1': {'texto': '11', '?': 1}
        , '2': {'texto': '12', '?': 2}
        , '3': {'texto': '13', '?': 2}
        , '4': {'texto': '14', '?': 2}
        , '5': {'texto': '15', '?': 2}},
    {'pergunta1': "Dada as funções f(x)=x-5 e g(x) = 3x+1:"
        , 'pergunta2': 'o valor da soma f(9)+g(2) é?'
        , '1': {'texto': '3', '?': 2}
        , '2': {'texto': '5', '?': 2}
        , '3': {'texto': '7', '?': 2}
        , '4': {'texto': '9', '?': 2}
        , '5': {'texto': '11', '?': 1}},
    {'pergunta1': "Considerando as seguintes funções: f(x) = x-4 e g(x) = 5x+1"
        , 'pergunta2': 'qual o valor da função composta g(f(3))'
        , '1': {'texto': '-4', '?': 2}
        , '2': {'texto': '-2', '?': 2}
        , '3': {'texto': '0', '?': 2}
        , '4': {'texto': '2', '?': 2}
        , '5': {'texto': '4', '?': 2}},
    {'pergunta1': "Qual a derivada da função y = x²-3x"
        , 'pergunta2': ''
        , '1': {'texto': 'y\' = 2x²-3', '?': 2}
        , '2': {'texto': 'y\' = 2x-3', '?': 2}
        , '3': {'texto': 'y\' = -2x-3', '?': 2}
        , '4': {'texto': 'y\' = 2x+3', '?': 1}
        , '5': {'texto': 'y\' = 2x³+2', '?': 2}},
    {'pergunta1': "Derive a função y = (3+x)(2-x)"
        , 'pergunta2': ''
        , '1': {'texto': 'y\' = 2x-3', '?': 2}
        , '2': {'texto': 'y\' = 2x-1', '?': 2}
        , '3': {'texto': 'y\' = -2x-1', '?': 2}
        , '4': {'texto': 'y\' = 2x+3', '?': 2}
        , '5': {'texto': 'y\' = -2x+1', '?': 1}},
    {'pergunta1': "Calcule LIM x²+3"
        , 'pergunta2': '        x>2'
        , '1': {'texto': '', '?': 2}
        , '2': {'texto': '', '?': 2}
        , '3': {'texto': '', '?': 2}
        , '4': {'texto': '', '?': 2}
        , '5': {'texto': '', '?': 2}},
    {'pergunta1': "Calcule LIM 3x²+2"
        , 'pergunta2': '        x>-5'
        , '1': {'texto': '', '?': 2}
        , '2': {'texto': '', '?': 2}
        , '3': {'texto': '', '?': 2}
        , '4': {'texto': '', '?': 2}
        , '5': {'texto': '', '?': 2}},
    {'pergunta1': "Calcule LIM 3x³+x²-x-6"
        , 'pergunta2': '        x>5'
        , '1': {'texto': '', '?': 2}
        , '2': {'texto': '', '?': 2}
        , '3': {'texto': '', '?': 2}
        , '4': {'texto': '', '?': 2}
        , '5': {'texto': '', '?': 2}},
    ]



def QualExercico():
    qual = random.choice(exercicios)
    return qual
