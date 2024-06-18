from flask import Flask, render_template, request
from genai_docker import handle_docker_automation
from TerraformInstance.terraform_instance import launch_instance
from TerraformInstance.S3_Buckets import terraform_s3
from TerraformInstance.Lambda  import terraform_lambda
from TerraformInstance.Vpc import terraform_vpc

from Jenkins_Pipeline.jenkins_pipeline import handle_jenkins

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    option = request.form['automation_option']
    if option == 'docker':
        docker_image_name = request.form['docker_image_name']
        docker_container_name = request.form['docker_container_name']
        result = handle_docker_automation(docker_image_name, docker_container_name)
    elif option == 'terraform':
        result = launch_instance()
    elif option == 's3':
        result = terraform_s3.create_s3_bucket()
    elif option == 'lambda':
        result = terraform_lambda.create_lambda_function()
    elif option == 'vpc':
        result = terraform_vpc.create_vpc()
    elif option == 'jenkins':
        result = handle_jenkins()
    else:
        result = "Invalid option selected."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
