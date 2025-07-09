// AJAX chat submit
const chatForm = document.getElementById('chat-form');
if (chatForm) {
  chatForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const input = document.getElementById('chat-input');
    const text = input.value;
    const convId = document.querySelector('input[name="conversation_id"]')?.value;
    const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    fetch('/chat/', {
      method: 'POST',
      headers: {'X-CSRFToken': csrf, 'Content-Type': 'application/x-www-form-urlencoded'},
      body: `text=${encodeURIComponent(text)}${convId ? `&conversation_id=${convId}` : ''}`
    })
    .then(res => res.json())
    .then(data => {
      input.value = '';
      window.location = `/chat/?conversation_id=${data.conversation_id}`;
      // Optionally, speak the response
      speakText(data.response);
    });
  });
}

// Voice input (Web Speech API)
const voiceBtn = document.getElementById('voice-btn');
if (voiceBtn && 'webkitSpeechRecognition' in window) {
  const recognition = new webkitSpeechRecognition();
  recognition.lang = 'en-US';
  recognition.continuous = false;
  recognition.interimResults = false;
  voiceBtn.onclick = function() {
    recognition.start();
  };
  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById('chat-input').value = transcript;
  };
}

// Text-to-speech (Web Speech API)
function speakText(text) {
  if ('speechSynthesis' in window) {
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = 'en-US';
    window.speechSynthesis.speak(utter);
  }
}
const ttsBtn = document.getElementById('tts-btn');
if (ttsBtn) {
  ttsBtn.onclick = function() {
    const lastMsg = document.querySelector('#chat-history div:last-child');
    if (lastMsg) speakText(lastMsg.textContent);
  };
} 