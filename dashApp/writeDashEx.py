from convertDash import writeLayout
import subprocess
import platform

InputFilename = './assets/externalDash/index.html'
OutPutFilename = './assets/externalDash/dashCodeSecundary.py'



writeLayout(InputFilename= InputFilename, OutPutFilename= OutPutFilename)

if (platform.system() == 'Linux'):
    subprocess.run(["black", f'{OutPutFilename}'])

elif(platform.system() == 'Windows'):
    subprocess.call(f'black {OutPutFilename}')
