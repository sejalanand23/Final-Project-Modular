<template>
  <div>
    <p class="alert alert-danger" role="alert" v-if="error_message">{{error_message}}</p>
  <h1 class="display-6">Welcome to your Dashboard!</h1>
  <br>
    <table align = "center" class = "table table-bordered">
    <thead class="thead-light">
      <tr>
        <th>Deck Name</th>
        <th>Last Reviewed at</th>
        <th>Last score</th>
        <th>Average Score</th>
        <th>Edit Deck</th>
        <th>Delete</th>
        <th>Start Quiz</th>
      </tr>
    </thead>
    <tbody>

    </tbody>
    <tbody>
      <tr v-for="deck in decks" :key="deck.deck_id">
      <td>{{deck.deck_name}}</td>
      <td>{{deck.time}}</td>
      <td>{{deck.correct}}</td>
      <td>{{deck.deck_average_score}}</td>
      <td><button @click="editDeck" class="btn btn-outline-dark">Edit Deck</button></td>
      <td><button @click="deleteDeck" class="btn btn-outline-dark">Delete</button></td>
      <td><button @click="quiz" class="btn btn-outline-dark">Take Quiz</button></td>
      </tr>
    </tbody> 
  </table>
  <router-link class="btn btn-outline-dark" to ="/createDeck">Create a new Deck</router-link> 
  </div>
</template>

<script>
export default {
  name : 'dashboard',
  data() {
    return {
      email : "",
      auth_token : "",
      decks : [],
      error_message: ''
    }
  },
  async created(){
    this.auth_token = sessionStorage.getItem('auth-token')
    this.email = sessionStorage.getItem('email')
    console.log(this.email)
    return fetch(`http://127.0.0.1:5000/api/deck/${this.email}`, {
              method: "GET",
              headers: {
                     'Content-Type':'application/json;charset=utf-8',
                     'Authentication-Token': `${this.auth_token}`
               }
            })
                .then(res => res.json())
                .then(data => {
                  this.decks = data
                }
                )
                .catch(error => console.log(error))
  },
  methods : {
    async deleteDeck(){
      try {
            const deck_data = fetch("http://127.0.0.1:5000/api/deck", {
              method: "DELETE",
              headers: {
                     'Content-Type':'application/json;charset=utf-8',
                     'Authentication-Token': `${this.auth_token}`
               },
               body: JSON.stringify({email:this.email,deck_name:this.deck_name})
            }).then(resp =>{ 
                return resp.json()
            })
            .then(async (deck_data) => {
                console.log({deck_data})
              const response = deck_data 
              console.log(response)
              if (!response){
                this.error_message = response.message
                console.log(response.message)
              }
              else{     

                  console.log('Deck Deleted')        
              }
            }
            )
            .catch(error => {
              console.log(error);
            });
          }         
            catch(error){
            console.log(error)
          }

    }
  }
}
</script>

<style>

</style>