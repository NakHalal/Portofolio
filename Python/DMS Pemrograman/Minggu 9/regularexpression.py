import re

password = input()

if re.match(".2*[a-zA-Z].*",password) and re.match(".*[0-9].*",password) and re.match(".*[\.!@#\$].*",password

"""untuk huruf butuh lebih dari 1 huruf untuk mencukupi"""
):
    print("kuat")
else:
    print("lemah")