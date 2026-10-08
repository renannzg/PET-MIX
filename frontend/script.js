let chatHistory = [];
let petContext = null;

document.getElementById('save-pet-btn').addEventListener('click', () => {
    const nome = document.getElementById('pet-nome').value;
    const especie = document.getElementById('pet-especie').value;
    const porte = document.getElementById('pet-porte').value;
    
    if (nome && especie) {
        petContext = { nome, especie, porte };
        document.getElementById('pet-status').innerText = 'Perfil salvo!';
        document.getElementById('pet-status').style.color = 'green';
    } else {
        document.getElementById('pet-status').innerText = 'Preencha nome e espécie.';
        document.getElementById('pet-status').style.color = 'red';
    }
});

document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

async function sendMessage() {
    const inputEl = document.getElementById('user-input');
    const message = inputEl.value.trim();
    
    if (!message) return;
    
    // Adicionar a mensagem do usuário à interface
    addMessageToUI(message, 'user');
    inputEl.value = '';
    
    // Adicionar indicador de digitação
    const typingId = addMessageToUI('...', 'system', true);
    
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                history: chatHistory,
                pet_context: petContext
            })
        });
        
        const data = await response.json();
        
        // Remover indicador de digitação
        document.getElementById(typingId).remove();
        
        if (response.ok) {
            addMessageToUI(data.response, 'system');
            
            // Atualizar histórico
            chatHistory.push({ role: 'user', content: message });
            chatHistory.push({ role: 'assistant', content: data.response });
        } else {
            addMessageToUI('Erro ao comunicar com o servidor.', 'system');
        }
    } catch (error) {
        document.getElementById(typingId).remove();
        addMessageToUI('Erro de conexão.', 'system');
    }
}

function addMessageToUI(text, sender, isTyping = false) {
    const chatBox = document.getElementById('chat-box');
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', sender);
    msgDiv.innerText = text;
    
    if (isTyping) {
        msgDiv.id = 'typing-indicator';
    }
    
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    
    return msgDiv.id;
}
