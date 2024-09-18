const icons = document.querySelectorAll('.fab');

icons.forEach(icon => {
  icon.addEventListener('mouseover', () => {
    icon.style.transform = 'scale(1.2)';
  });

  icon.addEventListener('mouseout', () => {
    icon.style.transform = 'scale(1)';   

  });
});