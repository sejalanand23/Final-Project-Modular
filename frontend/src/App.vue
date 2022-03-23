<template>
  <div :key="isLogged" id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Flashcard Application</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon " ></span>
        </button>
        <div class="collapse navbar-collapse justify-content-center" id="navbarSupportedContent">
          <div class="navbar-nav me-auto mb-2 mb-lg-0">
              <router-link class="btn btn-light" to ="/">Home</router-link> 
              <div class="col-sm-1 col-xs-1 col-md-1 col-lg-1"></div>
              <router-link v-if="isLogged === true" class="btn btn-light" to ="/dashboard">Dashboard</router-link> 
          </div>
          <router-link v-if="isLogged === false" class="btn btn-outline-dark" to ="/login">Login</router-link> 
          <div class="col-sm-1 col-xs-1 col-md-1 col-lg-1"></div>
          <router-link v-if="isLogged === false" class="btn btn-outline-dark" to ="/register">Register</router-link> 
          <span v-if="isLogged === true" class="navbar-text">
              User Logged in: {{this.email}}
          </span>
          <div class="col-sm-1 col-xs-1 col-md-1 col-lg-1"></div>
          <!-- <button v-if="isLogged === true" v-on:click="logout()" class="btn btn-outline-dark">Logout</button> -->
         <button v-if="isLogged === true" v-on:click="logout()" class="btn btn-outline-dark">Logout</button>
        </div>
      </div>
    </nav>
    <br/>
    <router-view />
  </div>
</template>

<script>
export default {
  name : "navbar",
    data() {
        return {
            auth_token : "",
            isLogged: false,
            email : sessionStorage.getItem('email')
        }
    },
    updated() {
        let token = sessionStorage.getItem('auth-token')
        if (token){
          this.isLogged = true;
          console.log(this.isLogged)
          
        }
        else{
          this.isLogged = false;
        }
    },
  methods : {
    logout(){
      try{
        sessionStorage.clear();
        this.$router.push('/');
          }
          catch(error){
            console.log(error)
          }
      },
      // checkIfIsLogged(){
      //   let token = sessionStorage.getItem('auth-token')
      //   if (token){
      //     return true
          
      //   }
      //   else{
      //     return false
      //   }
      // }
    }
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  text-align: center;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav-brand{
  font-weight: bold;
}

nav a.router-link-exact-active {
  /* color: #42b983; */
  cursor: pointer;
  font-weight: 700;
}

btn-outline-dark {
    margin-right: 5px;
    margin-bottom: 5px
}
</style>
