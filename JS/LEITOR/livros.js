document.addEventListener("DOMContentLoaded", function() {
    // Inicializa o modal Bootstrap
    const modalElement = document.getElementById('bookDetailsModal');
    const bookModal = new bootstrap.Modal(modalElement);

    function openBookModal(card) {
        const titulo = card.dataset.titulo;
        const preco = card.dataset.preco;
        const descricao = card.dataset.descricao;
        const capa = card.dataset.capa;
        const pdf = card.dataset.pdf;

        document.getElementById('modalTituloDetalhe').textContent = titulo;
        document.getElementById('modalPrecoDetalhe').textContent = preco;
        document.getElementById('modalDescricaoDetalhe').textContent = descricao;
        document.getElementById('modalCapa').src = capa;
        document.getElementById('modalCapa').alt = `Capa de ${titulo}`;
        document.getElementById('modalVerPdfBtn').href = pdf;

        document.getElementById('btnComprarModalDetalhe').onclick = function() {
            alert(`Comprar: ${titulo}`);
        };

        bookModal.show();
    }

    // Adiciona evento a todos os botões "LER PDF"
    document.querySelectorAll('.btn-ler-pdf').forEach(function(btn) {
        btn.addEventListener('click', function() {
            const card = this.closest('.card');
            openBookModal(card);
        });
    });
});
