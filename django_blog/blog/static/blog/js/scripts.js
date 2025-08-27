document.addEventListener('DOMContentLoaded', function () {
  console.log('Login/Register page loaded successfully.');
  
  // Optional: Add a little interactivity
  const submitBtn = document.querySelector('input[type="submit"]');
  if (submitBtn) {
    submitBtn.addEventListener('mouseover', () => {
      submitBtn.style.backgroundColor = '#0056b3';
    });
    submitBtn.addEventListener('mouseout', () => {
      submitBtn.style.backgroundColor = '#007bff';
    });
  }
});