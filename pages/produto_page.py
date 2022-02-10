from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProdutoPage(BasePage):
    nome_produto = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/tv_prod_name'
    }

    peso_slider = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/spinner_text'
    }

    slider_select_2 = {
        'by': AppiumBy.XPATH,
        'value': '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android'
                 '.widget.TextView[2]'
    }

    preco_produto = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/tv_prod_main_price'
    }

    adicionar_carrinho_btn = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/btnAddToCart'
    }

    def checar_nome_produto(self, nome_produto_esperado):
        self._esperar_texto_elemento(self.nome_produto, nome_produto_esperado)
        return self._localizar(self.nome_produto).text

    def selecionar_peso_2(self):
        self._localizar(self.peso_slider).click()
        self._clicar(self.slider_select_2)

    def checar_preco_produto(self):
        return self._localizar(self.preco_produto).text

    def clicar_adicionar_produto(self):
        self._clicar(self.adicionar_carrinho_btn)

    def adicionar_produto_carrinho(self, nome_produto_esperado, preco_produto_esperado):

        assert self.checar_nome_produto(nome_produto_esperado) == nome_produto_esperado

        self.selecionar_peso_2()

        assert self.checar_preco_produto() == preco_produto_esperado

        self.clicar_adicionar_produto()

