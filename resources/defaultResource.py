from enums.porta import Porta

class Resource:
    """Classe base para dispositivos LEGO®."""

    def extrair(self):
        # type: () -> object
        """Extrai o dispositivo LEGO® associado.

        Returns:
            Objeto: O dispositivo LEGO®.
        """
        return self.dispositivo
    
    def porta(self):
        # type: () -> Porta
        """Retorna a porta do dispositivo.

        Returns:
            Porta: Retorna a porta do dispositivo.
        """
        return self.porta
