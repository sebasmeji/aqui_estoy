const API_URL = "http://127.0.0.1:8000";

const formulario = document.getElementById("form-inicio-sesion");
const mensaje = document.getElementById("mensaje");

formulario.addEventListener("submit", async (evento) => {
    evento.preventDefault();
    mensaje.textContent = "";

    const datos = {
        correo: document.getElementById("email").value.trim(),
        contrasena: document.getElementById("password").value,
    };

    try {
        const respuesta = await fetch(`${API_URL}/usuarios/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(datos),
        });

        if (respuesta.ok) {
            const usuario = await respuesta.json();
            sessionStorage.setItem("usuario", JSON.stringify(usuario));
            window.location.href = "bienvenido.html";
        } else if (respuesta.status === 401) {
            mensaje.textContent = "Correo o contraseña incorrectos.";
        } else if (respuesta.status === 403) {
            mensaje.textContent = "La cuenta no está activa.";
        } else {
            mensaje.textContent = "No se pudo iniciar sesión. Intenta de nuevo.";
        }
    } catch (error) {
        mensaje.textContent = "No se pudo conectar con el servidor.";
    }
});