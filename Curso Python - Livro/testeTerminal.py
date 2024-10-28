import subprocess

def comando(x):
    subprocess.run(x, shell=True, check=True)

comando(['rmdir', 'teste pasta'])

input("Enter para finalizar")