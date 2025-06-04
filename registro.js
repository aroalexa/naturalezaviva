const inp_nombre = document.getElementById("nombre")
const inp_email = document.getElementById("email")
const inp_password = document.getElementById("password")
let usuarios = []
if(JSON.parse(localStorage.getItem('usuarios')) !== ""){
    usuarios = JSON.parse(localStorage.getItem('usuarios'))
}
function registrarse(){
    let nombre = inp_nombre.value
    let email = inp_email.value
    let password = inp_password.value 
    if(nombre === "" || email === "" || password === ""){
        alert("debe completar todos los campos")
        return
    }
    let usuario = {
        nombre:nombre,
        email:email,
        password:password
    }
    usuarios.push(usuario)
    localStorage.setItem("usuarios", JSON.stringify(usuarios))
    inp_email.value = ""
    inp_nombre.value = ""
    inp_password.value = ""
}