<template>
<div class="container ">
   <p class="alert alert-danger" role="alert" v-if="error_email">{{error_email}}</p>
   <p class="alert alert-danger" role="alert" v-if="error_password">{{error_password}}</p>
          <div class="row">
            <div class="col">
            </div>
            <div class="col-5">
            <br>
            <h2 class = 'title' align ='center'> Create new account </h2>
              <br>
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
              <button @click="register()" class="btn btn-primary">Register</button>
        <br><br>
        <p>Already have an account? Go to <a href="login">Login</a></p>
        </div>
            <div class="col">
            </div>
  </div>
  </div>
</template>

<script>
export default {
    name: 'register',
    data(){
        return {
            email : "",
            password : "",
            error_email : "",
            error_password : "",
        }
    },
    methods: {
        async register(){
          try{
            const fetched_data = fetch("http://127.0.0.1:5000/register",{
              method: "POST",
              headers: {
                     'Content-Type':'application/json;charset=utf-8'
               },
               body: JSON.stringify({email:this.email,password:this.password})
            })
            .then(
              resp => {
                return resp.json()
              })
              .then(async (register_data) => {
                const {response} = register_data
                if (response.errors){
                const {email,password} = response.errors;
                console.log({email,password});
                this.error_email = email ? email[0]:""
                this.error_password = password ? password[0]:""
                console.log(this.error_email,this.error_password)
              }
              else{
                this.$router.push('login')
              }
              })
              .catch(error => {
              console.log(error);
            });
          }
          catch(error){
            console.log("Registration unsuccessful: " , error)
          }
        }
    }
}
</script>

<style scoped>

</style>