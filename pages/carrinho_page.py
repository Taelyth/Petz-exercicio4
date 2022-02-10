from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CarrinhoPage(BasePage):
    titulo_page = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/toolbar_title'
    }

    produto_com_sucesso = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/textView11'
    }

    nome_produto = {
        'by': AppiumBy.XPATH,
        'value': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                 '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android'
                 '.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget'
                 '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget'
                 '.TextView'
    }

    preco_produto = {
        'by': AppiumBy.XPATH,
        'value': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                 '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android'
                 '.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget'
                 '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget'
                 '.LinearLayout[2]/android.widget.TextView[2]'
    }

    subtotal = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/tv_price_subtotal'
    }

    preco_total = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/tv_total_price'
    }

    # Ração Royal Canin Yorkshire Terrier - Cães Adultos - 2,5kg
    # 136.99 / 136.99
    # Produto adicionado com sucesso
    # titulo_page = Carrinho

    def checar_se_estou_no_carrinho(self):
        assert self._localizar(self.titulo_page).text == 'Carrinho'

    def checar_nome_produto(self):
        return self._localizar(self.nome_produto).text

    def checar_preco_produto(self):
        return self._localizar(self.preco_produto).text

    def checar_subtotal(self):
        return self._localizar(self.subtotal).text

    def checar_preco_total(self):
        return self._localizar(self.preco_total).text

    def checar_informacoes_carrinho(self, nome_produto_esperado, preco_produto_esperado,
                                    subtotal_esperado, preco_total_esperado):
        # Checar se estou na página correta
        self.checar_se_estou_no_carrinho()

        # Checar as informações do Produto e Preço
        assert self.checar_nome_produto() == nome_produto_esperado
        assert self.checar_preco_produto() == preco_produto_esperado
        assert self.checar_subtotal() == subtotal_esperado
        assert self.checar_preco_total() == preco_total_esperado
