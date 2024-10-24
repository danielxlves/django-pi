Este projeto conecta o sgbd mysql e o django via docker.

Os models, views, subrotas e serializers estão na pasta "api".

Na pasta principal myproject esta o arquivo de rota urls que gerencia a requisicao no servidor web.

Inicie o projeto após entrar na pasta que contem o docker compose:

Sem logs
```
docker compose up -d 
```

Com logs
```
docker compose up  
```

Deleta os containers/rede interna
```
docker compose down  
```

Crie um super usuário do admin do django
```
docker-compose exec api python manage.py createsuperuser  
```
