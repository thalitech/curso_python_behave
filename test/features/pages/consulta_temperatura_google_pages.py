#Autor: thalita Bernardes

import time
from features.support.environments import *
from features.support.elements import *
from features.support.page_utils import PageUtils
page_utils = PageUtils()

class PesquisaTemperatura:
    def acessar_site_google(context):
        page_utils.abrir_um_browser(URL_GOOGLE)

    def pesquisar_temperatura(context):
        page_utils.clicar_elemento_pagina(PESQ_GOOGLE)

    def inserir_texto_no_elemento(context):
        page_utils.inserir_dados_no_elemento(PESQ_GOOGLE, DESC_PESQ)
        time.sleep(1)
        
    def clicar_para_realizar_pesquisa(context):
        page_utils.clicar_elemento_pagina(BTN_DESC_PESQ)
        time.sleep(1)

