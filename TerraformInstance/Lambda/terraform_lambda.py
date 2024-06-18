import subprocess
import os
from ..common import run_terraform

def create_lambda_function():
    # Change directory to TerraformInstance/lambda directory
    # os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lambda'))

    script_dir = os.path.dirname(os.path.realpath(__file__))
    s3_dir = os.path.join(script_dir, '../Lambda')
    os.chdir(s3_dir)
    
    return run_terraform()
