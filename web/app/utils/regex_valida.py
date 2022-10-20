import re

from validate_docbr import CPF


def regex_valida_cpf(dados):
    """ Regex para buscar CPF no resultado do OCR e faz validação """
    padrao = "[0-9]{3}[.]*[0-9]{3}[.]*[0-9]{3}[-]*[0-9]{2}"
    cpfs_encontrados = re.findall(padrao, dados)
    if cpfs_encontrados:
        cpf_encontrado = cpfs_encontrados[0]
        cpf_valido = CPF().validate(cpf_encontrado)
        if cpf_valido:
            return cpf_encontrado
        else:
            return 'Não válido'
    else:
        return 'Não encontrado'