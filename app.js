document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const resetBtn = document.getElementById('reset-btn');
    
    const inputSection = document.getElementById('input-section');
    const loadingSection = document.getElementById('loading-section');
    const resultsSection = document.getElementById('results-section');
    
    const loadingTexts = [
        document.getElementById('loading-text-1'),
        document.getElementById('loading-text-2'),
        document.getElementById('loading-text-3')
    ];

    generateBtn.addEventListener('click', () => {
        const vibe = document.getElementById('vibe-input').value;
        const context = document.getElementById('game-context').value;
        
        if (!vibe || !context) {
            document.getElementById('vibe-input').value = "Futuristic cyberpunk with neon accents";
            document.getElementById('game-context').value = "Valorant";
        }

        inputSection.classList.add('hidden');
        loadingSection.classList.remove('hidden');

        setTimeout(() => { switchLoadingText(0, 1); }, 1200);
        setTimeout(() => { switchLoadingText(1, 2); }, 2400);

        setTimeout(() => {
            loadingSection.classList.add('hidden');
            resultsSection.classList.remove('hidden');
            resultsSection.classList.add('fade-in');
        }, 3500);
    });

    resetBtn.addEventListener('click', () => {
        resultsSection.classList.add('hidden');
        resultsSection.classList.remove('fade-in');
        inputSection.classList.remove('hidden');
        switchLoadingText(2, 0);
    });

    function switchLoadingText(currentIndex, nextIndex) {
        loadingTexts[currentIndex].classList.remove('active');
        loadingTexts[nextIndex].classList.add('active');
    }
});
