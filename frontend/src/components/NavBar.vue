<template>

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">

  <div class="main-header"> 

    <div class="left-nav">
        <ul class="ul-nav">
            <a href="#"> ROCK FEST</a>
        </ul>
    </div>

    <div class="right-nav"> 
        <ul class="ul-nav">
            <li class="nav-item">
                <router-link to="">Log In</router-link>
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
    background-color: rgb(154, 219, 228); /* Fondo de la barra */
}

.left-nav, .right-nav {
    display: flex;
    align-items: center;
}

.ul-nav {
    display: flex;
    list-style: none;
    font-family: 'Manrope', sans-serif;
    font-weight: 600;
    font-size: small;
}

.ul-nav a {
    text-decoration: none;
    color: white; /* Color del texto en la barra */
}

.nav-item {
    padding: 10px;
    border-radius: 5px;
    margin: 0 5px; /* Separación entre elementos */
    transition: background-color 0.3s ease; /* Efecto de transición en el color de fondo */
}

.nav-item:hover {
    background-color: rgb(218, 205, 205); /* Color de fondo al pasar el ratón */
}

</style>


