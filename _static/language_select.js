document.addEventListener("DOMContentLoaded", () => {
  let selectors = document.querySelectorAll("#language-selector");
  selectors.forEach((selector) => {
    selector.addEventListener("change", (event) => {
      let target = event.target.value;
      if (target.startsWith("https")) {
        window.location.href = target;
      } else {
        window.location.pathname = target;
      }
    });
  });
});
