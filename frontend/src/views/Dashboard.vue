<template>
  <h1>Welcome to your Dashboard!</h1>
</template>

<script>
export default {
  name : 'dashboard',
  props: { email_id : String },
  data() {
    return {
      email : ""
    }
  },
  created(){
    // console.log(sessionStorage.getItem('auth-token'))
    this.email = sessionStorage.getItem('email')
    console.log(this.email)
  }

}
</script>

<style>

</style>