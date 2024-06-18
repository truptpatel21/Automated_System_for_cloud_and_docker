output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.example_vpc.id
}

output "subnet_id" {
  description = "The ID of the subnet"
  value       = aws_subnet.example_subnet.id
}
