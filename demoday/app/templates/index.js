let banner = document.querySelector('#carrosel');
let banners = [
    '../static/images/Mulheres_Carrossel/MULHERES01.png',
    '../static/images/Mulheres_Carrossel/MULHERES02.png',
    '../static/images/Mulheres_Carrossel/MULHERES03.png',
    '../static/images/Mulheres_Carrossel/MULHERES04.png',
]

let bannerAtual = 0;

function trocaBanner() {
    bannerAtual++;
    if (bannerAtual == banners.length) {
        bannerAtual = 0;
    }
    banner.src = banners[bannerAtual];
}

// banner.onclick = trocaBanner();
setInterval((trocaBanner), 1000);