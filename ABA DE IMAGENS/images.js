// script.js
const imagens = document.querySelectorAll('.imagem');
let indiceImagem = 0;

function mostrarImagem(indice) {
  // Limpa a classe 'ativa' de todas as imagens
  imagens.forEach(imagem => imagem.classList.remove('ativa'));
  // Adiciona a classe 'ativa' à imagem atual
  imagens[indice].classList.add('ativa');
}

// Mostra a primeira imagem por padrão
mostrarImagem(indiceImagem);

function mostrarImagemAnterior() {
  indiceImagem--;
  if (indiceImagem < 0) {
    indiceImagem = imagens.length - 1;
  }
  mostrarImagem(indiceImagem);
}

function mostrarImagemProxima() {
  indiceImagem++;
  if (indiceImagem >= imagens.length) {
    indiceImagem = 0;
  }
  mostrarImagem(indiceImagem);
}