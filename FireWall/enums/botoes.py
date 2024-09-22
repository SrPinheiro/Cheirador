from pybricks.parameters import Button # type: ignore

class Botao:
    """
    Classe que representa os botões em um brick ou controle remoto.

    Atributos:
        SUPERIOR_ESQUERDO: Botão localizado na parte superior esquerda.
        SUPERIOR: Botão localizado na parte superior central.
        SUPERIOR_DIREITO: Botão localizado na parte superior direita.
        ESQUERDO: Botão localizado no lado esquerdo.
        CENTRO: Botão central.
        DIREITO: Botão localizado no lado direito.
        INFERIOR_ESQUERDO: Botão localizado na parte inferior esquerda.
        INFERIOR: Botão localizado na parte inferior central.
        INFERIOR_DIREITO: Botão localizado na parte inferior direita.
        FAROL: Botão que aciona o farol.
    """

    SUPERIOR_ESQUERDO = Button.LEFT_UP       # type: Botao
    SUPERIOR = Button.UP                     # type: Botao
    SUPERIOR_DIREITO = Button.RIGHT_UP       # type: Botao
    ESQUERDO = Button.LEFT              # type: Botao
    CENTRO = Button.CENTER               # type: Botao
    DIREITO = Button.RIGHT               # type: Botao
    INFERIOR_ESQUERDO = Button.LEFT_DOWN  # type: Botao
    INFERIOR = Button.DOWN                 # type: Botao
    INFERIOR_DIREITO = Button.RIGHT_DOWN   # type: Botao
    FAROL = Button.BEACON               # type: Botao