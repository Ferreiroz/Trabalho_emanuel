[logica.py](https://github.com/user-attachments/files/23246575/logica.py)
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
[dados.py](https://github.com/user-attachments/files/23246580/dados.py)# dados.py

from logica import ServicoData  # Importa o serviço de data para usá-lo

class GeradorPlanilhaFinanceira:
    """Responsável por criar e escrever o conteúdo no arquivo CSV."""
    
    # Encapsulamento: O nome do formato da data e o cabeçalho são detalhes internos.
    _FORMATO_DATA = "%d/%m/%Y %H:%M"
    _CABECALHO_PADRAO = "Categoria,Descrição,Valor (R$)\n"

    def __init__(self, servico_data: ServicoData):
        # Encapsulamento: Depende de um serviço injetado (Injeção de Dependência)
        self._servico_data = servico_data

    def gerar_planilha(self, nome_usuario: str, categorias: list, arquivo_saida: str):
        """
        Gera um arquivo .csv com a estrutura financeira básica.
        """
        data_geracao = self._servico_data.obter_data_atual()

        with open(arquivo_saida, "w", encoding="utf-8") as f:
            # Abstração: A classe expõe a criação do relatório, não os detalhes de escrita linha por linha.
            f.write(f"Relatório Financeiro - {nome_usuario}\n")
            f.write(f"Data de geração: {data_geracao}\n")
            f.write(self._CABECALHO_PADRAO)

            for categoria in categorias:
                # Encapsulamento: A escrita da linha da categoria é interna ao método.
                f.write(f"{categoria},,\n")

        print(f"Planilha gerada com sucesso: {arquivo_saida}")

# --- Fim de dados.py ---
[interface.py](https://github.com/user-attachments/files/23246584/interface.py)
# interface.py

# Importando as classes das outras camadas
from dados import GeradorPlanilhaFinanceira
from logica import ServicoData

def sanitizar_nome(nome: str) -> str:
    """Função utilitária para limpar o nome para uso em nomes de arquivo."""
    safe_name = "".join(c for c in nome if c.isalnum() or c in (" ", "-", "_")).strip().replace(" ", "")
    return safe_name if safe_name else "usuario"

def main():
    # Lógica de Interface/Apresentação (Interação com o usuário)
    nome = input("Digite seu nome: ").strip()
    safe_name = sanitizar_nome(nome)

    categorias_base = ["Receitas", "Despesas Fixas", "Despesas Variáveis", "Investimentos", "Saldo Final"]
    arquivo_saida = f"finaxis_{safe_name}.csv"
    
    try:
        # Injeção de Dependência: Criação e passagem das dependências.
        # A interface não precisa saber 'como' a data é obtida (logica.py) nem 'como' o CSV é escrito (dados.py).
        
        # 1. Iniciar o serviço de utilidade
        servico_data = ServicoData()
        
        # 2. Iniciar a classe de persistência/dados, injetando a dependência necessária
        gerador = GeradorPlanilhaFinanceira(servico_data)
        
        # 3. Executar a ação principal
        gerador.gerar_planilha(nome if nome else "Usuário", categorias_base, arquivo_saida)

    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}")

if __name__ == "__main__":
    main()

# --- Fim de interface.py ---
