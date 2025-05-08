# conversion.py

def dollars_to_dirhams(dollars):
    if(dollars < 0):
        raise ValueError("La valeure ne doit pas étre negative.")
    else:
        return dollars * 9.8

def meters_to_kilometers(meters):
    if(meters < 0):
        raise ValueError("La valeure ne doit pas étre negative.")
    else:
        return meters / 1000.0
