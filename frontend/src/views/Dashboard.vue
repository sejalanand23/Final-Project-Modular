<template>
  <h1>Welcome to your Dashboard!</h1>
</template>

<script>
export default {
  name : 'dashboard',
  beforeMount(){
    console.log(sessionStorage.getItem('auth-token'))
    console.log(sessionStorage.getItem('email'))
  }
}
</script>

<style>

</style>