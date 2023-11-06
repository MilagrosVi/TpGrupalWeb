<template>
  <div class="container mt-5">
    <div v-for="article in articles" :key="article.id">
        <h3>{{article.title}}</h3>
        <p>{{article.body}}</p>
        <p>{{article.fecha}}</p>
    </div>
  </div>
</template>

<script>
export default {

  data(){
    return {
      articles:[],
    }
  },
    methods:{
      getArticles(){
        fetch('http://localhost:5000/articles',{
          method:"GET",
          headers:{
            'Content-Type': 'application/json'
          }
        })
        .then(resp => resp.json())
        .then(data => {
          let articulos = data.articles;
          console.log(articulos);
          articulos.forEach(articulo => {this.articles.push(articulo)})
          //this.articles.push(...data)
        })
        .catch(error =>{
          console.log(error);
        })
      }
    },
    //este se llama una vez creado el objeto, ver lifecicle hooks
    created(){
      this.getArticles();
    }
  }
</script>

<style>

</style>