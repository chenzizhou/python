# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['dd_morning.py'],
    pathex=[],
    binaries=[],
    datas=[],    hiddenimports=['xlrd2','selenium','urllib3','httplib2','certifi','appium','queue','__future__','datetime','hmac','platform','appium.webdriver','selenium.common','chinese_calendar','chinese_calendar.is_workday','selenium.webdriver.common.by.By','selenium.webdriver.support','selenium.webdriver.support.expected_conditions'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='dd_morning',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='dd_morning',
)
