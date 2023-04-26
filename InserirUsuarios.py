#!/usr/bin/env python3 

import subprocess 

#define o nome de usuário e senha do novo usuário 

new_user_name = "mirella"
new_user_password = "020604"

#cria o usuário no sistema linux 

subprocess.run(["sudo","useradd",new_user_name])
subprocess.run(["sudo","passwd",new_user_name], input=f"{new_user_passwsugit addord}\n{new_user_password}\n".encode())
