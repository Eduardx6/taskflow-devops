output "app_public_ip" {
  description = "IP público da instância"
  value       = module.compute.public_ip
}

output "app_url" {
  description = "URL da aplicação"
  value       = "http://${module.compute.public_ip}:${var.app_port}"
}

output "artifacts_bucket" {
  description = "Bucket S3 de artefatos"
  value       = aws_s3_bucket.artifacts.bucket
}
