document.addEventListener('DOMContentLoaded', function () {
    const html = document.documentElement;
    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('.nav-links');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            const expanded = hamburger.getAttribute('aria-expanded') === 'true';
            hamburger.setAttribute('aria-expanded', String(!expanded));
            html.classList.toggle('nav-open');
        });
    }

    // Set current year in footer
    const yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();
});
