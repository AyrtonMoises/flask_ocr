
def test_create_leitura():
    """ Teste salvando leitura """ 
    from dao import insert_leitura, get_leitura, STATUS_PENDENTE

    arquivo = "imagem.jpg"
    leitura = insert_leitura(arquivo)
    leitura_id = leitura.inserted_id

    leitura_data = get_leitura(leitura_id)

    assert leitura_data['arquivo'] == arquivo
    assert leitura_data['status'] == STATUS_PENDENTE


def test_update_leitura(client):
    """ Teste atualizando leitura """ 
    from dao import insert_leitura, atualizar_leitura, get_leitura, STATUS_SUCESSO

    # Cria registro
    arquivo = "imagem.jpg"
    leitura = insert_leitura(arquivo)
    leitura_id = leitura.inserted_id

    # Atualiza dados e verifica mudanças
    cpf = "387.089.920-45"
    atualizar_leitura(leitura_id, cpf, STATUS_SUCESSO)
    leitura_atualizada = get_leitura(leitura_id)

    assert leitura_atualizada['cpf'] == cpf
    assert leitura_atualizada['status'] == STATUS_SUCESSO


def test_all_leituras(client, leituras):
    """ Teste buscando todas as leituras """
    from dao import all_leituras

    assert len(list(all_leituras())) == 3
    




