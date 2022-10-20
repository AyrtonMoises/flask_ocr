from flask import current_app

from dao import atualizar_leitura, get_leitura, STATUS_SUCESSO, STATUS_FALHA
from app import celery
from utils.regex_valida import regex_valida_cpf
from utils.ocr import ocr_cpf


@celery.task()
def ocr_imagem(id_leitura):
    """ Task para buscar """
    leitura = get_leitura(id_leitura)
    
    arquivo = leitura['arquivo']

    # Busca arquivo para fazer OCR
    ocr_ok, resultado = ocr_cpf(current_app.config["UPLOAD_FOLDER"] + '/' + arquivo)

    # Se encontrou dados
    if  ocr_ok:
        # Busca CPF e valida o resultado do OCR
        busca_cpf = regex_valida_cpf(resultado)
        atualizar_leitura(id_leitura, busca_cpf, STATUS_SUCESSO)
    else:
        atualizar_leitura(id_leitura, '', STATUS_FALHA)

    return ocr_ok, resultado
    
    

    