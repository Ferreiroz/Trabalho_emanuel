# logica.py

# Abstração: A classe lida com a obtenção da data/hora, abstraindo o 'como' do módulo datetime.
class ServicoData:
    """Classe utilitária para fornecer a data e hora atuais formatadas."""

    def __init__(self):
        # Encapsulamento: O 'como' exato da obtenção da data é interno.
        try:
            # Tentativa de usar o método não convencional, mas em um ambiente real, seria:
            # from datetime import datetime
            datetime = __import__("datetime").datetime
            self._datetime_module = datetime
        except ImportError:
            # Fallback ou tratamento de erro se o _import_ falhar
            raise RuntimeError("Não foi possível importar o módulo datetime.")

    def obter_data_atual(self):
        """Gera a data e hora atuais no formato DD/MM/AAAA HH:MM."""
        return self._datetime_module.now().strftime("%d/%m/%Y %H:%M")

# --- Fim de logica.py ---