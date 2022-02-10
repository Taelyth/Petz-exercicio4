import time

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProdutoSucessoPage(BasePage):
    produto_com_sucesso = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/textView11'
    }

    nome_produto = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/tv_product_name'
    }

    preco_produto = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/tv_product_price'
    }

    ir_carrinho_btn = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/btnGotoCart'
    }

    def checar_texto_sucesso(self):
        assert self._localizar(self.produto_com_sucesso).text == 'Produto adicionado com sucesso'

    def checar_nome_produto(self):
        return self._localizar(self.nome_produto).text

    def checar_preco_produto(self):
        return self._localizar(self.preco_produto).text

    def checar_produto_com_sucesso(self, nome_produto_esperado, preco_produto_esperado):
        # checar se entrou na página
        self.checar_texto_sucesso()

        # Checar nome e preço do produto
        assert self.checar_nome_produto() == nome_produto_esperado
        assert self.checar_preco_produto() == preco_produto_esperado

    def clicar_ir_para_carrinho(self):
        self._clicar(self.ir_carrinho_btn)
