document.addEventListener('DOMContentLoaded', function () {

    const toggleButtons = document.querySelectorAll('.toggle-lyrics');
    toggleButtons.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('data-target');
            const target = document.getElementById(targetId);
            if (target) {
                target.classList.toggle('d-none');
                this.innerHTML = target.classList.contains('d-none')
                    ? '<i class="bi bi-chevron-down"></i> Show Full Lyrics'
                    : '<i class="bi bi-chevron-up"></i> Hide Lyrics';
            }
        });
    });

    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('#navbarNav');
    if (navbarToggler && navbarCollapse) {
        navbarCollapse.addEventListener('shown.bs.collapse', function () {
            navbarToggler.setAttribute('aria-expanded', 'true');
        });
        navbarCollapse.addEventListener('hidden.bs.collapse', function () {
            navbarToggler.setAttribute('aria-expanded', 'false');
        });
    }
});
