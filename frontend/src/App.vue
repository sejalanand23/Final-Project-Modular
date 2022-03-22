<template>
  <div id="app">
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
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div class="navbar-nav me-auto mb-2 mb-lg-0">
            <!-- <li class="nav-item"> -->
              <!-- <router-link to="/" class = "nav-item">Home</router-link> -->
              <router-link class="nav-item btn btn-light" to ="/">Home</router-link> 
            <!-- </li> -->
          </div>
          <router-link class="nav-item btn btn-light" to ="/login">Login</router-link> 
          <router-link class="nav-item btn btn-light" to ="/register">Register</router-link> 
        </div>
      </div>
    </nav>
    <br/>
    <router-view />
  </div>
</template>


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
</style>
