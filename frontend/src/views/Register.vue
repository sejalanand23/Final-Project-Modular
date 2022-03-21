<template>
<div class="container ">
          <div class="row">
            <div class="col">
            </div>
            <div class="col-5">
            <br>
            <h2 class = 'title' align ='center'> Create new account </h2>
              <div class="form-row">
                <div class="form-group">
                  <input 
                  type="text" 
                  class="form-control" 
                  name = "username" 
                  id = "username" 
                  v-model = "username" 
                  required 
                  placeholder="username" 
                  autocomplete="off">
                </div>
              </div>
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
        <div class="form-row">
            <div class="form-group">
              <input type="password" 
              class="form-control" 
              name = "confirmpassword" 
              id = "confirmpassword" 
              v-model = "confirmPassword" 
              required 
              placeholder="Confirm password" 
              autocomplete="off">
            </div>
        </div>
        <br>
              <button @click="register()" class="btn btn-primary">Register</button>
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
            username : "",
            email : "",
            password : "",
            confirmPassword : ""
        }
    },
    methods: {
        register: function(){
            console.log(this.username,this.email, this.password, this.confirmPassword)
        }
    }
}
</script>

<style scoped>

</style>