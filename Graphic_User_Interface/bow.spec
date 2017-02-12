# -*- mode: python -*-

block_cipher = None


a = Analysis(['bow_mainwindow.py'],
             pathex=['C:\\Users\\Pierre\\Documents\\ENPC\\3. 2A\\3. S3\\2. TDLOG\\Projet Bag of Words\\Projet-BoW\\GUI'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='bow_mainwindow',
          debug=False,
          strip=False,
          upx=True,
          console=False )
