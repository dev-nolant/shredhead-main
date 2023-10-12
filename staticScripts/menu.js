document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById('menuToggle');
    const menuItems = document.getElementById('menuItems');

    menuToggle.addEventListener('click', () => {
        menuItems.classList.toggle('active');
    });
});
