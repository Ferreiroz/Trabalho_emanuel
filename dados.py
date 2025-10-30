# dados.py

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