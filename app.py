from flask import Flask, render_template, request, flash, redirect, url_for
import pandas as pd
import yagmail
import os

app = Flask(__name__)
app.secret_key = "chave_secreta_para_mensagens" # Necessário para usar o 'flash'

# --- CONFIGURAÇÕES ---
EMAIL_USER = "seu-email@gmail.com"
EMAIL_PASS = "sua-senha-de-app"  # Use a 'Senha de App' do Google, não a senha comum
PASTA_DADOS = 'data'
ARQUIVO_CSV = os.path.join(PASTA_DADOS, 'leads.csv')

# Garante que a pasta 'data' exista antes de tentar salvar qualquer arquivo
if not os.path.exists(PASTA_DADOS):
    os.makedirs(PASTA_DADOS)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    # 1. Coleta os dados do formulário
    nome = request.form.get('nome')
    email = request.form.get('email')
    whatsapp = request.form.get('whatsapp')

    # Validação básica
    if not nome or not email:
        return "<h1>Erro: Nome e E-mail são obrigatórios!</h1>", 400

    # 2. Salva no CSV usando Pandas
    try:
        dados = {"Nome": [nome], "Email": [email], "Whatsapp": [whatsapp]}
        df = pd.DataFrame(dados)
        
        # 'header=not os.path.exists' cria o cabeçalho apenas se o arquivo for novo
        df.to_csv(ARQUIVO_CSV, mode='a', index=False, header=not os.path.exists(ARQUIVO_CSV))
    except Exception as e:
        print(f"Erro ao salvar no CSV: {e}")
        return "<h1>Erro interno ao salvar os dados.</h1>", 500

    # 3. Envio do E-mail
    try:
        yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASS)
        corpo_email = f"""
        <h2>Novo Lead Capturado!</h2>
        <p><b>Nome:</b> {nome}</p>
        <p><b>Email:</b> {email}</p>
        <p><b>WhatsApp:</b> {whatsapp}</p>
        """
        yag.send(
            to=EMAIL_USER, 
            subject=f"Novo Lead - {nome}", 
            contents=corpo_email
        )
    except Exception as e:
        # Se o e-mail falhar, o lead ainda foi salvo no CSV. 
        # Logamos o erro no terminal para você ver.
        print(f"Erro ao enviar e-mail: {e}")

    return "<h1>Enviado com sucesso!</h1><p>Obrigado pelo contato.</p><a href='/'>Voltar</a>"

if __name__ == '__main__':
    # 'debug=True' é ótimo para desenvolvimento, mas desative em produção.
    app.run(debug=True)