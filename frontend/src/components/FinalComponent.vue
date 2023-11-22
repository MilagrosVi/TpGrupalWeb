<template>

    <form @submit.prevent="buyTickets">
        <div>
            <label for="name"> Nombre </label>
            <input v-model="user.name" type="text" id="name">
        </div>
        <div>
            <label for="lastname"> Apellido </label>
            <input v-model="user.lastname" type="text" id="lastname">
        </div>
        <div>
            <label for="email"> Email </label>
            <input v-model="user.email" type="email" id="email">
        </div>
        <div>
            <label for="qty"> Numero de entradas </label>
            <input v-model="numberOfTickers" type="number" id="qty">
        </div>
        <div>
            <label for="zones-select"> Selecciona la zona</label>
            <select id="zones-select" v-model="selectedZone">
                <option v-for="zone in zones" :key="zone.id" v-bind:value="zone.descripcion">{{ zone.descripcion }} </option>
            </select>
        </div>
        <div>
            <div v-for="day in days" :key="day.idDia">
                <input type="checkbox" :value="day.numeroDia" v-model="selectedDays">
                <label> {{ day.Recital }} Dia {{ day.numeroDia }} </label>
            </div>
        </div>
        <button type="submit">Comprar</button>
    </form>

</template>

<script>
export default {
    data() {
        return {
            user: {
                name: "",
                lastname: "",
                email: ""
            },
            days: [],
            zones: [],
            selectedZone: "",
            selectedDays: [],
            numberOfTickers: 0,
            pricePerDay: []

        }
    }, mounted() {
        fetch("http://localhost:5000/available-days")
            .then(response => response.json()).
            then(data => {
                this.days = data
                console.log(this.days)
            }
            ).catch(error => console.log(error));

        fetch("http://localhost:5000/zones")
            .then(response => response.json()).
            then(data => {
                this.zones = data
                console.log(this.zones)
            }
            ).catch(error => console.log(error));

    }, methods: {
        buyTickets() {
            console.log("dias ", this.selectedDays)
            console.log("zonas ", this.selectedZone)
            console.log("tickets ", this.numberOfTickers)
            console.log("user ", this.user)
            this.calculatePrice()

            const purchase = {
                days: this.selectedDays,
                zones: this.selectedZone,
                quantity: this.numberOfTickers,
                user: this.user
            }

            fetch("http://localhost:5000/buy", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(purchase),
            }).then(response => response.json()).
                then(data => console.log(data))

        },
        calculatePrice() {
            this.selectedDays.forEach(selectedDay => {
                this.days.forEach(day => {
                    if (day.numeroDia === selectedDay) {
                        this.pricePerDay.push(day.precio)
                    }
                })
            }
            )
            const zonePrice = this.zones.find(zona => zona.descripcion === this.selectedZone).adicional
            console.log("zonePrice", zonePrice)
            const finalPrice = this.pricePerDay.map(price => (price + zonePrice) * this.numberOfTickers)
            console.log(finalPrice)

        }
    }

}
</script>


<style>

</style>