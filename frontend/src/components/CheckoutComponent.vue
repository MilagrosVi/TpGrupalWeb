<template>

    <h2 class="h2-check">Dias seleccionados</h2>
  
      <div v-for="day in days" v-bind:key="day.idDia">
          <p class="p-check">Dia {{day.nroDia}}</p>
      </div>
  
    <form class="check">
      <input class="qty-input" type="number" v-model="quantity">
      <button class="btn btn-block btn-info" type="submit" v-on:click="buy"> Comprar</button>
    </form>
    
</template>
  
<script>
  export default {
      data(){
          return{
              quantity: 0,
              days: []
          }
      },
      mounted(){
          let purchase = JSON.parse(localStorage.getItem("purchase")).dias
          this.days = purchase
      },
      methods:{
          buy(){
              localStorage.setItem("quantity", JSON.stringify(this.quantity))
              this.$router.push("/final-component")
          }
      }   
  }
</script>
  
<style>

.h2-check{
    font-family: Julius Sans One;
    font-weight: 700;
    font-size: 4vh;
    margin: 4vw;
    margin-bottom: 2vw;
}

.p-check{
    font-family: Julius Sans One;
    font-weight: 700;
    font-size: 3vh;
    margin-left: 4vw;
    margin-bottom: 0;
}

.check{
    display: flex;
    flex-direction: column;
    width: 10vw;
    justify-content: flex-start;
    margin-top:0;
    margin-left: 4vw;
}

.qty-input{
    margin-bottom: 1vw;
    width: 10vw;
}


</style>