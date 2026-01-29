const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

const chatbotBtn = document.querySelector('.chatbot-btn');
const chatbotContainer = document.getElementById('chatbot-container');
const closeChat = document.getElementById('close-chatbot');
const sendBtn = document.getElementById('chatbot-send');
const input = document.getElementById('chatbot-input');
const messages = document.getElementById('chatbot-messages');

/* Abrir/Cerrar chat */
chatbotBtn.addEventListener('click', () => chatbotContainer.style.display = 'flex');
closeChat.addEventListener('click', () => chatbotContainer.style.display = 'none');

/* Función para agregar mensajes con estilo */
function addMessage(sender, text){
    const msg = document.createElement('div');
    msg.textContent = text;
    msg.style.marginBottom = "10px";
    msg.style.padding = "10px";
    msg.style.borderRadius = "10px";
    msg.style.maxWidth = "80%";
    msg.style.wordWrap = "break-word";
    msg.style.fontSize = "14px";

    if (sender === 'bot') {
        msg.style.backgroundColor = "#f1f1f1";
        msg.style.alignSelf = "flex-start";
        msg.style.borderLeft = "4px solid #e10600";
        msg.style.fontWeight = "bold";
    } else {
        msg.style.backgroundColor = "#e10600";
        msg.style.color = "white";
        msg.style.alignSelf = "flex-end";
        msg.style.marginLeft = "auto";
    }

    messages.appendChild(msg);
    messages.scrollTop = messages.scrollHeight;
}

/* Enviar mensaje */
sendBtn.addEventListener('click', () => {
    const userMessage = input.value.trim();
    if (!userMessage) return;

    addMessage('user', userMessage);
    input.value = "";

    // Indicador de carga
    const typing = document.createElement('div');
    typing.id = "typing";
    typing.textContent = "Ducati está pensando...";
    typing.style.fontSize = "11px";
    typing.style.color = "#888";
    messages.appendChild(typing);

    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-type': 'application/x-www-form-urlencoded' },
        body: `message=${encodeURIComponent(userMessage)}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('typing').remove();
        addMessage('bot', data.response);
    })
    .catch(err => {
        if(document.getElementById('typing')) document.getElementById('typing').remove();
        addMessage('bot', 'Error de conexión.');
        console.error(err);
    });
});

/* Enter para enviar */
input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendBtn.click();
});