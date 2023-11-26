import subprocess

# Replace this with the actual path to your Jupyter notebook file
notebook_path = "hadamard_gate.ipynb"

# Command to convert the notebook to HTML using nbconvert
command = f"wsl jupyter nbconvert --to html {notebook_path}"

# Run the command
subprocess.run(command, shell=True)
