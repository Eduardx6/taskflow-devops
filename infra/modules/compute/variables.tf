variable "name" {
  type        = string
  description = "Prefixo dos recursos"
}

variable "instance_type" {
  type        = string
  description = "Tipo da instância"
}

variable "subnet_id" {
  type        = string
  description = "Sub-rede onde a instância será criada"
}

variable "security_group_id" {
  type        = string
  description = "Security group da instância"
}

variable "app_port" {
  type        = number
  description = "Porta da aplicação"
}

variable "docker_image" {
  type        = string
  description = "Imagem Docker a ser executada"
}
