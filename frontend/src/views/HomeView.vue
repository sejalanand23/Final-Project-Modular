<template>
  <div class="home">
    <br>
    <pre><blockquote class="blockquote"> Make Flashcards online. Track your progress. </blockquote></pre>
    <br>
    <img alt="Vue logo" src="../assets/home.jpeg" height="450" width="800" />
    
     <br><br> 
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  components: {
    HelloWorld,
  },
};
</script>

<style scoped>
.blockquote{
  max-width: 100%;
  font-size: xx-large;
}

</style>
