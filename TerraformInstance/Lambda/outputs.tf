output "lambda_function_name" {
  description = "The name of the Lambda function"
  value       = aws_lambda_function.example_lambda.function_name
}
