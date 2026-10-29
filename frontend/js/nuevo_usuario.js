const API_URL = "http://127.0.0.1:8000";

const formulario = document.getElementById("form-nuevo-usuario");
const mensaje = document.getElementById("mensaje");

function mostrarMensaje(texto, ok = false) {
    mensaje.textContent = texto;
    mensaje.classList.toggle("ok", ok);
}

formulario.addEventListener("submit", async (evento) => {
    evento.preventDefault();
    mostrarMensaje("");

    const contrasena = document.getElementById("password").value;
    const confirmacion = document.getElementById("confirm-password").value;

    if (contrasena !== confirmacion) {
        mostrarMensaje("Las contraseñas no coinciden.");
        return;
    }

    const datos = {
        nombres: document.getElementById("name").value.trim(),
        apellidos: document.getElementById("last-name").value.trim(),
        correo: document.getElementById("email").value.trim(),
        contrasena: contrasena,
    };

    try {
        const respuesta = await fetch(`${API_URL}/usuarios/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(datos),
        });

        if (respuesta.status === 201) {
            mostrarMensaje("Usuario creado. Redirigiendo...", true);
            setTimeout(() => {
                window.location.href = "inicio_sesion.html";
            }, 800);
        } else if (respuesta.status === 409) {
            mostrarMensaje("Ese correo ya está registrado.");
        } else if (respuesta.status === 422) {
            mostrarMensaje("Revisa los datos. La contraseña debe tener mínimo 8 caracteres.");
        } else {
            mostrarMensaje("No se pudo crear el usuario. Intenta de nuevo.");
        }
    } catch (error) {
        mostrarMensaje("No se pudo conectar con el servidor.");
    }
});