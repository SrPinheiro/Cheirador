from pybricks.hubs import EV3Brick
from enums.cor import Cor
from resources.defaultResource import Resource
from enums.botoes import Botao
from enums.cor import Cor

class Cerebro(Resource):
    """Classe para controlar o LEGO® MINDSTORMS® EV3 Brick."""

    def __init__(self):
        # type: () -> None
        self.dispositivo = EV3Brick()
        self.dispositivo.speaker.set_speech_options(language='pt-br', voice='f1', speed=None, pitch=None)
        

    def getBotoes(self):
        # type: () -> list[Botao]
        """Retorna a lista de botões pressionados."""
        return self.dispositivo.buttons.pressed()
    
    def isPressionado(self, botao):
        # type: (Botao) -> bool
        """Verifica se um botão específico está pressionado.

        Parameters:
            botao (Botao): O botão a ser verificado.

        Returns:
            bool: True se o botão estiver pressionado, caso contrário False.
        """
        botoesPressionados = self.getBotoes()
        return botao in botoesPressionados

    def ligarLuz(self, cor):
        # type: (Cor) -> None
        """Liga a luz na cor especificada.

        Parameters:
            cor (Cor): A cor da luz.
        """
        self.dispositivo.light.on(cor)

    def desligarLuz(self):
        # type: () -> None
        """Desliga as luzes do bloco."""
        self.dispositivo.light.off()

    def tocarBeep(self, frequencia=500, duracao=100):
        # type: (int, int) -> None
        """Toca um beep com a frequência e duração especificadas.

        Parameters:
            frequencia (int): Frequência do beep.
            duracao (int): Duração do beep.
        """
        self.dispositivo.speaker.beep(frequency=frequencia, duration=duracao)

    def tocarVariosBips(self, quantidade, frequencia=500, duracao=100):
        #type: (int, int, int) -> None
        """Toca varios beep com a frequência e duração especificadas.

        Parameters:
            quantidade (int): quantidade de beeps
            frequencia (int): Frequência do beep.
            duracao (int): Duração do beep.
        """
        for _ in range(quantidade):
            self.tocarBeep(frequencia, duracao)

    def tocarNotas(self, notas, tempo=120):
        # type: (iter, int) -> None
        """Toca uma sequência de notas musicais.

        Parameters:
            notas (iter): Sequência de notas a serem tocadas.
            tempo (int): Tempo em batidas por minuto.
        """
        self.dispositivo.speaker.play_notes(notas, tempo=tempo)

    def tocarArquivo(self, nome_arquivo):
        # type: (str) -> None
        """Toca um arquivo de som.

        Parameters:
            nome_arquivo (str): Caminho do arquivo de som.
        """
        self.dispositivo.speaker.play_file(nome_arquivo)

    def dizerTexto(self, texto):
        # type: (str) -> None
        """Faz o EV3 dizer um texto.

        Parameters:
            texto (str): O texto a ser dito.
        """
        self.dispositivo.speaker.say(texto)

    def configurarOpcoesFala(self, idioma='pt-br', voz=None, velocidade=None, tom=None):
        # type: (str, str, int, int) -> None
        """Configura as opções de fala.

        Parameters:
            idioma (str): Idioma do texto.
            voz (str): Voz a ser usada.
            velocidade (int): Velocidade em palavras por minuto.
            tom (int): Tom da voz.
        """
        self.dispositivo.speaker.set_speech_options(language=idioma, voice=voz, speed=velocidade, pitch=tom)

    def ajustarVolume(self, volume, qual='_all_'):
        # type: (int, str) -> None
        """Ajusta o volume do speaker.

        Parameters:
            volume (int): Volume do speaker.
            qual (str): Tipo de volume a ser ajustado (Beep ou PCM).
        """
        self.dispositivo.speaker.set_volume(volume, which=qual)

    def limparTela(self):
        # type: () -> None
        """Limpa a tela do EV3."""
        self.dispositivo.screen.clear()

    def escreverTexto(self, x, y, texto, cor_texto=Cor.PRETO, cor_fundo=None):
        # type: (int, int, str, Cor, Cor) -> None
        """Escreve texto na tela.

        Parameters:
            x (int): Posição x onde o texto começa.
            y (int): Posição y onde o texto começa.
            texto (str): Texto a ser escrito.
            cor_texto (Cor): Cor do texto.
            cor_fundo (Cor): Cor de fundo.
        """
        self.dispositivo.screen.draw_text(x, y, texto, text_color=cor_texto, background_color=cor_fundo)

    def imprimirTexto(self, *args, separador=' ', fim='\n'):
        # type: (*object, str, str) -> None
        """Imprime texto na tela.

        Parameters:
            *args: Objetos a serem impressos.
            separador (str): Separador entre os objetos.
            fim (str): Final da linha.
        """
        self.dispositivo.screen.print(*args, sep=separador, end=fim)

    def imprimirImagem(self, url):
        # type: (str) -> None
        """Carrega uma imagem na tela.

        Parameters:
            url (str): Caminho da imagem.
        """
        self.dispositivo.screen.load_image(url)

    def larguraDaTela(self):
        # type: () -> int
        """Retorna a largura da tela em pixels."""
        return self.dispositivo.screen.width
    
    def alturaDaTela(self):
        # type: () -> int
        """Retorna a altura da tela em pixels."""
        return self.dispositivo.screen.height

    def salvarTela(self, nome):
        # type: (str) -> None
        """Salva a tela como um arquivo PNG.

        Parameters:
            nome (str): Caminho do arquivo a ser salvo.
        """
        self.dispositivo.screen.save(nome)

    def bateria(self):
        # type: () -> int
        """Retorna a corrente da bateria."""
        return self.dispositivo.battery.current()
    
    def voltagem(self):
        # type: () -> int
        """Retorna a voltagem da bateria."""
        return self.dispositivo.battery.voltage()
