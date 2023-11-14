<template>
    <div class="container">
        <div id="logInApp" class="col-sm-8 col-sm-offset-2">
            <h1 class="log">{{nameApp}}</h1>
            
            <form v-on:submit="comprobarUsuario">
                <input type="text" v-model="usuarioIngresado.nombreUsuario" class="form-control" placeholder="nombre de usuario">
                <input type="password" v-model="usuarioIngresado.contrasenia" class="form-control" placeholder="contraseña">
                <input type="submit" value="Ingresar" class="btn btn-block btn-success">
                <router-link to="/otra-pagina">Registrate </router-link>
            </form>
            
            
        </div>
    </div>
</template>

<script>
export default {
    data() {
                return {
                    nameApp: 'LOG IN ',

                    usuarioIngresado: {
                        nombreUsuario:'',
                        contrasenia:''
                    },
                    usuarios: []
                    /*usuarios: [
                        {
                            nombreUsuario: 'juan',
                            contrasenia: 1234
                        },
                        {
                            nombreUsuario: 'pablo',
                            contrasenia: 2415
                        },
                        {
                            nombreUsuario: 'ana',
                            contrasenia: 7845
                        }
                    ]*/
                }
            },
            methods: { //creamos un objetos con funciones (métodos)
                getUsuarios(){
                    fetch('http://10.32.0.38:5000/usuarios',{
                        method:"GET",
                        headers:{
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(resp => resp.json())
                    .then(data => {
                    let usuarios = data.usuarios;
                    console.log(usuarios);
                    usuarios.forEach(usuario => {this.usuarios.push(usuario)})
                    //this.articles.push(...data)
                    })
                    .catch(error =>{
                        console.log(error);
                    })
                },

                comprobarUsuario: function(e){
                    e.preventDefault();
                    var flag = false;
                    console.log(this.usuarioIngresado);
                    this.usuarios.forEach(usuario => {
                        if(this.usuarioIngresado.nombreUsuario == usuario.nombreUsuario && 
                        this.usuarioIngresado.contrasenia == usuario.contrasenia){
                            console.log('Acceso concedido');
                            flag = true;
                            window.location.replace("http://localhost:8080");
                            return;
                        }
                    });

                    if(flag==false)
                        console.log('Acceso denegado');
                },
            },
            created(){
                this.getUsuarios();
            }
}
</script>

<style>
.log{
    color:black;
    font-size: 2.3rem;
    text-align: center;
    line-height:2;
    font-family: 'Manrope', sans-serif;
}
.container{
    display:flex;
    justify-content:center;
    align-items:center;
    height:80vh;
}

.container div form {
    display:block;
    width: 100%;
    margin: 1vh 5vw;
}

    .container div form input {
        display:flex;
        width: 80%;
        justify-content:center;
        align-items:center;
    }
</style>
