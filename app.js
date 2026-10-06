(() => {
  const links = document.querySelectorAll('a[href^="#"]');
  links.forEach(link => link.addEventListener('click', () => {
    const id = link.getAttribute('href').slice(1);
    const target = document.getElementById(id);
    if (target) setTimeout(() => target.focus?.({preventScroll:true}), 300);
  }));
})();
