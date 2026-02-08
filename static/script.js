async function sendMessage() {
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const message = input.value;
    if (!message) return;

    // Add user message to UI
    chatBox.innerHTML += `<div class="message user-message">${message}</div>`;
    input.value = '';

    // Fetch from FastAPI
    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message })
    });
    const data = await response.json();

    // Add AI response to UI
    chatBox.innerHTML += `<div class="message ai-message">${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}