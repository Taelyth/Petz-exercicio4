# Petz - Exercício 4
Projeto criado para exercício final do curso [Formação em Teste de Software][Iterasys] em **Python** utilizando **Appium**.

Neste projeto é possível rodar testes **mobile** localmente no emulador disponibilizado pelo AVD Manager.

Ele foi criado para treinamento em como utilizar a formatação **Page Object**, onde os elementos e testes ficam separados por script/página.

---

### Pré-Requisitos
- As bibliotecas utilizadas são:

```
Appium-Python-Client
selenium
pytest
```

- APK usado para o exercício: **Petz**, que pode ser encontrado em qualquer site de download de APKs.

---

### Glossário

`pages` Diretório onde é adicionado os scripts de cada página testada (PageObject).

`base_page.py` Arquivo base onde é programada as ações que serão utilizadas em cada teste, como entrar, clicar, etc.

`login_page.py, inicial_page.py, carrinho_page.py, etc ` Arquivos onde estão os elementos e os requisitos usados nos testes de cada uma dessas páginas.

`tests` Diretório contendo os testes realizados e configurações do teste.

`conftest.py` Configuração do ambiente onde rodará o teste.

`comprar_racao_test.py` Script dos testes de comprar um produto, ele utiliza o código criado nos arquivos `_page.py` para fazer as ações do teste.

---

### Créditos
[<img src="assets\Iterasys-Logo.png" width="20%"/>][Iterasys]


<!-- links -->
[Iterasys]: https://iterasys.com.br/

<!-- imagens -->
[Iterasys-Logo]: assets/Iterasys-Logo.png (Iterasys-logo)