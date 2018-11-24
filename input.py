import pygame

# array que vai conter as teclas carregadas
_keys = []
# array que vai conter as teclas carregadas no ultimo update
_last_keys = []

# array que contem os butoes do mouse
_mouse_buttons = [False, False, False]

# array que contem os butoes do mouse no ultimo update
_last_mouse_buttons = _mouse_buttons

"""
Keys from pygame

KeyASCII      ASCII   Common Name

K_BACKSPACE   \b      backspace
K_TAB         \t      tab
K_CLEAR               clear
K_RETURN      \r      return
K_PAUSE               pause
K_ESCAPE      ^[      escape
K_SPACE               space
K_EXCLAIM     !       exclaim
K_QUOTEDBL    "       quotedbl
K_HASH        #       hash
K_DOLLAR      $       dollar
K_AMPERSAND   &       ampersand
K_QUOTE               quote
K_LEFTPAREN   (       left parenthesis
K_RIGHTPAREN  )       right parenthesis
K_ASTERISK    *       asterisk
K_PLUS        +       plus sign
K_COMMA       ,       comma
K_MINUS       -       minus sign
K_PERIOD      .       period
K_SLASH       /       forward slash
K_0           0       0
K_1           1       1
K_2           2       2
K_3           3       3
K_4           4       4
K_5           5       5
K_6           6       6
K_7           7       7
K_8           8       8
K_9           9       9
K_COLON       :       colon
K_SEMICOLON   ;       semicolon
K_LESS        <       less-than sign
K_EQUALS      =       equals sign
K_GREATER     >       greater-than sign
K_QUESTION    ?       question mark
K_AT          @       at
K_LEFTBRACKET [       left bracket
K_BACKSLASH   \       backslash
K_RIGHTBRACKET ]      right bracket
K_CARET       ^       caret
K_UNDERSCORE  _       underscore
K_BACKQUOTE   `       grave
K_a           a       a
K_b           b       b
K_c           c       c
K_d           d       d
K_e           e       e
K_f           f       f
K_g           g       g
K_h           h       h
K_i           i       i
K_j           j       j
K_k           k       k
K_l           l       l
K_m           m       m
K_n           n       n
K_o           o       o
K_p           p       p
K_q           q       q
K_r           r       r
K_s           s       s
K_t           t       t
K_u           u       u
K_v           v       v
K_w           w       w
K_x           x       x
K_y           y       y
K_z           z       z
K_DELETE              delete
K_KP0                 keypad 0
K_KP1                 keypad 1
K_KP2                 keypad 2
K_KP3                 keypad 3
K_KP4                 keypad 4
K_KP5                 keypad 5
K_KP6                 keypad 6
K_KP7                 keypad 7
K_KP8                 keypad 8
K_KP9                 keypad 9
K_KP_PERIOD   .       keypad period
K_KP_DIVIDE   /       keypad divide
K_KP_MULTIPLY *       keypad multiply
K_KP_MINUS    -       keypad minus
K_KP_PLUS     +       keypad plus
K_KP_ENTER    \r      keypad enter
K_KP_EQUALS   =       keypad equals
K_UP                  up arrow
K_DOWN                down arrow
K_RIGHT               right arrow
K_LEFT                left arrow
K_INSERT              insert
K_HOME                home
K_END                 end
K_PAGEUP              page up
K_PAGEDOWN            page down
K_F1                  F1
K_F2                  F2
K_F3                  F3
K_F4                  F4
K_F5                  F5
K_F6                  F6
K_F7                  F7
K_F8                  F8
K_F9                  F9
K_F10                 F10
K_F11                 F11
K_F12                 F12
K_F13                 F13
K_F14                 F14
K_F15                 F15
K_NUMLOCK             numlock
K_CAPSLOCK            capslock
K_SCROLLOCK           scrollock
K_RSHIFT              right shift
K_LSHIFT              left shift
K_RCTRL               right ctrl
K_LCTRL               left ctrl
K_RALT                right alt
K_LALT                left alt
K_RMETA               right meta
K_LMETA               left meta
K_LSUPER              left windows key
K_RSUPER              right windows key
K_MODE                mode shift
K_HELP                help
K_PRINT               print screen
K_SYSREQ              sysrq
K_BREAK               break
K_MENU                menu
K_POWER               power
K_EURO                euro
"""


def update():
    # se a janela do jogo estiver ativa
    if pygame.key.get_focused():
        # como estamos a usar 2 variaveis
        # que estao defenidas dentro de um modulo
        # usamos a palavra global para o metodo saber que nao queremos defenir
        # uma nova variavel mas sim usar a que esta defenida
        global _keys, _last_keys, _last_mouse_buttons, _mouse_buttons
        # setamos o _last_keys para conter as teclas que estavas carregadas no ultimo update
        _last_keys[:] = _keys[:]  # usamos o : para selecao
        #  _keys[3:8] = [] neste caso limpavamos as posicoes 3 ate ao 8

        # defenimos uma variavel temporaria para conter as teclas que estao a ser carregadas
        # get_pressed retorna um array com todas as keys do teclado, tendo o valor 0 se nao forem carregadas
        # e o valor 1 se forem carregadas
        Key_pressed = pygame.key.get_pressed()
        # limpamos a variavel keys
        _keys = []
        # e adicionamos as keys que estiverem a ser clicadas
        for key in range(0, len(Key_pressed)):
            if Key_pressed[key] == 1:  # se estivermos a carregar na tecla
                _keys.append(key)  # adicionamos as _keys

        # obtemos os butoes do mouse
        _last_mouse_buttons[:] = _mouse_buttons[:]
        _mouse_buttons = pygame.mouse.get_pressed()


# metodo para saber se uma tecla esta a ser presionada
# no RGSS seria Input.press?
def is_key_press(key):
    return key in _keys


# metodo para saber se uma tecla foi carregada e largada
# no RGSS seria Input.trigger?
def is_key_pressed(key):
    global _last_keys, _keys
    return (key in _last_keys) and (key not in _keys)


# retorna um array contendo [x,y] posicao relativa a janela
def mouse_pos():
    return pygame.mouse.get_pos()


# retorna um array contendo [x, y] movimentro relativo desde o ultimo update
def mouse_movement():
    return pygame.mouse.get_rel()


# retorna verdadeiro se o butao esquerdo estiver a ser clicado, caso contrario retorna falso
def mouse_left_button_down():
    return _mouse_buttons[0]


# retorna verdadeiro se o butao do meio estiver a ser clicado, caso contrario retorna falso
def mouse_middle_button_down():
    return _mouse_buttons[1]


# retorna verdadeiro se o butao direito estiver a ser clicado, caso contrario retorna falso
def mouse_right_button_down():
    return _mouse_buttons[2]


# retorna verdadeiro se o butao esquerdo foi clicado e agora largado, caso contrario retorna falso
def mouse_left_button_up():
    return not _mouse_buttons[0] and _last_mouse_buttons[0]


# retorna verdadeiro se o butao do meio foi clicado e agora largado, caso contrario retorna falso
def mouse_middle_button_up():
    return not _mouse_buttons[1] and _last_mouse_buttons[1]


# retorna verdadeiro se o butao direito foi clicado e agora largado, caso contrario retorna falso
def mouse_right_button_up():
    return not _mouse_buttons[2] and _last_mouse_buttons[2]