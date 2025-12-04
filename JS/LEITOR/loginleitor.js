document.getElementById("loginForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value.trim();
    const msg = document.getElementById("mensagem");

    msg.innerHTML = "";

    // Simples validação
    if (email === "admin@liberium.com" && senha === "12345") {
        msg.innerHTML = "<p class='text-success fw-bold'>✅ Login realizado com sucesso!</p>";
        setTimeout(() => window.location.href = "dashboard.html", 1200);
    } else {
        msg.innerHTML = "<p class='text-danger fw-bold'>❌ Email ou senha inválidos.</p>";
    }
});
