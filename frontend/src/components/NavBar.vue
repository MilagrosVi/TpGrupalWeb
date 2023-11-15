<template>

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">

  <div class="main-header"> 

    <div class="left-nav">
        <ul class="ul-nav">
            <li class="nav-item">
                <router-link to="/">Home</router-link>
            </li>
        </ul>
    </div>

    <div class="right-nav"> 
        <ul class="ul-nav">
            <li class="nav-item">
                <router-link to="/login">Log In</router-link>
            </li>
            <li class="nav-item">
                <router-link to="/select-days">Comprar Tickets</router-link>
            </li>
        </ul>   
    </div>

  </div>

</template>

<script>
export default {

}
</script>

<style scoped>

.main-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1%;
    background-color: black; /* Fondo de la barra */
}

.left-nav, .right-nav {
    padding: 10px;
    border-radius: 5px;
   

}





</style>
