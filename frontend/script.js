let chatHistory = [];
let petContext = null;

// Inicialização: carregar perfil do pet salvo no localStorage (se houver)
window.addEventListener('DOMContentLoaded', () => {
    const savedPet = localStorage.getItem('petmix_pet_context');
    if (savedPet) {
        try {
            petContext = JSON.parse(savedPet);
            document.getElementById('pet-nome').value = petContext.nome || '';
            document.getElementById('pet-especie').value = petContext.especie || 'Cachorro';
            document.getElementById('pet-porte').value = petContext.porte || 'Médio';
            updatePetBadge();
        } catch (e) {
            console.error('Erro ao recuperar perfil:', e);
        }
    }
});

// Salvar Perfil do Pet
document.getElementById('save-pet-btn').addEventListener('click', () => {
    const nome = document.getElementById('pet-nome').value.trim();
    const especie = document.getElementById('pet-especie').value;
    const porte = document.getElementById('pet-porte').value;

    if (!nome) {
        alert('Por favor, informe o nome do seu pet.');
        return;
    }

    petContext = { nome, especie, porte };
    localStorage.setItem('petmix_pet_context', JSON.stringify(petContext));
    updatePetBadge();

    // Notificação sutil no chat
    addAssistantMessage(`Perfeito! Perfil do **${nome}** (${especie}, porte ${porte}) ativado. Suas próximas perguntas levarão isso em consideração! 🐶✨`);
});

// Limpar Perfil do Pet
document.getElementById('clear-pet-btn').addEventListener('click', () => {
    petContext = null;
    localStorage.removeItem('petmix_pet_context');
    document.getElementById('pet-nome').value = '';
    document.getElementById('pet-badge-active').style.display = 'none';
    addAssistantMessage('Perfil do pet removido. Respostas voltarão ao modo genérico.');
});

function updatePetBadge() {
    if (petContext && petContext.nome) {
        const badge = document.getElementById('pet-badge-active');
        const info = document.getElementById('active-pet-info');
        info.innerText = `${petContext.nome} (${petContext.especie}, ${petContext.porte})`;
        badge.style.display = 'block';
    }
}

// Limpar Histórico de Chat
document.getElementById('clear-chat-btn').addEventListener('click', () => {
    if (confirm('Deseja reiniciar a conversa?')) {
        chatHistory = [];
        const chatBox = document.getElementById('chat-box');
        chatBox.innerHTML = `
            <div class="message assistant">
                <div class="avatar">🐾</div>
                <div class="bubble">
                    <p>Conversa reiniciada. Como posso ajudar você e seu pet agora?</p>
                </div>
            </div>
        `;
    }
});

// Chips de Ação Rápida
document.querySelectorAll('.chip').forEach(chip => {
    chip.addEventListener('click', () => {
        const query = chip.getAttribute('data-query');
        if (query) {
            document.getElementById('user-input').value = query;
            sendMessage();
        }
    });
});

// Envio de Mensagem
async function sendMessage() {
    const inputEl = document.getElementById('user-input');
    const message = inputEl.value.trim();
    if (!message) return;

    // Adiciona mensagem do usuário à interface
    addUserMessage(message);
    inputEl.value = '';

    // Adiciona indicador de digitação
    const typingId = addTypingIndicator();

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: message,
                history: chatHistory,
                pet_context: petContext
            })
        });

        const data = await response.json();
        removeTypingIndicator(typingId);

        if (response.ok) {
            addAssistantMessage(data.response, data.tools_used);
            // Atualiza histórico em memória
            chatHistory.push({ role: 'user', content: message });
            chatHistory.push({ role: 'assistant', content: data.response });
        } else {
            const detalhe = data && data.detail ? data.detail : 'Erro no processamento da solicitação.';
            addAssistantMessage(`⚠️ **Aviso:** ${detalhe}`);
        }
    } catch (error) {
        removeTypingIndicator(typingId);
        addAssistantMessage('⚠️ **Erro de Conexão:** Não foi possível contactar o servidor local do Pet Mix.');
    }
}

// Adiciona Mensagem do Usuário
function addUserMessage(text) {
    const chatBox = document.getElementById('chat-box');
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', 'user');

    const bubble = document.createElement('div');
    bubble.classList.add('bubble');
    bubble.innerText = text;

    msgDiv.appendChild(bubble);
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Adiciona Mensagem do Assistente com Suporte a Markdown
function addAssistantMessage(markdownText, toolsUsed = []) {
    const chatBox = document.getElementById('chat-box');
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', 'assistant');

    const avatar = document.createElement('div');
    avatar.classList.add('avatar');
    avatar.innerText = '🐾';

    const bubble = document.createElement('div');
    bubble.classList.add('bubble');

    // Converte Markdown para HTML (se marked estiver disponível)
    if (window.marked && typeof marked.parse === 'function') {
        bubble.innerHTML = marked.parse(markdownText);
    } else {
        bubble.innerText = markdownText;
    }

    // Se houve execução de ferramentas (Grounding), mostra badge de transparência
    if (toolsUsed && toolsUsed.length > 0) {
        const toolTag = document.createElement('div');
        toolTag.classList.add('tool-tag');
        toolTag.innerText = `🔍 Consulta realizada: ${toolsUsed.join(', ')}`;
        bubble.appendChild(toolTag);
    }

    msgDiv.appendChild(avatar);
    msgDiv.appendChild(bubble);
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addTypingIndicator() {
    const chatBox = document.getElementById('chat-box');
    const id = 'typing-' + Date.now();
    const msgDiv = document.createElement('div');
    msgDiv.id = id;
    msgDiv.classList.add('message', 'assistant');
    msgDiv.innerHTML = `
        <div class="avatar">🐾</div>
        <div class="bubble">
            <span style="color: #64748b;">Consultando informações do Pet Mix...</span>
        </div>
    `;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    return id;
}

function removeTypingIndicator(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
}
