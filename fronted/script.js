async function gerar() {
  const tema = document.getElementById('tema').value;

  const res = await fetch('https://SUA_API/gerar', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ tema })
  });

  const blob = await res.blob();
  const url = window.URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'versiculos.pdf';
  a.click();
}
function selecionarTema(texto) {
  const input = document.getElementById('tema');
  input.value = texto;
  input.focus();
}
