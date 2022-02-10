from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class InicialPage(BasePage):
    comprar_btn = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/largeLabel'
    }

    pesquisa_btn = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/toolbar_search'
    }

    text_btn = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/searchBox'
    }

    pesquisa1 = {
        'by': AppiumBy.XPATH,
        'value': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                 '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android'
                 '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                 '.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView '
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def checar_texto_comprar(self):
        return self._localizar(self.comprar_btn).text

    def checar_tela_pesquisa(self):
        return self._localizar(self.text_btn).text

    def pesquisar_produto(self, texto_busca):
        # Checar se está na página correta
        assert self.checar_texto_comprar() == 'Comprar'

        # Clicar no botão pesquisar
        self._clicar(self.pesquisa_btn)

        # Checar tela de pesquisa
        assert self.checar_tela_pesquisa() == 'Pesquisar na Petz'

        # Escrever nome do produto
        self._escrever(self.text_btn, texto_busca)

    def checar_nome_produto_e_clicar(self, nome_produto_esperado):
        nome_produto = self._localizar(self.pesquisa1)
        assert nome_produto.text == nome_produto_esperado
        nome_produto.click()
