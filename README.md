Flask + Zabbix: Monitoramento de Aplicações

Descrição Geral
  Este projeto demonstra a integração entre uma aplicação Flask e o sistema de monitoramento Zabbix. O objetivo é monitorar a disponibilidade e o desempenho da aplicação Flask em tempo real, utilizando o agente Zabbix.

Tecnologias Utilizadas
  Flask: Framework web em Python para criar aplicações leves e rápidas.

  Docker: Para conteinerização da aplicação Flask e do agente Zabbix.

  Zabbix: Ferramenta de monitoramento utilizada para coletar e visualizar métricas da aplicação.

  Docker Compose: Orquestração dos containers.

Passo a Passo para Rodar a Aplicação

  Clone o repositório:

    git clone https://github.com/seuusuario/flask-zabbix-monitoring.git
    cd flask-zabbix-monitoring

Construa e inicie os containers:

    sudo docker-compose up -d --build

Verifique se os containers estão rodando:

    sudo docker ps

Acesse a aplicação Flask via navegador ou curl:

    http://localhost:5000

Configuração do Zabbix

  Acesse o container do agente Zabbix:

    sudo docker exec -it zabbix-agent bash

Edite o arquivo de configuração:

    nano /etc/zabbix/zabbix_agentd.conf

  Configure os seguintes parâmetros:

    Server=IP_DO_SERVIDOR_ZABBIX
    ServerActive=IP_DO_SERVIDOR_ZABBIX
    Hostname=flask-app

Reinicie o agente Zabbix:

    service zabbix-agent restart

No Zabbix Server:

  Adicione um novo host

    Configure a coleta de métricas para monitorar a API Flask

Exemplos de Monitoramento

  Disponibilidade da aplicação: Teste de resposta HTTP 200.

  Uso de CPU e Memória: Métricas do container.

  Tempo de resposta: Mede a latência de resposta da API.

Referências

[Documentação do Flask](https://flask.palletsprojects.com/en/stable/)

[Documentação do Zabbix](https://www.zabbix.com/documentation/7.2/en/manual/appliance)

[Docker Compose](https://docs.docker.com/desktop/setup/install/linux/)
