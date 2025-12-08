# WordPress Automated Deployment

Deploy automatizado do WordPress na AWS usando Terraform, Ansible e Docker.

##  Características

- **Infraestrutura como Código** (Terraform)
- **Configuração automatizada** (Ansible) 
- **Containerizado** (Docker Compose)
- **Free Tier** (t3.micro, 8GB EBS)
- **1 comando para deploy completo**

## Pré-requisitos

### Instalação das ferramentas:

```
sudo apt update
sudo apt install unzip
```

```bash
# Terraform (Linux/WSL)
curl -fsSL https://releases.hashicorp.com/terraform/1.8.3/terraform_1.8.3_linux_amd64.zip -o terraform.zip \
&& unzip terraform.zip \
&& sudo mv terraform /usr/local/bin/ \
&& rm terraform.zip

# Ansible
sudo apt install ansible

# AWS CLI (Linux x86_64)
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install
````

Configurar credencias: ```aws configure```
(As credencias são geradas pelo IAM da AWS)
<img width="543" height="194" alt="aws" src="https://github.com/user-attachments/assets/66dd8881-19b4-4ca9-a938-c331780f7719" />



# Para realizar o Deploy

```
chmod +x check-prerequisites.sh deploy.sh
./check-prerequisites.sh    # Verifica dependências
./deploy.sh                 # Deploy automático
```

# Destruir tudo 

```cd terraform && terraform destroy -auto-approve```

# Ver graficos:

Instalar o Python completo e venv: ```sudo apt install python3-venv python3-pip -y```

Criar um ambiente virtual na pasta do projeto: ```python3 -m venv venv```

Ativar o ambiente virtual: ```source venv/bin/activate```

Instalar dependências dentro do venv: ```pip install pandas seaborn matplotlib```

Rodar o script de gráficos: ```python3 graficos.py```

Rodar o script de metricas: ```python3 metricas.py```

## Observações

O Deploy cria automaticamente um csv e o log do benchmark do tempo do processo

Deletar pasta benchmarks e logs para iniciar um benchmark do zero.

Usar o script loop.sh para rodar o código quantas vezes quiser realizar Deploy com benchmark.

Passar um número como argumento para o número de vezes a ser repetido o Deploy juntamente com benchmark

Exemplo: ```./loop.sh 13```





