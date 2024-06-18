import zipfile

def create_lambda_zip():
    with zipfile.ZipFile('lambda_function.zip', 'w') as zf:
        zf.write('lambda_function.py')

if __name__ == "__main__":
    create_lambda_zip()
