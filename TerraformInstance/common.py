import subprocess

def run_terraform():
    try:
        # Initialize Terraform (only needed the first time or if you modify providers)
        subprocess.run(["terraform", "init"], check=True)
        
        # Create an execution plan
        subprocess.run(["terraform", "plan", "-out=tfplan"], check=True)
        
        # Apply the execution plan to create resources
        subprocess.run(["terraform", "apply", "tfplan"], check=True)
        
        return "Terraform operation completed successfully."
    
    except subprocess.CalledProcessError as e:
        return f"Error during Terraform operation: {e}"
