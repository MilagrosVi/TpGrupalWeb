<template>
    <div class="container  mt-4">
        <div id="logInApp" class="col-sm-8 col-sm-offset-2">
            <h1>{{nameApp}}</h1>
            
            <form v-on:submit="comprobarUsuario">
                <input type="text" v-model="usuarioIngresado.nombreUsuario" class="form-control">
                <input type="password" v-model="usuarioIngresado.contrasenia" class="form-control">
                <input type="submit" value="Ingresar" class="btn btn-block btn-success">
            </form>
            <br>
            
        </div>
    </div>
</template>

<script>
export default {
    data() {
                return {
                    nameApp: 'LogIn',

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

</style>
