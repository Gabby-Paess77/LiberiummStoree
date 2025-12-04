document.addEventListener('DOMContentLoaded', () => {
    // 1. Seleciona os elementos que terão o efeito de suavidade
    const logo = document.getElementById('logo-anim');
    const texto = document.getElementById('texto-anim');
    const botoes = document.getElementById('botoes-anim');

    logo.classList.add('fade-in');
    texto.classList.add('fade-in');
    botoes.classList.add('fade-in');

    const delayLogo = 100; // 0.1 segundo
    const delayTexto = 600; // 0.6 segundo (após a logo começar)
    const delayBotoes = 1100; // 1.1 segundo (após o texto começar)

    // Efeito para o Logo
    setTimeout(() => {
        // Adiciona a classe 'visible', que muda a opacidade para 1
        // e transforma o elemento de volta para a posição original (transform: translateY(0)).
        logo.classList.add('visible');
    }, delayLogo);

    // Efeito para o Texto
    setTimeout(() => {
        texto.classList.add('visible');
    }, delayTexto);

    // Efeito para os Botões
    setTimeout(() => {
        botoes.classList.add('visible');
    }, delayBotoes);
});

