<template>
  <div class="container ">
          <div class="row">
            <div class="col">
            </div>
            <div class="col-5">
            <br>
            <h2 class = 'title' align ='center'> Login </h2>
              <div class="form-row">
                <div class="form-group">
                  <input type="email" 
                  class="form-control" 
                  name = "email" 
                  id = "email" 
                  v-model = "email"
                  required 
                  placeholder="email" 
                  autocomplete="off">
                </div>
              </div>
              <br>
              <div class="form-row">
                <div class="form-group">
                  <input type="password" 
                  class="form-control" 
                  name = "password" 
                  id = "password"  
                  v-model = "password" 
                  required 
                  placeholder="password" 
                  autocomplete="off">
                </div>
              </div>
              <br>
              <button @click="login" class="btn btn-primary">Sign in</button>
            </div>
            <div class="col">
            </div>
    </div>
    </div>
</template>

<script>
export default {
    name: 'login',
    data() {
      return {
        email : "",
        password : ""
      }
  },
    methods: {
        async login(){
          try {
            let user_credentials = {
              email : this.email,
              password : this.password
            };
            await fetch("http://127.0.0.1:5000/login?include_auth_token", {
               method: "POST",
               headers: {
                     'Content-Type':'application/json'
               },
               body: JSON.stringify(user_credentials)
     }).then(data=>data.json()).then(r=>console.log(r));
          }
          catch(error){
            console.log(error)
          }
        }
    }
}
</script>

<style scoped>

</style>