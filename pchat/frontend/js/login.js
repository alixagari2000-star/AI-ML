document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  if (!form) return;

  form.addEventListener("submit", function (event) {
    const usernameInput = document.querySelector('input[name="username"]');
    if (!usernameInput.value.trim()) {
      alert("Please enter a username.");
      event.preventDefault();
    }
  });
});
