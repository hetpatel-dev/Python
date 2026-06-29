// Theme toggle — saves preference to localStorage
(function () {
  const STORAGE_KEY = "python-lessons-theme";

  function getSavedTheme() {
    return localStorage.getItem(STORAGE_KEY);
  }

  function setTheme(theme) {
    // theme: "light", "dark", or "system"
    const html = document.documentElement;
    html.classList.remove("light-mode", "dark-mode");

    if (theme === "light") {
      html.classList.add("light-mode");
    } else if (theme === "dark") {
      html.classList.add("dark-mode");
    }
    // "system" → no class → respects prefers-color-scheme
  }

  function getCurrentTheme() {
    const html = document.documentElement;
    if (html.classList.contains("dark-mode")) return "dark";
    if (html.classList.contains("light-mode")) return "light";
    return "system";
  }

  function getNextTheme(current) {
    const order = ["system", "light", "dark"];
    const idx = order.indexOf(current);
    return order[(idx + 1) % order.length];
  }

  function getLabel(theme) {
    if (theme === "light") return "\u{2600}\u{FE0F}"; // sun
    if (theme === "dark") return "\u{1F319}"; // moon
    return "\u{1F504}"; // refresh (follows system)
  }

  function getTitle(theme) {
    if (theme === "light") return "Light mode";
    if (theme === "dark") return "Dark mode";
    return "System default";
  }

  // Apply saved theme on load
  const saved = getSavedTheme();
  if (saved) {
    setTheme(saved);
  }

  // Create toggle button
  const btn = document.createElement("button");
  btn.id = "theme-toggle";
  const current = getCurrentTheme();
  btn.textContent = getLabel(current);
  btn.title = getTitle(current);

  btn.addEventListener("click", function () {
    const current = getCurrentTheme();
    const next = getNextTheme(current);
    setTheme(next);
    localStorage.setItem(STORAGE_KEY, next);
    btn.textContent = getLabel(next);
    btn.title = getTitle(next);
  });

  document.body.prepend(btn);
})();
