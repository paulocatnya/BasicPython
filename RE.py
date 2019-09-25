
# ----------- REGULAR EXPRESSION ----------------REGEX101.COM#
import re
print(r'oi\ngalera')
strTeste = 'Era uma alguel vez alguem  que ja nao era da vez, gatos, gatas, gatinhos, gatoes gatilho gataaaap bacaaaa' 
emails = 'po-po@rbr.com sa.pook@fe.com smdsn22@sok.com.br soaksaok sokaosk appa pp@hotmail.com.br pau.lo.rob@hotmaill.com'

padrao = re.search(r'algue\w',strTeste)
padrao1 = re.search(r'algue.',strTeste)
padrao2 = re.search(r'\w\w',strTeste)
padrao3 = re.findall(r'gat\w',strTeste)
padrao4 = re.findall(r'gat\w+',strTeste)
padrao5 = re.findall(r'gat\w*',strTeste)
padrao6 = re.findall(r'[gat]+',strTeste)
padrao7 = re.findall(r'\w{4,6}',strTeste)
padrao8 = re.findall(r'a{3}',strTeste)
padrao9 = re.findall(r'[\w.-]+@+\w+\.+\w+[.\w*.]+[\w]',emails)

if padrao:
    print(padrao.group())
    print(padrao1.group())
    print(padrao2.group())
    print(padrao3)
    print(padrao4)
    print(padrao5)
    print(padrao6)
    print(padrao7)
    print(padrao9)
else:
    print('nao achei')








