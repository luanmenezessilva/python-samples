from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between requests

    @task
    def my_task(self):
        # self.client.get("/portal/familias/00350B/filtro") # Informações para o filtro
        self.client.get("/portal/familias/00006B/0001/N/dados") # Massa de dados

    # Através do console executar uma das opções abaixo

    ## Opção 1 - Executar no modo console para 10 usuários e com spawn-rate 3
    # locust -f my_test_script.py --host=http://192.168.0.9:9792 --headless -u 10 -r 3

    ## Opção 2 - Executar o comando e acessar as informações via navegador
    # locust -f my_test_script.py --host=http://192.168.0.9:9792
    # Acessar via navegador - http://localhost:8089/

    # TODO: Alterar nome da API para documentar como fonte exemplo