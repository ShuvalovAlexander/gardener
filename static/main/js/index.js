// изменение цвета
const black = document.querySelector(".black-color");
const red = document.querySelector(".red-color");
const white = document.querySelector(".white-color");
const textColor = document.querySelector("#text-color");

// память
const smal = document.querySelector(".smal");
const medium = document.querySelector(".medium");
const textMemory = document.querySelector("#textMemory");

// группы кнопок
const colorButtons = [black, red, white];
const memoryButtons = [smal, medium];

function setActiveButton(activeButton, group) {
  group.forEach((btn) => btn.classList.remove("active"));
  activeButton.classList.add("active");
}

black.addEventListener("click", () => {
  textColor.textContent = "Выбран: Черный";
  setActiveButton(black, colorButtons);
});
red.addEventListener("click", () => {
  textColor.textContent = "Выбран: Красный";
  setActiveButton(red, colorButtons);
});
white.addEventListener("click", () => {
  textColor.textContent = "Выбран: Белый";
  setActiveButton(white, colorButtons);
});

smal.addEventListener("click", () => {
  textMemory.textContent = "64 ГБ";
  setActiveButton(smal, memoryButtons);
});
medium.addEventListener("click", () => {
  textMemory.textContent = "128 ГБ";
  setActiveButton(medium, memoryButtons);
});

// свернуть/развернуть текст
document.querySelector(".toggle-link").addEventListener("click", function(e) {
  e.preventDefault();
  const hiddenText = document.querySelector(".hidden-text");
  const link = this;
  
  if (hiddenText.style.display === "none") {
    hiddenText.style.display = "block";
    link.textContent = "свернуть";
  } else {
    hiddenText.style.display = "none";
    link.textContent = "развернуть";
  }
});