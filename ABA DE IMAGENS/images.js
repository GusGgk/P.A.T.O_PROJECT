const imagens = document.querySelectorAll('.galeria img');
const totalImagens = imagens.length;
let indiceImagem = 0;

function trocarImagem() {
    imagens[indiceImagem].style.display = 'none';
    indiceImagem = Math.floor(Math.random() * totalImagens);
    imagens[indiceImagem].style.display = 'block';
}

// Iniciar a transição automática
setInterval(trocarImagem, 4000);