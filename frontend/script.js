async function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();
  if (!message) return;

  addMessage("You", message, "user");
  input.value = "";

  const response = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  addMessage("Bot", data.reply, "bot");
}

function addMessage(sender, text, cls) {
  const messages = document.getElementById("messages");
  const div = document.createElement("div");
  div.className = cls;
  div.innerText = `${sender}: ${text}`;
  messages.appendChild(div);
}
