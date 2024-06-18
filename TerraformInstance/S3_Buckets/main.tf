provider "aws" {
  region = "ap-south-1"  # Replace with your desired AWS region
}

resource "random_string" "bucket_suffix" {
  length  = 8
  special = false
}

resource "aws_s3_bucket" "example_bucket" {
  bucket = "pravesh73737"
  acl    = "private"

  tags = {
    Name        = "ExampleBucket"
    Environment = "Dev"
  }
}
