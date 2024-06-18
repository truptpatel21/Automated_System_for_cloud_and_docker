import paramiko

def execute_docker_commands(commands):
    # SSH configuration
    host = '13.233.87.241'
    port = 22
    username = 'ec2-user'
    key_file = 'tp.pem'

    # Initialize SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the server
        ssh.connect(host, port, username, key_filename=key_file)
        
        # Execute each command
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            if error:
                return f"Error: {error}"
            print(output)
        
        return "Docker commands executed successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    finally:
        ssh.close()
