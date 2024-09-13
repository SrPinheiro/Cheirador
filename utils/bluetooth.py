from pybricks.messaging import BluetoothMailboxServer, Mailbox, BluetoothMailboxClient
from configs.parametros import Parametros

class BluetoothStatus:
    HOST = True
    CLIENT = False

class Bluetooth():
    CLIENT = BluetoothStatus.CLIENT
    HOST = BluetoothStatus.HOST

    def __init__(self, host):
        if(host):
            self.servidor = BluetoothMailboxServer()
            self.mensageiro = Mailbox(Parametros.SERVER_BLUETOOTH_CODE, self.servidor)
        else:
            self.servidor  = BluetoothMailboxClient()
            self.servidor.connect(Parametros.SERVER_BLUETOOTH_NAME)
            self.mensageiro = Mailbox(Parametros.CLIENT_BLUETOOTH_CODE, self.servidor)

    def aguardarConexao(self, conexoes=1):
        self.servidor.wait_for_connections(conexoes)

    def lerMensagem(self):
        return self.mensageiro.read()
    
    def enviarMensagem(self, mensagem):
        self.mensageiro.send(mensagem)

    def aguardarMensagem(self):
        self.mensageiro.wait()

    def aguardarMensagemDiferente(self):
        self.mensageiro.wait_new()
        

