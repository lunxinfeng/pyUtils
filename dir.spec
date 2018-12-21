# -*- mode: python -*-

block_cipher = None

dirName = 'project'
exeName = 'start'

a = Analysis(['gui\\__init__.py'],
             pathex=['C:\\workspace\\pyUtils'],
             binaries=[],
             datas=[('gui\\ui.css','.'),('gui\\img','img')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=exeName,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='e:\\photo.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=dirName)
