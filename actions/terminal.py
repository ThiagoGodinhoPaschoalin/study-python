import subprocess

# Comando para abrir o PowerShell e executar um comando
comando = 'powershell.exe -NoExit -Command "streamlit run app.py"'

# Executar o comando
subprocess.run(comando)
