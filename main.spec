# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas = [
        ('assets/backgrounds/graveyard.jpg', 'assets/backgrounds'),
        ('assets/sprites/skeleton.png', 'assets/sprites'),
        ('assets/sprites/skull.png', 'assets/sprites'),
        ('assets/sprites/pumpkin.png', 'assets/sprites'),
        ('assets/WhatsThis.ogg', 'assets'),
        ('assets/fonts/Bangers-Regular.ttf', 'assets/fonts'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
