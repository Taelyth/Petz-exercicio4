import pytest
from pages import login_page, inicial_page, produto_page, produto_sucesso_page, carrinho_page


@pytest.fixture()
def login(driver):
    return login_page.LoginPage(driver)


@pytest.fixture()
def inicial(driver):
    return inicial_page.InicialPage(driver)


@pytest.fixture()
def produto(driver):
    return produto_page.ProdutoPage(driver)


@pytest.fixture()
def sucesso(driver):
    return produto_sucesso_page.ProdutoSucessoPage(driver)

@pytest.fixture()
def carrinho(driver):
    return carrinho_page.CarrinhoPage(driver)


def testar_comprar_racao(login, inicial, produto, sucesso, carrinho):
    texto_busca = 'ração yorkshire'
    nome_produto = 'Ração Royal Canin Yorkshire Terrier - Cães Adultos'
    preco_produto = '136.99'
    nome_produto_com_peso = 'Ração Royal Canin Yorkshire Terrier - Cães Adultos - 2,5kg'
    subtotal = '136.99'
    preco_total = '136.99'

    login.clicar_botao_sem_login()

    # Checar texto pagina inicial
    assert inicial.checar_texto_comprar() == 'Comprar'

    # Pesquisar produto
    inicial.pesquisar_produto(texto_busca)
    inicial.checar_nome_produto_e_clicar(nome_produto)

    # Adicionar produto no carrinho
    produto.adicionar_produto_carrinho(nome_produto, preco_produto)

    # Checar se produto foi adicionado com sucesso
    sucesso.checar_produto_com_sucesso(nome_produto_com_peso, preco_produto)

    # Ir para o carrinho
    sucesso.clicar_ir_para_carrinho()

    # Checar informações do carrinho
    carrinho.checar_informacoes_carrinho(nome_produto_com_peso, preco_produto, subtotal, preco_total)
