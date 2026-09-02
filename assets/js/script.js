document.addEventListener("DOMContentLoaded", () => {
  // Grab all section headings inside the main body
  const headings = document.querySelectorAll(".main-body h1, .main-body h2, .main-body h3");
  const tocLinks = document.querySelectorAll(".sidebar-toc a");

  if (!headings.length || !tocLinks.length) return;

  // Map header IDs to corresponding TOC <a> elements
  const linkMap = {};
  tocLinks.forEach(link => {
    const href = link.getAttribute("href");
    if (href && href.startsWith("#")) {
      linkMap[href.slice(1)] = link;
    }
  });

  const observerOptions = {
    root: null,
    // Trigger when heading enters the top 20% to 40% of the viewport
    rootMargin: "0px 0px -60% 0px",
    threshold: 0
  };

  let currentActiveId = null;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute("id");
        if (id && linkMap[id]) {
          // Remove active class from previous link
          if (currentActiveId && linkMap[currentActiveId]) {
            linkMap[currentActiveId].classList.remove("active");
            linkMap[currentActiveId].closest("li")?.classList.remove("active-item");
          }

          // Apply active class to current visible heading's link
          currentActiveId = id;
          linkMap[id].classList.add("active");
          linkMap[id].closest("li")?.classList.add("active-item");
        }
      }
    });
  }, observerOptions);

  headings.forEach(heading => observer.observe(heading));
});