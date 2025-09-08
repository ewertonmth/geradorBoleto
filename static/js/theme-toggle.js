const toggleBtn = document.getElementById('toggle-theme');
const body = document.body;

function setTheme(theme) {
  if (theme === 'light') {
    body.classList.remove('dark');
  } else {
    body.classList.add('dark');
  }
  localStorage.setItem('theme', theme);
}

// Inicializa tema salvo ou padrão dark
const savedTheme = localStorage.getItem('theme') || 'dark';
setTheme(savedTheme);

toggleBtn.addEventListener('click', () => {
  const currentTheme = body.classList.contains('dark') ? 'dark' : 'light';
  setTheme(currentTheme === 'dark' ? 'light' : 'dark');
});
