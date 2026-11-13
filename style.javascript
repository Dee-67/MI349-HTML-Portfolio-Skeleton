(() => {
  const initializeThemeToggle = () => {
    const header = document.querySelector("header");

    if (!header) {
      throw new Error("The theme toggle requires a page header.");
    }

    const themeStyles = document.createElement("style");
    themeStyles.textContent = `
      html[data-theme="dark"] {
        color-scheme: dark;
        --color-page: #121a18;
        --color-surface: #1c2925;
        --color-text: #f3f0e7;
        --color-muted: #b4c3bb;
        --color-forest: #101b18;
        --color-mint: #243b33;
        --color-coral: #a94c32;
        --color-gold: #9b7628;
        --color-border: #43574e;
      }

      html[data-theme="dark"] a:not(.showcase-link):not(.topic-tile) {
        color: #b8d5ff;
      }

      html[data-theme="dark"] a:not(.showcase-link):not(.topic-tile):hover {
        color: #d7e6ff;
      }
    `;
    document.head.append(themeStyles);

    const toggle = document.createElement("button");
    toggle.type = "button";
    toggle.style.cssText = [
      "padding: 0.55rem 0.8rem",
      "border: 1px solid rgb(255 253 247 / 48%)",
      "background: transparent",
      "color: #fffdf7",
      "font: inherit",
      "cursor: pointer",
    ].join(";");
    header.append(toggle);

    const savedTheme = window.localStorage.getItem("portfolio-theme");
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    let isDark = savedTheme ? savedTheme === "dark" : prefersDark;

    const updateTheme = () => {
      document.documentElement.dataset.theme = isDark ? "dark" : "light";
      toggle.textContent = isDark ? "☀ Light mode" : "☾ Dark mode";
      toggle.setAttribute("aria-label", `Switch to ${isDark ? "light" : "dark"} mode`);
      toggle.setAttribute("aria-pressed", String(isDark));
    };

    toggle.addEventListener("click", () => {
      isDark = !isDark;
      window.localStorage.setItem("portfolio-theme", isDark ? "dark" : "light");
      updateTheme();
    });

    updateTheme();
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeThemeToggle, { once: true });
  } else {
    initializeThemeToggle();
  }
})();

