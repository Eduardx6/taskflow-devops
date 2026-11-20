module "network" {
  source = "./modules/network"

  name               = "${var.project_name}-${var.environment}"
  vpc_cidr           = var.vpc_cidr
  public_subnet_cidr = var.public_subnet_cidr
  app_port           = var.app_port
  allowed_ssh_cidr   = var.allowed_ssh_cidr
}

module "compute" {
  source = "./modules/compute"

  name              = "${var.project_name}-${var.environment}"
  instance_type     = var.instance_type
  subnet_id         = module.network.public_subnet_id
  security_group_id = module.network.app_security_group_id
  app_port          = var.app_port
  docker_image      = var.docker_image
}

# Bucket para artefatos de build e logs do pipeline
resource "aws_s3_bucket" "artifacts" {
  bucket_prefix = "${var.project_name}-${var.environment}-artifacts-"
}

resource "aws_s3_bucket_versioning" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "artifacts" {
  bucket                  = aws_s3_bucket.artifacts.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
