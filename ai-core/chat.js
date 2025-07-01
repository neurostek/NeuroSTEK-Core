const chatApi = "http://localhost:8000/chat";

function appendMessage(role, text) {
  const box = document.getElementById("chatBox");
  const div = document.createElement("div");
  div.innerHTML = `<strong>${role === "bot" ? "🤖 Бот" : "🧑 Вы"}:</strong> ${text}`;
  div.className = "mb-1";
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}

async function sendMessage() {
  const username = document.getElementById("username").value;
  const message = document.getElementById("userInput").value;

  if (!username || !message) {
    alert("Заполни имя и сообщение!");
    return;
  }

  appendMessage("user", message);
  document.getElementById("userInput").value = "";

  const res = await fetch(chatApi, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, message })
  });

  const data = await res.json();
  appendMessage("bot", data.reply);
    }
