import pytesseract
from PIL import Image


def ocr_cpf(caminho_arquivo):
    """ Busca arquivo para fazer OCR e retorna se ouve falha e dados """
    try:
        resultado = pytesseract.image_to_string(
            Image.open(caminho_arquivo)
        )
        return True, resultado
    except Exception as e:
        return False, e