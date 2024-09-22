from pybricks.messaging import BluetoothMailboxServer, Mailbox, BluetoothMailboxClient # type: ignore
from configs.parametros import Parametros

class Bluetooth():
    def __init__(self, host, nome=''):
        # type: (bool, str) -> Bluetooth
        if(host):
            self.servidor = BluetoothMailboxServer()
            self.mensageiro = Mailbox(Parametros.SERVER_BLUETOOTH_CODE, self.servidor)
        else:
            self.servidor  = BluetoothMailboxClient()
            self.servidor.connect(Parametros.SERVER_BLUETOOTH_NAME)
            self.mensageiro = Mailbox(Parametros.CLIENT_BLUETOOTH_CODE, self.servidor)

    def aguardarConexao(self, conexoes=1):
        # type: (int) -> None
        self.servidor.wait_for_connections(conexoes)

    def lerMensagem(self):
        # type: () -> str
        return self.mensageiro.read()
    
    def enviarMensagem(self, mensagem):
        # type: (str) -> None
        self.mensageiro.send(mensagem)

    def aguardarMensagem(self):
        # type: () -> None
        self.mensageiro.wait()

    def aguardarMensagemDiferente(self):
        # type: () -> None
        self.mensageiro.wait_new()
