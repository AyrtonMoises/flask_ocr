import os
import pathlib
from uuid import uuid4

from flask import render_template, request, url_for, redirect, flash, Blueprint, current_app
from werkzeug.utils import secure_filename

from dao import insert_leitura, all_leituras
from tasks import ocr_imagem


ocr_bp = Blueprint('ocr', __name__, url_prefix='/')


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    """ Verifica se arquivo possui extensão permitida """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@ocr_bp.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        if 'arquivo' not in request.files:
            flash('Não faz parte de um arquivo')
            return redirect(request.url)
        arquivo = request.files['arquivo']

        extensao = arquivo.filename.split('.')[-1]
        arquivo.filename = uuid4().__str__() + '.' + extensao

        if arquivo.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        if arquivo and allowed_file(arquivo.filename):
            pathlib.Path(current_app.config["UPLOAD_FOLDER"]).mkdir(exist_ok=True)
            arquivo_filename = secure_filename(arquivo.filename)
            arquivo.save(os.path.join(current_app.config["UPLOAD_FOLDER"], arquivo_filename))
            resultado = insert_leitura(arquivo.filename)
            id_leitura = str(resultado.inserted_id)
            ocr_imagem.delay(id_leitura)

        else:
            flash('Tipo de arquivo não permitido:' + extensao)
            return redirect(request.url)
            
        flash('Leitura na fila')
        return redirect(url_for('ocr.index'))

    leitura_all = all_leituras()
    return render_template('index.html', leituras=leitura_all)