# Loja-online
"O projeto web visa oferecer uma experiência inovadora e interativa para os usuários, combinando design moderno e funcionalidades avançadas."


# comandos
instalar as dependencias para o pygraphviz
```
sudo apt install graphviz libgraphviz-dev pkg-config
```

Gerar DER
```
./manage.py graph_models -a -g --pygraphviz -o der_produtos_inicial_completo.png
./manage.py graph_models --pygraphviz -o der_produtos_inicial.png produtos
```