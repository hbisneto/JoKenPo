## SplashScreen File
## This file contains information about your project

from datetime import date

CurrentYear = date.today().year
SoftwareName = "JoKenPô"
Version = "2.0"
CopyrightName = "Heitor Bisneto"

print("Name:", SoftwareName)
print("Version:", Version)
print("Created By:", CopyrightName)

if CurrentYear == 2021:
   print("Copyright ©", CurrentYear, "|", CopyrightName, "All rights reserved.")
else:
   print("Copyright © 2021 -", CurrentYear, "|", CopyrightName, "All rights reserved.")

print("=" * 80)
print(f'[{SoftwareName} for Windows] - Running...')
print("=" * 80)
print()
