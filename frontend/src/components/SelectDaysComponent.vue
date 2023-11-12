<template>
    <section>
        <h1>COMPRÁ TUS TICKETS</h1>
            <div>
                <form>
                    <div v-for="day in days" class="card"  v-bind:key="day.idDia">
                        <input type="checkbox" v-bind:value="day.numeroDia" v-model="selectedDays">
                        <h2> {{day.Recital}} Dia {{day.numeroDia}}</h2>
                        <h3>{{day.fecha}}</h3>
                        <p>{{day.precio}}</p>
                        <img src="">
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
                {'idBanda':1,'nombreBanda': 'La vela Puerca', 'cantIntegrantes': '5', 'url':'/images/lvp.jpg'},
                {'idBanda':2,'nombreBanda': 'El cuarteto de Nos', 'cantIntegrantes': '4', 'url':'/images/lvp.jpg'}
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
}

h1{
    padding: 3vw;
}

</style>