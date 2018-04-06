import subprocess

subprocess.run(["python", "-m", "unittest", "discover"],stdout=subprocess.PIPE)