from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica


pf = PessoaFisica('125.815.146-47', nome='Paulo',idade=23)
pj = PessoaJuridica('120.335.876.81', nome='Cia LTDA', idade=10)


print (pf.getCPF())
print (pf.getNome())
print (pf.getIdade())

print('\n-------Empresa-------\n')
print (pj.getCNPJ())
print (pj.getNome())
pj.setNome('CIA2')
print (pj.getNome())
print (pj.getIdade())
