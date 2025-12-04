const listaAutores = document.getElementById('lista-autores-carrossel');
const btnEsq = document.getElementById('btn-carrossel-esq');
const btnDir = document.getElementById('btn-carrossel-dir');

// Função para rolar o carrossel
function rolarCarrossel(direcao) {
    // Largura do item e do espaçamento entre eles
    const itemLargura = listaAutores.querySelector('.autor-item').offsetWidth + 20; // 20px de gap
    listaAutores.scrollBy({
        left: direcao * itemLargura * 3,
        behavior: 'smooth'
    });
}

// Eventos de clique para os botões
if (btnEsq && btnDir) {
    btnEsq.addEventListener('click', () => rolarCarrossel(-1));
    btnDir.addEventListener('click', () => rolarCarrossel(1));
}

// Lógica para os indicadores (opcional)
const indicadores = document.querySelectorAll('.ponto');
if (indicadores.length > 0) {
    listaAutores.addEventListener('scroll', () => {
        const scrollLeft = listaAutores.scrollLeft;
        const scrollWidth = listaAutores.scrollWidth;
        const clientWidth = listaAutores.clientWidth;

        // Calcula o índice do slide atual
        const slideIndex = Math.round(scrollLeft / (scrollWidth - clientWidth) * (indicadores.length - 1));

        // Remove a classe 'ativo' de todos os pontos
        indicadores.forEach(ponto => ponto.classList.remove('ativo'));

        // Adiciona a classe 'ativo' ao ponto atual
        if (indicadores[slideIndex]) {
            indicadores[slideIndex].classList.add('ativo');
        }
    });
}



let currentDepoimento = 0;
const depoimentos = document.querySelectorAll('.depoimento-item');
const dots = document.querySelectorAll('.dot');
const totalDepoimentos = depoimentos.length;

// Função para mostrar o depoimento atual
function showDepoimento(index) {
    // Garante que o index esteja dentro dos limites
    if (index >= totalDepoimentos) {
        currentDepoimento = 0;
    } else if (index < 0) {
        currentDepoimento = totalDepoimentos - 1;
    } else {
        currentDepoimento = index;
    }

    // Esconde todos os depoimentos e remove a classe 'active' das bolinhas
    depoimentos.forEach(item => item.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active-dot'));

    // Mostra o depoimento e a bolinha correspondente
    depoimentos[currentDepoimento].classList.add('active');
    dots[currentDepoimento].classList.add('active-dot');
}


// Pega os elementos do DOM
const modal = document.getElementById('modalDepoimento');
const btnAbrir = document.getElementById('abrirModal');
const spanFechar = document.getElementsByClassName('fechar')[0];
const form = document.getElementById('formDepoimento');
const mensagemSucesso = document.getElementById('mensagemSucesso');

// Quando o usuário clica no botão, abre o modal
btnAbrir.onclick = function() {
    modal.style.display = 'block';
    mensagemSucesso.style.display = 'none'; // Esconde a mensagem de sucesso
    form.reset(); // Limpa o formulário
    form.style.display = 'block'; // Mostra o formulário
}

// Quando o usuário clica no (x), fecha o modal
spanFechar.onclick = function() {
    modal.style.display = 'none';
}

// Quando o usuário clica em qualquer lugar fora do modal, fecha o modal
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Simula o envio do formulário (na vida real, você enviaria para um servidor)
form.onsubmit = function(event) {
    event.preventDefault(); // Impede o envio real do formulário

    // Aqui você faria uma requisição AJAX/Fetch para enviar os dados.
    console.log('Dados a serem enviados:', {
        nome: document.getElementById('nome').value,
        livro: document.getElementById('livro').value,
        comentario: document.getElementById('comentario').value
    });

    // Simula o sucesso no envio: esconde o formulário e mostra a mensagem de sucesso
    form.style.display = 'none';
    mensagemSucesso.style.display = 'block';

    // Opcional: Fechar o modal após alguns segundos
    setTimeout(() => {
        modal.style.display = 'none';
    }, 3000);
}







