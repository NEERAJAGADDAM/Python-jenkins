import os
import subprocess

os.makedirs("reports", exist_ok=True)

subprocess.run(["pytest", "--junitxml=reports/results.xml"])