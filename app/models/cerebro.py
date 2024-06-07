from pybricks.hubs import EV3Brick
from app.enums.cor import Cor

class Cerebro:
    def __init__(self):
        self.dispositivo = EV3Brick()

    def getBotoes(self):
        return self.dispositivo.buttons.pressed()
    
    def isPressionado(self, botao):
        pressionados = self.getBotoes()

        return botao in pressionados

    def ligarLuz(self, cor):
        self.dispositivo.light.on(cor)

    def desligarLuz(self):
        self.dispositivo.light.off()

    def tocarBeep(self, frequencia=500, duracao=100):
        self.dispositivo.speaker.beep(frequency=frequencia, duration=duracao)

    def tocarNotas(self, notas, tempo=120):
        self.dispositivo.speaker.play_notes(notas, tempo=tempo)

    def tocarArquivo(self, nome_arquivo):
        self.dispositivo.speaker.play_file(nome_arquivo)

    def dizerTexto(self, texto):
        self.dispositivo.speaker.say(texto)

    def configurarOpcoesFala(self, idioma=None, voz=None, velocidade=None, tom=None):
        self.dispositivo.speaker.set_speech_options(language=idioma, voice=voz, speed=velocidade, pitch=tom)

    def ajustarVolume(self, volume, qual='_all_'):
        self.dispositivo.speaker.set_volume(volume, which=qual)

    def limparTela(self):
        self.dispositivo.screen.clear()

    def escreverTexto(self, x, y, texto, cor_texto=Cor.PRETO, cor_fundo=None):
        self.dispositivo.screen.draw_text(x, y, texto, text_color=cor_texto, background_color=cor_fundo)

    def imprimirTexto(self, *args, separador=' ', fim='\n'):
        self.dispositivo.screen.print(*args, sep=separador, end=fim)

    def imprimirImagem(self, url):
        self.dispositivo.screen.load_image(url)

    def larguraDaTela(self):
        return self.dispositivo.screen.width
    
    def alturaDaTela(self):
        return self.dispositivo.screen.height

    def salvarTela(self, nome):
        self.dispositivo.screen.save(nome)

    def bateria(self):
        return self.dispositivo.baterry.current()
    
    def voltagem(self):
        return self.dispositivo.baterry.current()
