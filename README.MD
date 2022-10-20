# Flask + Pymongo + Docker

- Projeto web para OCR de imagens usando Pytesseract 
- Mensageria com Celery e RabbitMQ para mensageria e Redis para guardar resultados
- Flower para monitoramento


### Desenvolvimento
```
docker-compose -f docker-compose-dev.yml build
docker-compose -f docker-compose-dev.yml up
docker-compose -f docker-compose-dev.yml down
```

### Produção
```
docker-compose build
docker-compose up
docker-compose down
```

### Testes
```
docker-compose -f docker-compose-dev.yml run web python -m pytest tests -p no:cacheprovider
```

###  Flask (Visualizar e enviar imagens para fila de OCR)

### Desenvolvimento
[http://0.0.0.0:5000/]

### Produção
[http://0.0.0.0:81/]

### Flower
Monitoramento das tasks
[http://0.0.0.0:5555/]

### RabbitMQ Management
[http://0.0.0.0:15673]