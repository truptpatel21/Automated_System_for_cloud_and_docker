import subprocess
import os

def launch_instance():
    # Change directory to TerraformInstance directory
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    
    # Run terraform init, plan, and apply
    try:
        # Initialize Terraform (only needed the first time or if you modify providers)
        subprocess.run(["terraform", "init"], check=True)
        
        # Create an execution plan
        subprocess.run(["terraform", "plan", "-out=tfplan"], check=True)
        
        # Apply the execution plan to create resources
        subprocess.run(["terraform", "apply", "tfplan"], check=True)
        
        return "AWS instance launched successfully."
    
    except subprocess.CalledProcessError as e:
        return f"Error launching instance: {e}"
