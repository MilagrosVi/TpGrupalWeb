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
            <li class="nav-item1">
            <router-link class="" aria-current="page" to="/">Sobre Nosotros</router-link>
            </li>
            <li class="nav-item2">
            <router-link class="" to="/select-days">Comprar Tickets</router-link>
            </li>
        </ul>   
    </div>

  </div>

</template>

<script>
export default {

}
</script>

<style>

.main-header{
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 1%;
}

.left-nav{
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items:center;
    flex: 50vw;
}

.right-nav{
    display: flex;
    flex-direction: row;
    align-items: center;
    flex: 50vw;
    text-decoration:none;
}

.ul-nav {
    display: flex;
    flex-direction: row;
    list-style: none;
    width: 33vw;
    justify-content: space-evenly;
    font-family: 'Manrope', sans-serif;
    font-weight: 600;
    font-size: small;
}

a{
    text-decoration: none;
    color: black;
}

.nav-item1{
    padding: 2%;
    background-color: #f2defa;
    border-radius: 7%;
}

.nav-item2{
    padding: 2%;
    background-color: greenyellow;
    border-radius: 7%;
}

</style>