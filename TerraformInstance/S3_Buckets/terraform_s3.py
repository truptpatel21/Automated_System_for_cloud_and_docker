import subprocess
import os
from .common import run_terraform

def create_s3_bucket():
    # Change directory to TerraformInstance/s3 directory
    # os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), 's3'))
    script_dir = os.path.dirname(os.path.realpath(__file__))
    s3_dir = os.path.join(script_dir, '../S3_Buckets')
    os.chdir(s3_dir)
    
    return run_terraform()
