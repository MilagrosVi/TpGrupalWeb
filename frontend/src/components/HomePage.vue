<template>
  <section class="hero">
    <div class="hero-div">
      <h1>ROCK FEST</h1>
      <h2 class="fechas">10 y 11 de Noviembre</h2>
      <p class="lugar">Hipódromo de San Isidro</p>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      articles: [],
    };
  },
  methods: {
    getArticles() {
      fetch('http://localhost:5000/articles', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          let articulos = data.articles;
          console.log(articulos);
          articulos.forEach((articulo) => {
            this.articles.push(articulo);
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getArticles();
  },
};
</script>

<style>
.hero-div {
  overflow-x: hidden;
  width: 100vw;
  height: 50vh;
  background-image: url("../assets/Festival-1500x430-1.png");
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.hero-div h1,
.hero-div h2,
.hero-div p {
  font-family: Julius Sans One;
  color: white;
}

.hero-div h1 {
  font-size: 10vh;
}

.fechas {
  font-size: 2em;
}

.lugar {
  font-size: 1.5em;
}
</style>