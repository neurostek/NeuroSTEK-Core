const api = "http://localhost:8000"; // если локально

async function register() {
  const body = {
    username: document.getElementById("reg_username").value,
    password: document.getElementById("reg_password").value,
    email: document.getElementById("reg_email").value,
  };

  const res = await fetch(`${api}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });

  const data = await res.json();
  alert(data.message || JSON.stringify(data));
}

async function login() {
  const body = {
    username: document.getElementById("login_username").value,
    password: document.getElementById("login_password").value,
  };

  const res = await fetch(`${api}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });

  const data = await res.json();

  if (res.ok) {
    getBalance(body.username);
  } else {
    alert(data.detail || "Ошибка входа");
  }
}

async function getBalance(username) {
  const res = await fetch(`${api}/tokens/balance/${username}`);
  const data = await res.json();
  document.getElementById("tokenBalance").textContent = data.tokens;
  document.getElementById("balanceBlock").classList.remove("hidden");
      }
