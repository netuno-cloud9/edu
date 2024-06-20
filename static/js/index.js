document.addEventListener('DOMContentLoaded', function () {
    // Add event listeners to all .bt elements
    document.querySelectorAll('.bt').forEach(button => {
        button.addEventListener('click', (event) => {
            // Prevent default link behavior
            event.preventDefault();

            // Determine the URL to navigate to based on the button clicked
            let url = '';
            switch (button.id) {
                case 'indicadores':
                    url = '../indicators/indicators.html';
                    break;
                case 'planos-de-aula':
                    url = '../classplan/classplan.html';
                    break;
                case 'links-rapidos':
                    url = '../splinks';
                    break;
                case 'educhat':
                    url = '/content/educhat.html';
                    break;
                case 'ranking':
                    url = '/content/ranking.html';
                    break;
                case 'suporte-tecnico':
                    url = '/content/suporte_tecnico.html';
                    break;
                default:
                    return; // Exit function if no matching case
            }

            // Apply a click animation
            button.classList.add('clicked');

            // Redirect to the selected URL after a short delay
            setTimeout(() => {
                window.location.href = url;
            }, 300); // Adjust delay time as needed
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: true,
        autoplay: {
            delay: 5000, // Delay in milliseconds (5 seconds here)
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
});