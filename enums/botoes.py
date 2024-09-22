from pybricks.parameters import Button

class Botao:
    """
    Classe que representa os botões em um brick ou controle remoto.

    Atributos:
        ESQUERDA_BAIXO: Botão localizado na parte inferior esquerda.
        BAIXO: Botão localizado na parte inferior central.
        DIREITA_BAIXO: Botão localizado na parte inferior direita.
        ESQUERDA: Botão localizado no lado esquerdo.
        CENTRO: Botão central.
        DIREITA: Botão localizado no lado direito.
        ESQUERDA_CIMA: Botão localizado na parte superior esquerda.
        CIMA: Botão localizado na parte superior central.
        FAROL: Botão que aciona o farol.
        DIREITA_CIMA: Botão localizado na parte superior direita.
    """
    ESQUERDA_BAIXO = Button.LEFT_DOWN  # type: Botao
    BAIXO = Button.DOWN                 # type: Botao
    DIREITA_BAIXO = Button.RIGHT_DOWN   # type: Botao
    ESQUERDA = Button.LEFT              # type: Botao
    CENTRO = Button.CENTER               # type: Botao
    DIREITA = Button.RIGHT               # type: Botao
    ESQUERDA_CIMA = Button.LEFT_UP       # type: Botao
    CIMA = Button.UP                     # type: Botao
    FAROL = Button.BEACON               # type: Botao
    DIREITA_CIMA = Button.RIGHT_UP       # type: Botao