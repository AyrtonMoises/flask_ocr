import io

from utils.regex_valida import regex_valida_cpf
from utils.ocr import ocr_cpf


def test_index_get_page(client, leituras):
    """ Teste index"""
    response = client.get('/')
    assert response.status_code == 200

    for leitura in leituras:
        assert bytes(str(leitura['_id']), 'UTF-8') in response.data
        assert bytes(str(leitura['arquivo']), 'UTF-8') in response.data


def test_index_post_page_ok(client):
    """ Teste enviando arquivo """
    image_name = "fake-image-stream.jpg"
    data = {
        'arquivo': (io.BytesIO(b"some random data"), image_name)
    }
    response = client.post('/', data=data, follow_redirects=True)
    assert response.status_code == 200

def test_index_post_page_empty(client):
    """ Teste enviando arquivo vazio """
    data = {'arquivo': ''}
    response = client.post('/', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert bytes('Não faz parte de um arquivo', 'UTF-8') in response.data
    
def test_index_post_page_not_allowed(client):
    """ Teste enviando arquivo não permitido """
    nome_arquivo = "arquivo"
    extensao = 'pdf'
    data = {
        'arquivo': (io.BytesIO(b"some random data"), nome_arquivo + '.' + extensao)
    }
    response = client.post('/', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert bytes(f'Tipo de arquivo não permitido:{extensao}', 'UTF-8') in response.data

def test_valida_cpf_valido():
    """ Teste busca de CPF válido """
    dados = "teste 12345 111.abc.11x.11 387.089.920-45"
    resultado = regex_valida_cpf(dados)
    print(resultado,'kkk')
    assert resultado == "387.089.920-45"

def test_valida_cpf_nao_valido():
    """ Teste busca de CPF não válido """
    dados = "teste 12345 111.abc.11x.11 231.189.900-45"
    resultado = regex_valida_cpf(dados)
    assert resultado == "Não válido"

def test_valida_sem_cpf():
    """ Teste busca sem CPF """
    dados = "teste 12345 111.abc.11x.11"
    resultado = regex_valida_cpf(dados)
    assert resultado == "Não encontrado"

def test_leitura_ocr():
    """ Teste busca OCR """
    caminho_arquivo = './tests/functional/ocr_example/imagem_valida.png'
    ocr_ok, _ = ocr_cpf(caminho_arquivo)
    assert ocr_ok == True

def test_leitura_ocr_invalido():
    """ Teste busca OCR invalido"""
    caminho_arquivo = './tests/functional/ocr_example/imagem_invalida.png'
    ocr_ok, _ = ocr_cpf(caminho_arquivo)    
    assert ocr_ok == False


