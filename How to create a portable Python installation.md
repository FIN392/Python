# How to create a portable Python installation on Windows

The goal is to get the Python installation into a folder that can be distributed along with your scripts to ensure that you can package it all together and get it working on another computer without having to pre-install Python or any modules or packages.

Python itself is distributed under the Python Software Foundation License (PSFL). This is a permissive open-source license, meaning it allows you to:
- Use Python for any purpose: including commercial use.
- Modify the Python source code: and distribute your modified versions.
- Distribute Python: in both source code and binary forms.

If you are going to add additional third-party packages or modules, please check their licenses before distributing.

## Requirements

- A computer with Windows
- Internet access (to download Python and other packages).
- Your fancy Python script. If you don't have any, use this one:

```Python
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def main():
    
    root = ttk.Window( title="Hello, World! with TkBootstrap", themename="darkly" )
    root.geometry( "300x150" )

    output_label = ttk.Label( root, text="Hello, World!", font=( "Helvetica", 16 ) )
    output_label.pack( pady=20 )

    root.mainloop()

if __name__ == '__main__':
    main()
```

## Steps

1. [Create folder structure](#folders).
2. [Install Python](#python).
3. [Installa additional packages](#pip).
4. [Create a Python script](#script).
5. [Test and go live](#test).

## <a name="folders"></a>1. Create folder structure.

This is the folder structure I suggest:

> 📁 myPythomApplication  
> ├── 📁 Python  
> └── 📁 Scripts

## <a name="python"></a>2. Install Python.

>[!WARNING]
>Use ONLY files downloaded from https://www.python.org/. This way you will avoid possible trojans, viruses, malwares, spam and other modern evils.


En la sección _Downloads / Windows_ 

## <a name="pip"></a>3. Installa additional packages.

x

## <a name="script"></a>4. Create a Python script.

x

## <a name="test"></a>5. Test and go live.

x


