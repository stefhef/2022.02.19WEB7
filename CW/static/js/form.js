const upload = document.querySelector('#inputGroupFile01');
const result = document.querySelector('#result');

upload.addEventListener("change", (e) => {
  previewFunc(e.target.files[0]);
});

function previewFunc(file) {
  if (!file.type.match(/image.*/)) return false;
  const reader = new FileReader();

  reader.addEventListener("load", (e) => {
    const img = document.createElement('img');
    img.src = e.target.result;
    result.innerHTML = '';
    result.append(img);
  });
  reader.readAsDataURL(file);
}