variable "aws_region" {
  description = "Região AWS onde a infraestrutura será criada"
  type        = string
  default     = "sa-east-1"
}

variable "project_name" {
  description = "Nome do projeto (usado como prefixo dos recursos)"
  type        = string
  default     = "taskflow"
}

variable "environment" {
  description = "Ambiente (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR da VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR da sub-rede pública"
  type        = string
  default     = "10.0.1.0/24"
}

variable "instance_type" {
  description = "Tipo da instância EC2"
  type        = string
  default     = "t3.micro"
}

variable "allowed_ssh_cidr" {
  description = "CIDR autorizado a acessar a porta 22 (restrinja ao seu IP, ex.: 200.1.2.3/32)"
  type        = string
  default     = "127.0.0.1/32"
}

variable "app_port" {
  description = "Porta em que a aplicação escuta"
  type        = number
  default     = 8000
}

variable "docker_image" {
  description = "Imagem Docker da aplicação executada na EC2"
  type        = string
  default     = "ghcr.io/SEU-USUARIO/taskflow-api:latest"
}
