<template>
    <section>
        <div>
            <h1>COMPRÁ TUS TICKETS</h1>
        </div>
            <div class="div-form">
                <form>
                    <div v-for="day in days" class="card"  v-bind:key="day.idDia">
                        <div>
                            <input type="checkbox" v-bind:value="day.numeroDia" v-model="selectedDays">
                        </div>
                        <div class="card-data">
                            <h2> {{day.Recital}} Dia {{day.numeroDia}}</h2>
                            <h3>{{day.fecha}}</h3>
                            <p> Precio: {{day.precio}}</p>
                            <div v-for="banda in day.bandas" :key="banda.idBanda">
                                <h4>{{banda.nombreBanda}}</h4>
                            </div>
                        </div>
                    </div>
                    <button class="btn btn-block btn-info" type="submit" v-on:click="saveDays"> Continuar</button>
                </form>
            </div>
    </section>
</template>

<script>
export default  {
    data (){
        return {
            days: [],
            selectedDays: []
        }
    },
    methods: {
        saveDays(e){
            e.preventDefault()
            console.log(this.selectedDays)
            const daysToSave = []
            this.selectedDays.forEach( day =>
            {
            const obj = {
                idDia: day,
                nroDia: day
            }
            daysToSave.push(obj)
           })
           localStorage.setItem("purchase", JSON.stringify({dias: daysToSave}))
           this.$router.push("/checkout")
        }
    },
    mounted(){
        fetch("http://127.0.0.1:5000//available-days")
        .then(response =>response.json()).
        then(data => 
        this.days=data
        )
    }
}

</script>

<style>

section{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: black;
}

h1{
    padding: 3vw;
    color: white;
}

.div-form{
    padding-bottom: 3vw;
}

.boton{
    align:center;
}

.card{
    margin: 2vw;
    margin-top: 0;
    padding: 2vw;
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.card-data{
    display: flex;
    flex-direction: column;
    text-align: center;
    justify-content: center;
    align-items: center;
}

input{
    margin-right: 1vw;
    margin-top: 1vw;
}

</style>
