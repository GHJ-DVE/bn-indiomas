from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# Chave necessária para o funcionamento das mensagens de alerta (flash)
app.config["SECRET_KEY"] = "bn_idiomas_2026_secret"

# --- BANCO DE DADOS FICTÍCIO (Dados que aparecerão no Painel ADM) ---
matriculas_simuladas = [
    {"nome": "João Silva", "whatsapp": "(88) 99887-6655", "curso": "Adulto", "data": "28/02/2026"},
    {"nome": "Maria Oliveira", "whatsapp": "(88) 98877-2233", "curso": "Infantil", "data": "27/02/2026"}
]

# Lista de mensagens (vazia por enquanto para o contador mostrar 0)
mensagens_simuladas = []

# --- ROTA DA PÁGINA INICIAL ---
@app.route("/")
def index():
    return render_template("index.html")

# --- INSTITUCIONAL E CONTEÚDO ---
@app.route("/quem-somos")
def quem_somos():
    return render_template("quem_somos.html")

@app.route("/area-estudante")
def area_estudante():
    return render_template("area_estudante.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

# --- ROTAS DE CURSOS ---
@app.route("/pagina_infantil")
def pagina_infantil():
    return render_template("pagina_infantil.html")

@app.route("/pagina_adulto")
def pagina_adulto():
    return render_template("pagina_adulto.html")

# --- TESTE DE NÍVEL ---
@app.route("/teste-nivel")
def teste_nivel():
    return render_template("teste_nivel.html")

# --- ROTA DE LOGIN (Redireciona para o ADM) ---
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("pass")
        
        # Simulação de login administrativo
        if user == "admin" and password == "123":
            flash("Bem-vindo ao Painel Administrativo!", "success")
            return redirect(url_for("adm")) 
        else:
            flash("Usuário ou senha inválidos.", "error")
            return redirect(url_for("login"))
            
    return render_template("login.html")

# --- ROTA ADMINISTRATIVA ---
@app.route("/adm")
def adm():
    """Painel de controle com dados de matrículas e mensagens."""
    return render_template("adm.html", 
                           matriculas=matriculas_simuladas, 
                           mensagens=mensagens_simuladas)

# --- LOGOUT ---
@app.route("/logout")
def logout():
    flash("Sessão encerrada.", "success")
    return redirect(url_for("login"))

# --- ROTA DE CONTATO ---
@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form.get("nome")
        # Aqui você poderia dar um .append na lista mensagens_simuladas
        flash(f"Obrigado {nome}, mensagem enviada!", "success")
        return redirect(url_for("contato"))
    return render_template("contato.html")

# --- ROTAS DE PRÉ-MATRÍCULA ---
@app.route("/pre-matricula")
def pre_matricula():
    return render_template("pre_matricula.html")

@app.route("/enviar-pre-matricula", methods=["POST"])
def enviar_pre_matricula():
    nome = request.form.get("nome")
    whatsapp = request.form.get("whatsapp") 
    curso = request.form.get("curso")
    
    # Simula salvar a matrícula para aparecer no ADM em tempo real (apenas nesta sessão)
    nova_matricula = {"nome": nome, "whatsapp": whatsapp, "curso": curso, "data": "28/02/2026"}
    matriculas_simuladas.append(nova_matricula)
    
    flash(f"Sucesso! Pré-matrícula de {nome} recebida.", "success")
    return redirect(url_for("index"))

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    app.run(debug=True)