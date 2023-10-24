terraform {
  backend "s3" {
    bucket         = "shop-tfstate"
    key            = "state/terraform.tfstate"
    region         = var.aws_default_region
    ecnrypt        = true
    dynamodb_table = "shop_tf_lockid"
  }
}
