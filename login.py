
print("====== Login======")
user=input('Informe seu usuario: ')
senha = input('Informe sua senha: ')

if(user == "admin" and senha=="admin"):
    print('Bem vindo! , {} ,\n (Privilegio: [ADM])'.format(user))
    print('|user|> {}  |password| > ****** '.format(user))
    print("--- Senha Descriptografada ---")
    print(senha)
elif(user!='' and senha !="" or senha=='admin' or user=='admin') :
    print("Bem vindo!, {} ,\n (Privilegio: [Usuario Padrao])".format(user))   
    print('|user|> {}  |password| > ****** '.format(user))
    print("--- Senha Descriptografada ---")
    print(senha)
elif(user=="" or senha==""):
    print("ERROR")    
print('=============================')
