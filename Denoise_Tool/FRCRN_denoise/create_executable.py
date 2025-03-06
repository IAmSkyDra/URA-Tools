import PyInstaller.__main__

PyInstaller.__main__.run([
    'interface.py',
    '--onefile',
    '--windowed',
    '--name=DenoiseTool'
])
