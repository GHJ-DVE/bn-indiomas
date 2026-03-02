from flask import Flask, render_template, request, redirect, url_for, flash

# CONFIGURAÇÃO CORRETA:
# static_url_path='' é essencial quando os arquivos estão na raiz para o CSS carregar
app = Flask(__name__, 
            template_folder='.', 
            static_folder='.', 
            static_url_path='')

# Chave necessária para o funcionamento das mensagens de alerta (flash)
app.config["SECRET_KEY"] = "bn_idiomas_2026_secret"

# --- BANCO DE DADOS FICTÍCIO ---
matriculas_simuladas = [
    {"nome": "João Silva", "whatsapp": "(88) 99887-6655", "curso": "Adulto", "data": "28/02/2026"},
    {"nome": "Maria Oliveira", "whatsapp": "(88) 98877-2233", "curso": "Infantil", "data": "27/02/2026"}
]
mensagens_simuladas = []

# --- ROTAS ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quem-somos")
def quem_somos():
    return render_template("quem_somos.html")

@app.route("/area-estudante")
def area_estudante():
    return render_template("area_estudante.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

@app.route("/pagina_infantil")
def pagina_infantil():
    return render_template("pagina_infantil.html")

@app.route("/pagina_adulto")
def pagina_adulto():
    return render_template("pagina_adulto.html")

@app.route("/teste-nivel")
def teste_nivel():
    return render_template("teste_nivel.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("pass")
        if user == "admin" and password == "123":
            flash("Bem-vindo ao Painel Administrativo!", "success")
            return redirect(url_for("adm")) 
        else:
            flash("Usuário ou senha inválidos.", "error")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/adm")
def adm():
    return render_template("adm.html", matriculas=matriculas_simuladas, mensagens=mensagens_simuladas)

@app.route("/logout")
def logout():
    flash("Sessão encerrada.", "success")
    return redirect(url_for("login"))

@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form.get("nome")
        flash(f"Obrigado {nome}, mensagem enviada!", "success")
        return redirect(url_for("contato"))
    return render_template("contato.html")

@app.route("/pre-matricula")
def pre_matricula():
    return render_template("pre_matricula.html")

@app.route("/enviar-pre-matricula", methods=["POST"])
def enviar_pre_matricula():
    nome = request.form.get("nome")
    whatsapp = request.form.get("whatsapp") 
    curso = request.form.get("curso")
    nova_matricula = {"nome": nome, "whatsapp": whatsapp, "curso": curso, "data": "28/02/2026"}
    matriculas_simuladas.append(nova_matricula)
    flash(f"Sucesso! Pré-matrícula de {nome} recebida.", "success")
    return redirect(url_for("index"))

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    # O app.run deve ser a última coisa. 
    # Removida a linha duplicada que estava abaixo dele.
    app.run(debug=True)