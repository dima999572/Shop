locals {
  instance_types = ["t2.micro"]
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.17.2"

  cluster_name                   = var.shop_cluster_name
  cluster_endpoint_public_access = true

  cluster_addons = {
    aws-ebs-csi-driver = {
      most_recent = true
    }
    coredns = {
      most_recent = true
    }
    kube-proxy = {
      most_recent = true
    }
    vpc-cni = {
      most_recent = true
    }
  }

  vpc_id                   = module.vpc.vpc_id
  subnet_ids               = module.vpc.private_subnets
  control_plane_subnet_ids = module.vpc.intra_subnets

  # EKS Managed Node Group(s)
  eks_managed_node_group_defaults = {
    ami_type       = "AL2_x86_64"
    instance_types = local.instance_types

    attach_cluster_primary_security_group = true
  }

  eks_managed_node_groups = {
    shop-cluster-wg = {
      min_size     = 1
      max_size     = 2
      desired_size = 1

      instance_types = local.instance_types
      capacity_type  = "SPOT"
      tags = {
        ExtraTag = "HelloWorld"
      }
    }
  }
}
