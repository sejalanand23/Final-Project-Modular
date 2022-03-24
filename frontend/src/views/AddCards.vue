<template>
<div class="container ">   
   <p class="alert alert-danger" role="alert" v-if="error_message">{{error_message}}</p>
   <p class="alert alert-success" role="alert" v-if="success_message">{{success_message}}</p>
          <div class="row">
            <div class="col">
            </div>
            <div class="col-5">
            <br>
            <h2 class = 'title' align ='center'> Add Cards </h2>
            <br>
              <div class="form-row">
                <div class="form-group">
                  <input type="text" 
                  class="form-control" 
                  name = "card_front" 
                  id = "card_front" 
                  v-model = "card_front"
                  required 
                  placeholder="Card Front" 
                  autocomplete="off">
                </div>
              </div>
              <br>
              <div class="form-row">
                <div class="form-group">
                  <input type="text" 
                  class="form-control" 
                  name = "card_back" 
                  id = "card_back" 
                  v-model = "card_back"
                  required 
                  placeholder="Card Back" 
                  autocomplete="off">
                </div>
              </div>
              <br>
              <button v-on:click="addCard" class="btn btn-primary">Add Card</button>
            </div>
            <div class="col">
            </div>
    </div>
    </div>
</template>

<script>
export default {
    name: 'AddCards',
    data() {
        return {
            card_front : "", 
            card_back : "",
            deck : [],
            email : '',
            error_message : '',
            success_message : ''
        }
    },
    created(){
        this.deck = this.$route.params.deck_data
        console.log(this.deck)
    },
    mounted(){
        this.email = sessionStorage.getItem('email')
        this.auth_token = sessionStorage.getItem('auth-token')
    },
    methods: {
        async addCard(){
        if (!this.card_front || !this.card_back){
            this.error_message = 'Card information cannot be empty'
        }
        else{
            try {
            const card_data = fetch("http://127.0.0.1:5000/api/card", {
              method: "POST",
              headers: {
                     'Content-Type':'application/json;charset=utf-8',
                     'Authentication-Token': `${this.auth_token}`
               },
               body: JSON.stringify({email:this.email,card_front:this.card_front,card_back:this.card_back,deck_id:this.deck.deck_id})
            }).then(resp =>{ 
                    return resp.json()
            })
            .then(card_data => {
              const response = card_data 
              if (response.message){
                this.error_message = response.message
                console.log(response.message)
              }
              else{     
                  this.success_message = "Card added successfully. Add Another"
                  console.log('Card Added')

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
        this.card_front = ''
        this.card_back = ''
        this.success_message = ''
        }
    }

}
</script>

<style>

</style>