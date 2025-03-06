// scripts.js
function toggleForm(formId) {
  const signInForm = document.getElementById('sign-in-form');
  const signUpForm = document.getElementById('sign-up-form');
  
  if (formId === 'sign-in-form') {
    signInForm.style.display = 'block';
    signUpForm.style.display = 'none';
  } else {
    signUpForm.style.display = 'block';
    signInForm.style.display = 'none';
  }
}