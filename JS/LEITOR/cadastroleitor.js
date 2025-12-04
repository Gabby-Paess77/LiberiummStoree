document.getElementById('signup-form').addEventListener('submit', function(event) {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        alert('As senhas não coincidem. Por favor, verifique.');
        event.preventDefault();
    } else {
        alert('Formulário enviado com sucesso!');
    }
});