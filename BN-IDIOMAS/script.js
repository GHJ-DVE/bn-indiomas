/* =========================================
   LÓGICA DO MODAL DE PRÉ-MATRÍCULA
   ========================================= */
document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("pre-modal");
    const openBtn = document.getElementById("open-pre");
    const closeBtn = document.getElementById("close-modal");

    // Função para abrir/fechar o modal
    const toggleModal = (state) => {
        if (modal) {
            modal.style.display = state;
            // Opcional: focar no primeiro campo ao abrir
            if (state === "flex") {
                const firstInput = modal.querySelector("input");
                if (firstInput) firstInput.focus();
            }
        }
    };

    // Abrir modal ao clicar no botão (ex: botão de pré-matrícula na navbar)
    if (openBtn) {
        openBtn.addEventListener("click", (e) => {
            e.preventDefault();
            toggleModal("flex");
        });
    }

    // Fechar modal ao clicar no 'X'
    if (closeBtn) {
        closeBtn.addEventListener("click", () => toggleModal("none"));
    }

    // Fechar ao clicar fora do conteúdo branco (no fundo escurecido)
    window.addEventListener("click", (e) => {
        if (e.target === modal) {
            toggleModal("none");
        }
    });

    // Fechar ao apertar a tecla ESC
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
            toggleModal("none");
        }
    });
});