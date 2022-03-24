<template>
  <div class="container">
      <p class="alert alert-danger" role="alert" v-if="error_message">{{error_message}}</p>
      <p class="alert alert-success" role="alert" v-if="success_message">{{success_message}}</p>
      <div class="row">
            <div class="col">
            </div>
            <div class="col-5">
            <br>
            <h2 class = 'title' align ='center'> Edit Deck: {{this.deck_name}} </h2>
            <br>
              <div class="form-row">
                <div class="form-group">
                  <input type="text" 
                  class="form-control" 
                  name = "new_deck_name" 
                  id = "new_deck_name" 
                  v-model = "new_deck_name"
                  required 
                  placeholder="Deck Name" 
                  autocomplete="off">
                </div>
              </div>
              <br>
              <button v-on:click="editDeck" class="btn btn-primary">Change Deck Name</button>
            </div>
            <div class="col">
            </div>
    </div>
  </div>
</template>

<script>
export default {
    name: "EditDeck",
    data(){
        return {
            deck_name : '',
            new_deck_name : '',
            error_message : '',
            success_message : '',
            auth_token : '',
            email : ''
        }
    },
    created(){
        this.deck_name = this.$route.params.deck_name
        console.log(this.deck_name)
    },
    methods: {
        async editDeck(){
        if (!this.deck_name){
            this.error_message = 'Deck name cannot be empty'
        }
        else{
            try {
            this.auth_token = sessionStorage.getItem('auth-token')
            this.email = sessionStorage.getItem('email')
            const deck_data = fetch(`http://127.0.0.1:5000/api/deck/edit/${this.deck_name}`, {
              method: "PUT",
              headers: {
                     'Content-Type':'application/json;charset=utf-8',
                     'Authentication-Token': `${this.auth_token}`
               },
               body: JSON.stringify({email:this.email,deck_name:this.new_deck_name})
            }).then(resp =>{ 
                    return resp.json()
            })
            .then(deck_data => {
              const response = deck_data 
              if (response.message){
                this.error_message = response.message
                console.log(response.message)
              }
              else{     
                  this.success_message = "Deck name updated successfully"     
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
        this.deck_name = this.new_deck_name
        this.new_deck_name = ''
        }
    }
}
</script>

<style>

</style>