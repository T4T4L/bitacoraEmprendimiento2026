document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    let currentSlide = 0;

    const pageIndicator = document.getElementById('page-counter');
    const presentationContainer = document.getElementById('presentation-container');

    function updateSlide() {
        slides.forEach((slide, index) => {
            if (index === currentSlide) {
                slide.classList.add('active');
            } else {
                slide.classList.remove('active');
            }
        });
        
        if (pageIndicator) {
            pageIndicator.innerText = `${currentSlide + 1} / ${totalSlides}`;
        }
    }

    function nextSlide() {
        if (currentSlide < totalSlides - 1) {
            currentSlide++;
            updateSlide();
        }
    }

    function prevSlide() {
        if (currentSlide > 0) {
            currentSlide--;
            updateSlide();
        }
    }

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
            nextSlide();
        } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
            prevSlide();
        }
    });

    // Button navigation
    document.getElementById('btn-next').addEventListener('click', (e) => {
        e.stopPropagation();
        nextSlide();
    });
    
    document.getElementById('btn-prev').addEventListener('click', (e) => {
        e.stopPropagation();
        prevSlide();
    });

    // Click anywhere to advance (except buttons)
    presentationContainer.addEventListener('click', () => {
        nextSlide();
    });

    // Responsive scaling
    function resizePresentation() {
        const windowWidth = window.innerWidth;
        const windowHeight = window.innerHeight;
        const containerWidth = 1920;
        const containerHeight = 1080;
        
        const scale = Math.min(windowWidth / containerWidth, windowHeight / containerHeight);
        
        presentationContainer.style.transform = `scale(${scale})`;
    }

    window.addEventListener('resize', resizePresentation);
    
    // Initialize
    resizePresentation();
    updateSlide();
});

