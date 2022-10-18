import pytest

from app import create_app


@pytest.fixture(scope="session")
def app():
    _app = create_app('config.ConfigTesting')

    yield _app

    drop_db()

    import shutil
    pasta_uploader = _app.config.get('UPLOAD_FOLDER')
    shutil.rmtree(pasta_uploader)


def drop_db():
    from ext.database import mongo
    
    collections = mongo.db.list_collection_names()

    for collection in collections:
        mongo.db.drop_collection(collection)

@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture(scope="module")
def leituras():
    # Limpar dados
    drop_db()

    # Insere lista de leituras
    from dao import insert_leitura, all_leituras

    insert_leitura(arquivo="imagem1.jpg")
    insert_leitura(arquivo="imagem2.jpg")
    insert_leitura(arquivo="imagem3.jpg")

    return all_leituras()