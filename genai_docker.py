from ssh_docker import execute_docker_commands

def handle_docker_automation(docker_image_name, docker_container_name):
    # Define Dockerfile content as a list of lines
    dockerfile_lines = [
        "FROM python:3.8-slim",
        "RUN pip install flask",
        "COPY . /app",
        "WORKDIR /app",
        'CMD ["python", "app.py"]'
    ]
    
    # Create a command to write the Dockerfile content to a file
    create_dockerfile_commands = [
        f'echo "{line}" > Dockerfile' if i == 0 else f'echo "{line}" >> Dockerfile'
        for i, line in enumerate(dockerfile_lines)
    ]
    
    # Define other commands
    docker_commands = [
        f"docker build -t {docker_image_name} .",
        f"docker run -d -p 5000:5000 --name {docker_container_name} {docker_image_name}",
        "docker ps -a"
    ]
    
    # Combine all commands
    commands = create_dockerfile_commands + docker_commands

    # Execute commands on remote machine and capture output and errors
    output = []
    for command in commands:
        result = execute_docker_commands([command])
        output.append(f"$ {command}\n{result}\n")
    
    # Check if container is running
    if docker_container_name not in output[-1]:
        # If not, fetch logs of the container
        log_command = f"docker logs {docker_container_name}"
        log_result = execute_docker_commands([log_command])
        output.append(f"$ {log_command}\n{log_result}\n")

    return "\n".join(output)
