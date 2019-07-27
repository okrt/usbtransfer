# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['start.py'],
             pathex=['C:\\Users\\oguz\\projects\\usbtransfer'],
             binaries=[('dd.exe','.')],
             datas=[ ('lang', 'lang') ,('qt', 'qt'), ('ts', 'ts')  ],
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
          name='USBTransfer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , uac_admin=True, icon='main.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='start')
