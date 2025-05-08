# main.py

import conversion

dollars = -10
try:
    dirhams = conversion.dollars_to_dirhams(dollars)
    print(f"{dollars} dollars valent {dirhams} dirhams.")
except ValueError as e:
    print(e)
    
meters = 2000
try:
    kilometers = conversion.meters_to_kilometers(meters)
    print(f"{meters} mètres valent {kilometers} kilomètres.")
except ValueError as e:
    print(e)