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
                            <img src="">
                        </div>
                    </div>
                    <button type="submit" v-on:click="saveDays">Continuar</button>
                </form>
            </div>
    </section>
</template>

<script>
export default  {
    data (){
        return {
            days: [
    {'idDia': 1, 'Recital': 'Rock Fest', 'numeroDia': '1', 'fecha': '10/11/2023', 'precio':5000,
            'bandas':[
                {'idBanda':1,'nombreBanda': 'La vela Puerca', 'cantIntegrantes': '5', 'url':''},
                {'idBanda':2,'nombreBanda': 'El cuarteto de Nos', 'cantIntegrantes': '4', 'url':''}
                ]
    },
    {'idDia': 2, 'Recital': 'Rock Fest', 'numeroDia': '2', 'fecha': '11/11/2023', 'precio':5000,
            'bandas':[
                {'idBanda':1,'nombreBanda': 'La vela Puerca', 'cantIntegrantes': '5', 'url':'/images/lvp.jpg'},
                {'idBanda':3,'nombreBanda': 'Los Piojos', 'cantIntegrantes': '5', 'url':'/images/lvp.jpg'}
                ]
    }
],

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
           this.$router.push("/")
        }
    },
    // mounted(){
    //     fetch("http://localhost:5000/available-days")
    //     .then(response =>response.json()).
    //     then(data => 
    //     this.days=data
    //     )
    // }
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
