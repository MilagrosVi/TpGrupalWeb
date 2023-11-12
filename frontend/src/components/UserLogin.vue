<template>
    <div>
        <h1>Login</h1>
        <form @submit="checkUser">
            <input type="text" v-model="user.name" placeholder="User">
            <input type="password" v-model="user.password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
    </div>
</template>

<script>
export default {
    name: "UserLogin",
    data () {
        return {
            user: {
                name: "",
                password: ""
            }
        }
    },
    methods: {
        checkUser(e){
            e.preventDefault();

            fetch('http://localhost:5000/api/login',{
                method: "POST",
                headers:{
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.user)
            }
            ).then( response => { console.log(response)})
        }
    }
}
</script>

<styles>

</styles>