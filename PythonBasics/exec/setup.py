from cx_Freeze import setup, Executable

setup(name='DistBeta',
      version='0.1',
      description='Parse Stuff',
      executables=[Executable("dist.py")])
