<template>

  <section class="hero">
    <div class="hero-div">
      <h1>ROCK FEST</h1>
      <h2 class="fechas"> 10 y 11  de Noviembre </h2>
      <p class="lugar"> Hipodromo de San Isidro </p>
   </div> 
  </section>
 



</template>

<script>
// export default {

//   data(){
//     return {
//       articles:[],
//     }
//   },
//     methods:{
//       getArticles(){
//         fetch('http://localhost:5000/articles',{
//           method:"GET",
//           headers:{
//             'Content-Type': 'application/json'
//           }
//         })
//         .then(resp => resp.json())
//         .then(data => {
//           let articulos = data.articles;
//           console.log(articulos);
//           articulos.forEach(articulo => {this.articles.push(articulo)})
//           //this.articles.push(...data)
//         })
//         .catch(error =>{
//           console.log(error);
//         })
//       }
//     },
//     //este se llama una vez creado el objeto, ver lifecicle hooks
//     created(){
//       this.getArticles();
//     }
//   }


</script>

<style>

.hero-div{
  overflow-x: hidden;
  width:100vw;
  height: 50vh;
  background-image: url("../assets/Festival-1500x430-1.png");
  background-repeat: no-repeat;
  background-size: cover ;
}

  .hero-div h1{
    display: flex;
    font-size: 3em;
    justify-content:center;
    color: rgb(154,219,228);
  }

  .fechas{display: flex;
  font-size: 2em;
  justify-content:center;
    color: rgb(154,219,228);

  }

  .lugar{
  display: flex;
  font-size: 1.5em;
  justify-content:center;
    color: rgb(154,219,228);

  }
  

</style>
