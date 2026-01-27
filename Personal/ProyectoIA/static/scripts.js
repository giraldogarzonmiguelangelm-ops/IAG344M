const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});
<script src="{{ url_for('static', filename='scripts.js') }}"></script>
const chatbotBtn = document.querySelector('.chatbot-btn');
const chatbotContainer = document.getElementById('chatbot-container');
const closeChat = document.getElementById('close-chatbot');
const sendBtn = document.getElementById('chatbot-send');
const input = document.getElementById('chatbot-input');
const messages = document.getElementById('chatbot-messages');
/* Abrir chat */
chatbotBtn.addEventListener('click', () => {
    chatbotContainer.style.display = 'flex';
});
/* Cerrar chat */
closeChat.addEventListener('click', () =>{
    chatbotContainer.style.display = 'none';
});
/* Función para agregar mensaje */
function addMessage(sender, text){
    const msg = document.createElement('div');
    msg.textContent = text;
    msg.style.marginBottom = "8px";
    msg.style.fontWeight = sender === 'bot' ? 'bold' : 'normal';
    messages.appendChild(msg);
    messages.scrollTop = messages.scrollHeight;
}
/* Enviar mensaje */
sendBtn.addEventListener('click', () =>{
    const userMessage = input.value.trim();
    if (!userMessage) return;
    addMessage('user', userMessage);
    input.value = "";
/* Llamada al backend flask */
fetch('/chat',{
    method: 'POST',
    headers: {'Content-type': 'application/x-www-form-urlencoded'},
    body: `message=${encodeURIComponent(userMessage)}`
})
.then(response => response.json())
.then(data =>{
    addMessage('bot', data.response);
})
.catch(err =>{
    addMessage('bot', 'Error al conectar con el servidor.');
    console.error(err);
});
});
/* Enviar mensaje al presionar enter */
input.addEventListener('keypress', function(e){
    if (e.key === 'Enter') {
        sendBtn.click();
    }
});