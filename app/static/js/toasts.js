window.onload = (event) => {
    let alert = document.querySelector(".toast");
    let bootstrapAlert = new bootstrap.Toast(alert);
    bootstrapAlert.show();
}