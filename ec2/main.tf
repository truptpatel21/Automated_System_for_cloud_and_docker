provider "aws" {
  region = "ap-south-1"  # Replace with your desired AWS region
    # Replace with your AWS profile name

}

resource "aws_instance" "example" {
  ami           = "ami-0e1d06225679bc1c5"  # Replace with your desired AMI ID
  instance_type = "t2.micro"                # Replace with your desired instance type

  tags = {
    Name = "pravesh"
  }
}
