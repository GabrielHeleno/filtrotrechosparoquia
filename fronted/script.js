async function gerar() {
  try {
    const tema = document.getElementById('tema').value;
    if (!tema) {
      alert("Digite um tema antes de gerar.");
      return;
    }

    const res = await fetch('https://filtrotrechosparoquia.onrender.com/gerar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tema })
    });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(`Erro no backend: ${res.status} ${text}`);
    }

    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = 'versiculos.pdf';
    document.body.appendChild(a);
    a.click();
    a.remove();
    window.URL.revokeObjectURL(url);

  } catch (err) {
    console.error(err);
    alert("Erro ao gerar arquivo: " + err.message);
  }
}

function selecionarTema(texto) {
  const input = document.getElementById('tema');
  input.value = texto;
  input.focus();
}
