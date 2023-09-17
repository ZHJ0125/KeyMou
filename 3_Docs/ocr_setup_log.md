## 环境配置记录

### 1. 安装 cnocr

1. 安装 cnocr

```powershell
PS C:\Users\ZHJ> pip install cnocr
Collecting cnocr
  Obtaining dependency information for cnocr from https://files.pythonhosted.org/packages/e9/9c/715d86820c108df4dfeec59d2115c110ea94fdb4406e27da03a403104da1/cnocr-2.2.3.2-py3-none-any.whl.metadata
  Using cached cnocr-2.2.3.2-py3-none-any.whl.metadata (17 kB)
Collecting click (from cnocr)
....... 省略显示内容 .......
Building wheels for collected packages: Polygon3
  Building wheel for Polygon3 (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for Polygon3 (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [14 lines of output]
      NumPy extension not found - disabling support for it!
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-cpython-311
      creating build\lib.win-amd64-cpython-311\Polygon
      copying Polygon\IO.py -> build\lib.win-amd64-cpython-311\Polygon
      copying Polygon\Shapes.py -> build\lib.win-amd64-cpython-311\Polygon
      copying Polygon\Utils.py -> build\lib.win-amd64-cpython-311\Polygon
      copying Polygon\__init__.py -> build\lib.win-amd64-cpython-311\Polygon
      running build_ext
      building 'Polygon.cPolygon' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for Polygon3
Failed to build Polygon3
ERROR: Could not build wheels for Polygon3, which is required to install pyproject.toml-based projects
```

遇到上述问题，解决办法：安装 [`Microsoft Visual C++ 14.0 or greater`](https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/) （参考资料[1][2]）

```powershell
# 重新 pip install cnocr 遇到以下问题：
Building wheels for collected packages: Polygon3
  Building wheel for Polygon3 (setup.py) ... error
  error: subprocess-exited-with-error

  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [20 lines of output]
      NumPy extension not found - disabling support for it!
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-cpython-311
      creating build\lib.win-amd64-cpython-311\Polygon
      copying Polygon\IO.py -> build\lib.win-amd64-cpython-311\Polygon
      copying Polygon\Shapes.py -> build\lib.win-amd64-cpython-311\Polygon
      copying Polygon\Utils.py -> build\lib.win-amd64-cpython-311\Polygon
      copying Polygon\__init__.py -> build\lib.win-amd64-cpython-311\Polygon
      running build_ext
      building 'Polygon.cPolygon' extension
      creating build\temp.win-amd64-cpython-311
      creating build\temp.win-amd64-cpython-311\Release
      creating build\temp.win-amd64-cpython-311\Release\src
      D:\VisualStudio\install\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DDEFAULT_STYLE=STYLE_LIST -DSYSTEM_WIN32=1 -Isrc -ID:\Python3\install\include -ID:\Python3\install\Include -ID:\VisualStudio\install\VC\Tools\MSVC\14.37.32822\include -ID:\VisualStudio\install\VC\Tools\MSVC\14.37.32822\ATLMFC\include -ID:\VisualStudio\install\VC\Auxiliary\VS\include /Tcsrc/PolyUtil.c /Fobuild\temp.win-amd64-cpython-311\Release\src/PolyUtil.obj
      PolyUtil.c
      C:\Users\ZHJ\AppData\Local\Temp\pip-install-hxncvors\polygon3_650345c58fc348b694d5b6c0c5a86e85\src\gpc.h(36): fatal error C1083: 无法打开包括文件: “stdio.h”: No such file or directory
      error: command 'D:\\VisualStudio\\install\\VC\\Tools\\MSVC\\14.37.32822\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for Polygon3
  Running setup.py clean for Polygon3
Failed to build Polygon3
ERROR: Could not build wheels for Polygon3, which is required to install pyproject.toml-based projects
```

解决方案：去 Visual Stdio Installer 中安装 Windows10 SDK

```powershell
# 安装完成后再次 pip install cnocr

Building wheels for collected packages: Polygon3
  Building wheel for Polygon3 (setup.py) ... done
  Created wheel for Polygon3: filename=Polygon3-3.0.9.1-cp311-cp311-win_amd64.whl size=48513 sha256=f8b07f816416dbcfbdfad21821ef20b41f8a6ebfecedc155fd452c3cfaebba80
  Stored in directory: c:\users\zhj\appdata\local\pip\cache\wheels\ef\fc\31\c070b9a46072680075dfe4bcd910cae8101fed035aceffdd44
Successfully built Polygon3
Installing collected packages: pytz, pyreadline3, pyclipper, Polygon3, mpmath, flatbuffers, urllib3, unidecode, tzdata, typing-extensions, sympy, pyyaml, python-dateutil, pyparsing, protobuf, pillow, packaging, numpy, networkx, multidict, MarkupSafe, kiwisolver, idna, humanfriendly, fsspec, frozenlist, fonttools, filelock, cycler, colorama, charset-normalizer, certifi, attrs, async-timeout, yarl, tqdm, shapely, scipy, requests, pandas, opencv-python, onnx, lightning-utilities, jinja2, contourpy, coloredlogs, click, aiosignal, torch, onnxruntime, matplotlib, huggingface-hub, aiohttp, torchvision, torchmetrics, seaborn, pytorch-lightning, cnstd, cnocr
Successfully installed MarkupSafe-2.1.3 Polygon3-3.0.9.1 aiohttp-3.8.5 aiosignal-1.3.1 async-timeout-4.0.3 attrs-23.1.0 certifi-2023.7.22 charset-normalizer-3.2.0 click-8.1.7 cnocr-2.2.3.2 cnstd-1.2.3.2 colorama-0.4.6 coloredlogs-15.0.1 contourpy-1.1.1 cycler-0.11.0 filelock-3.12.4 flatbuffers-23.5.26 fonttools-4.42.1 frozenlist-1.4.0 fsspec-2023.9.1 huggingface-hub-0.17.1 humanfriendly-10.0 idna-3.4 jinja2-3.1.2 kiwisolver-1.4.5 lightning-utilities-0.9.0 matplotlib-3.8.0 mpmath-1.3.0 multidict-6.0.4 networkx-3.1 numpy-1.26.0 onnx-1.14.1 onnxruntime-1.15.1 opencv-python-4.8.0.76 packaging-23.1 pandas-2.1.0 pillow-10.0.1 protobuf-4.24.3 pyclipper-1.3.0.post5 pyparsing-3.1.1 pyreadline3-3.4.1 python-dateutil-2.8.2 pytorch-lightning-2.0.9 pytz-2023.3.post1 pyyaml-6.0.1 requests-2.31.0 scipy-1.11.2 seaborn-0.12.2 shapely-2.0.1 sympy-1.12 torch-2.0.1 torchmetrics-1.1.2 torchvision-0.15.2 tqdm-4.66.1 typing-extensions-4.7.1 tzdata-2023.3 unidecode-1.3.6 urllib3-2.0.4 yarl-1.9.2
```

### 2. 安装 Pillow

```powershell
PS C:\Users\ZHJ\Desktop\KeyMou> python3 -m pip install --upgrade pip
PS C:\Users\ZHJ\Desktop\KeyMou> python3 -m pip install --upgrade Pillow
```

### 参考资料

* [1] Not able to install OCRPaddle for WIndows - [stackoverflow](https://stackoverflow.com/questions/74132102/not-able-to-install-ocrpaddle-for-windows)
* [2] 【python】pip installの際に「error: Microsoft Visual C++ 14.0 is required」が発生した場合の対応方法 - [PythonTech](https://tech.nkhn37.net/python-pip-install-error-microsoft-visual-c-14/)
