let livros = [
    { titulo: "Dom Casmurro", autor: "Machado de Assis", imagem: "img/domcasmurro.jpg", pdf: "PDF/DomCasmurro.pdf" },
    { titulo: "O Pequeno Príncipe", autor: "Antoine de Saint-Exupéry", imagem: "img/principe.jpg", pdf: "PDF/PequenoPrincipe.pdf" },
    { titulo: "1984", autor: "George Orwell", imagem: "img/1984.jpg", pdf: "PDF/1984.pdf" },
    { titulo: "A Metamorfose", autor: "Franz Kafka", imagem: "img/metamorfose.jpg", pdf: "PDF/Metamorfose.pdf" }
];

const listaLivros = document.getElementById("lista-livros");

// Função para renderizar livros
function renderizarLivros() {
    listaLivros.innerHTML = "";
    livros.forEach(livro => {
        const col = document.createElement("div");
        col.className = "col-6 col-md-4 col-lg-3";
        col.innerHTML = `
      <div class="card h-100 shadow-sm">
        <div class="img-container">
          <img src="${livro.imagem}" alt="${livro.titulo}">
        </div>
        <div class="card-body">
          <h5 class="card-title">${livro.titulo}</h5>
          <p>${livro.autor}</p>
          ${livro.pdf ? `<a href="static/${livro.pdf}" target="_blank" class="btn btn-dark btn-sm">LER PDF</a>` : ''}
        </div>
      </div>
    `;
        listaLivros.appendChild(col);
    });
}
renderizarLivros();

// Cadastro de novo livro
document.getElementById("formCadastro").addEventListener("submit", function(e) {
    e.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;
    const descricao = document.getElementById("descricao").value;
    const imagemFile = document.getElementById("imagem").files[0];
    const pdfFile = document.getElementById("pdf").files[0];

    if (imagemFile) {
        const reader = new FileReader();
        reader.onload = function(e) {
            livros.push({
                titulo,
                autor,
                imagem: e.target.result, // preview da capa
                pdf: pdfFile ? `PDF/${pdfFile.name}` : "", // link para PDF dentro da pasta static/PDF
                descricao
            });
            renderizarLivros();
        };
        reader.readAsDataURL(imagemFile);
    }

    // Fecha modal
    const modal = bootstrap.Modal.getInstance(document.getElementById("modalCadastro"));
    modal.hide();
    this.reset();
});
