terraform {
  backend "s3" {
    bucket = "shop-tfstate"
    key    = "state/terraform.tfstate"
    region = "eu-central-1"
  }
}
