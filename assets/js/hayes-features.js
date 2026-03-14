document.addEventListener("DOMContentLoaded", () => {
  const player = document.getElementById("player");

  document.querySelectorAll(".sound").forEach((button) => {
    button.addEventListener("click", () => {
      const src = button.dataset.audio;
      if (!src) return;

      player.pause();
      player.currentTime = 0;
      player.src = src;
      player.play().catch(console.error);
    });
  });
});
