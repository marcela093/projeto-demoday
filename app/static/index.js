let banner = document.querySelector('.img img');
let banners = [
    '../static/images/MULHERES01.png',
    '../static/images/MULHERES02.png',
    '../static/images/MULHERES03.png',
    '../static/images/MULHERES04.png',    
];

let bannerAtual = 0;

function trocaBanner(){
    bannerAtual++;
    if(bannerAtual == banners.length){
        bannerAtual = 0;
    }
    banner.src = banners[bannerAtual];
}

setInterval(trocaBanner, 4000);
