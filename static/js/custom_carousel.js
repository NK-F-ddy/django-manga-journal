// static/js/custom_carousel.js

document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.getElementById('roomCarousel');
    if (!carousel) return;

    const items = Array.from(carousel.querySelectorAll('.carousel-item-custom'));
    const prevButton = document.querySelector('.carousel-control-prev-custom');
    const nextButton = document.querySelector('.carousel-control-next-custom');
    
    // アイテム数が0または1の場合は動作を無効化
    if (items.length <= 1) {
        if (prevButton) prevButton.style.display = 'none';
        if (nextButton) nextButton.style.display = 'none';
        return;
    }

    let currentIndex = 0;

    function updateCarouselClasses() {
        items.forEach((item, index) => {
            // すべてのカスタムクラスを一旦リセット
            item.classList.remove('center', 'left', 'right', 'hidden', 'next-right', 'prev-left');

            const diff = index - currentIndex;
            
            // 循環を考慮した計算
            let actualDiff = diff;
            if (diff > items.length / 2) {
                actualDiff = diff - items.length;
            } else if (diff < -items.length / 2) {
                actualDiff = diff + items.length;
            }

            if (actualDiff === 0) {
                item.classList.add('center');
            } else if (actualDiff === 1) {
                item.classList.add('right');
            } else if (actualDiff === -1) {
                item.classList.add('left');
            } else if (actualDiff === 2) {
                item.classList.add('next-right');
            } else if (actualDiff === -2) {
                item.classList.add('prev-left');
            } else {
                item.classList.add('hidden');
            }
        });

        // クリック切り替え機能の再設定
        items.forEach((item, index) => {
            item.onclick = (e) => {
                if (item.classList.contains('right')) {
                    nextButton.click();
                } else if (item.classList.contains('left')) {
                    prevButton.click();
                }
            };
        });
    }

    // 次へボタン
    nextButton.addEventListener('click', function() {
        currentIndex = (currentIndex + 1) % items.length;
        updateCarouselClasses();
    });

    // 前へボタン
    prevButton.addEventListener('click', function() {
        currentIndex = (currentIndex - 1 + items.length) % items.length;
        updateCarouselClasses();
    });

    // 初回表示
    updateCarouselClasses();
});
