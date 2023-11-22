<template>

    <h1>Checkout</h1>
      <h2>Dias seleccionados</h2>
  
      <div v-for="day in days" v-bind:key="day.idDia">
          <p>Dia {{day.nroDia}}</p>
      </div>
  
    <form>
      <input type="number" v-model="quantity">
      <button type="submit" v-on:click="buy"> Comprar</button>
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
          }
      }   
  }
  </script>
  
  <style>
  
  </style>