def autoSalvarHistoricoDeCor(funcao):
        """
        * NÃO UTILIZE ESSA FUNCAO!
            Esta é uma funcao Wrapper que serve para salvar historico automaticamente e nao deve ser usada fora da classe ColorService
        """
        def funcaoWrapper(self):
            resultado = funcao(self)
            
            if(self._autoSalvarHistorico):
                self.adicionarCorNoHistorico(resultado)

            return resultado
        
        return funcaoWrapper
    
def autoSalvarHistoricoDeDistancia(funcao):
    """
    * NÃO UTILIZE ESSA FUNCAO!
        Esta é uma funcao Wrapper que serve para salvar historico automaticamente e nao deve ser usada fora da classe UltraSonicoService
    """
    
    def funcaoWrapper(self):
        resultado = funcao(self)
        
        if(self._autoSalvar):
            self.adicionarDistanciaNoHistorico(resultado)

        return resultado
    
    return funcaoWrapper