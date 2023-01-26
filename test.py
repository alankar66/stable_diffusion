import subprocess

command = 'python train.py --config train.json'
output = subprocess.run(command, shell=True, capture_output=True)
print(output.stdout.decode())

print("subprocess running")