document.addEventListener("DOMContentLoaded", () => {
    const popup = document.getElementById("popupOverlay");
    const editBtn = document.getElementById("editBtn");
    const closeBtn = document.getElementById("closeBtn");
    const deleteBtn = document.getElementById("deletebtn");

    const livroId = "{{ livro[0] }}"; // Passando o id do livro para o JS

    // ---------- Abrir popup ----------
    editBtn.addEventListener("click", () => {
        popup.classList.add("active");
        document.body.style.overflow = "hidden";
    });

    // ---------- Fechar popup ----------
    closeBtn.addEventListener("click", () => {
        popup.classList.remove("active");
        document.body.style.overflow = "auto";
    });

    popup.addEventListener("click", (e) => {
        if (e.target === popup) {
            popup.classList.remove("active");
            document.body.style.overflow = "auto";
        }
    });

    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && popup.classList.contains("active")) {
            popup.classList.remove("active");
            document.body.style.overflow = "auto";
        }
    });

    // ---------- Botão Excluir ----------
    deleteBtn.addEventListener("click", () => {
        if (confirm("Tem certeza que deseja excluir este livro?")) {
            fetch(`/excluir_livro/${livroId}`, {
                method: "DELETE"
            })
            .then(response => {
                if (response.ok) {
                    alert("Livro excluído com sucesso!");
                    window.location.href = "{{ url_for('minhaconta_view') }}"; // Redireciona
                } else {
                    alert("Erro ao excluir o livro.");
                }
            })
            .catch(err => {
                console.error(err);
                alert("Erro ao excluir o livro.");
            });
        }
    });
});
