variable "name" {
  type        = string
  description = "Prefixo dos recursos"
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR da VPC"
}

variable "public_subnet_cidr" {
  type        = string
  description = "CIDR da sub-rede pública"
}

variable "app_port" {
  type        = number
  description = "Porta da aplicação"
}

variable "allowed_ssh_cidr" {
  type        = string
  description = "CIDR autorizado para SSH"
}
