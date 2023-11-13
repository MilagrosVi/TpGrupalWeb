<template>
  <!-- <div class="container mt-5">
    <div v-for="article in articles" v-bind:key="article.id">
        <h3>{{article.title}}</h3>
        <p>{{article.body}}</p>
        <p>{{article.fecha}}</p>
    </div>
  </div> -->

  <section class="hero">
    <div class="hero-div">
      <h1>ROCK FEST</h1>
    </div> 
  </section>
  
  <h1>Festival</h1>


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
}

  .hero-div h1{
    display: flex;
    font-size: 3em;
    justify-content:center;
    color: deeppink;
  }

</style>