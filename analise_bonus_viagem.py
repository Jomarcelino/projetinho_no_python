import pandas as pd;
from twilio.rest import Client;
# Your Account SID from twilio.com/console
account_sid = "AC361fdb1d922932f54e24ea06cbfe38db"
# Your Auth Token from twilio.com/console
auth_token  = "02b855d039b79e151ee96a9734b75011"
client = Client(account_sid, auth_token)

#instalar o pandas, twilio, openpyxl

# passo a passo das vendas

#abrir a planilha e comparar as vendas
tabela_vendas = pd.read_excel('janeiro.xlsx');

# print(tabela_vendas);

if (tabela_vendas['vendas'] >= 11000).any():
    funcionario = tabela_vendas.loc[tabela_vendas['vendas'] >= 11000, 'funcionario'].values[0]
    vendas = tabela_vendas.loc[tabela_vendas['vendas'] >= 11000, 'vendas'].values[0]
    print(f'o vendedor: {funcionario}, bateu a meta com: {vendas} em vendas');
    message = client.messages.create(
        to="+5515974024147", 
        from_="+5515974078545",
        body=f'o vendedor: {funcionario}, bateu a meta com: {vendas} em vendas')

    print(message.sid)




#se as vendas forem maiores que 10.000:
#se o valor for maior que 10.000 envia um sms com o nome e a venda dele
#caso o valor nao atinja a meta, nao fazer nada
