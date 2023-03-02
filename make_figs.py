import subprocess

files = [
    'fig_BP_norm',
    'fig_GMRES_convergence',
    'fig_numerical_range',
    'fig_resolvent_norm',
]

for file in files:
    subprocess.run(f'jupyter nbconvert --execute --to notebook --inplace --allow-errors --ExecutePreprocessor.timeout=-1 {file}.ipynb',shell=True)

