document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("pre-modal");
    const openBtn = document.getElementById("open-pre");
    const closeBtn = document.getElementById("close-modal");

    const toggleModal = (state) => {
        if (modal) modal.style.display = state;
    };

    if (openBtn) {
        openBtn.addEventListener("click", (e) => {
            e.preventDefault();
            toggleModal("flex");
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener("click", () => toggleModal("none"));
    }

    // Fechar ao clicar fora do conteúdo ou apertar ESC
    window.addEventListener("click", (e) => {
        if (e.target === modal) toggleModal("none");
    });

    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") toggleModal("none");
    });
});