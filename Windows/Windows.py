﻿## Windows File
## This file is used to implement code used to run scripts for Windows
## Codes implemented here, will run before the script starts running.

import os
from Windows import FileSystem

def Windows():
   ## NOTE: You can use this function
   ## To load information before the app starts running

   ## Lets run the SplashScreen
   from Windows import SplashScreen

   ## Lets check system requirements
   from ErrorReport import SystemRequirements

   ## Start App for Windows
   from Windows import WindowsApp

