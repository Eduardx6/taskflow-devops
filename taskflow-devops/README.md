# TaskFlow API – DevOps na Prática (Fase 1)

API REST simples de gerenciamento de tarefas, usada como base para praticar integração contínua (GitHub Actions) e infraestrutura como código (Terraform / AWS).

## Estrutura

```
app/                  Aplicação Flask
tests/                Testes automatizados (pytest)
Dockerfile            Imagem da aplicação
.github/workflows/    Pipeline de CI (GitHub Actions)
infra/                Terraform (módulos network e compute + bucket S3)
```

## Executar localmente

```bash
pip install -r requirements-dev.txt
flake8 .
pytest --cov=app
python -m app.main        # http://localhost:8000/health
```

## Endpoints

| Método | Rota             | Descrição                         |
|--------|------------------|-----------------------------------|
| GET    | /health          | Verificação de saúde              |
| GET    | /tasks           | Lista tarefas (`?status=`)        |
| POST   | /tasks           | Cria tarefa (`{"title": "..."}`)  |
| GET    | /tasks/{id}      | Consulta tarefa                   |
| PATCH  | /tasks/{id}      | Altera status                     |
| DELETE | /tasks/{id}      | Remove tarefa                     |

## Pipeline de CI

`.github/workflows/ci.yml` roda em todo push/PR na `main`: lint (flake8) e testes com cobertura mínima de 80% (Python 3.11 e 3.12), build da imagem Docker com smoke test e `terraform fmt/validate`.

## Infraestrutura (Terraform)

```bash
cd infra
cp terraform.tfvars.example terraform.tfvars   # ajuste seu IP e a imagem
terraform init
terraform plan
terraform apply
```

Cria VPC, sub-rede pública, Internet Gateway, Security Group, uma EC2 que executa o container e um bucket S3 (versionado, criptografado e privado). Use `terraform destroy` ao terminar para evitar custos.
