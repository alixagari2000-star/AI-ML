// Temporary user ID — replace this with dynamic value after real login
const userId = 1;

const ws = new WebSocket(`ws://localhost/ws/chat/${userId}`);

ws.onopen = () => {
  console.log("✅ Connected to WebSocket server");
};

ws.onmessage = (event) => {
  const chatWindow = document.getElementById('chat-window');
  const msg = document.createElement('p');
  msg.textContent = event.data;
  chatWindow.appendChild(msg);
  chatWindow.scrollTop = chatWindow.scrollHeight;  // Auto-scroll
};

ws.onclose = () => {
  console.log("❌ Disconnected from WebSocket server");
};

document.getElementById('send-btn').onclick = () => {
  const input = document.getElementById('message-input');
  const message = input.value.trim();
  if (message) {
    ws.send(message);
    input.value = '';
  }
};
