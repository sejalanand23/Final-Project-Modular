<template>
  <div>
      <h1>Edit Deck</h1>
  </div>
</template>

<script>
export default {
    name: "EditDeck",
    data(){
        return {
            deck_name : ''
        }
    },
    created(){
        this.deck_name = this.$route.params.deck_name
        console.log(this.deck_name)
    }
}
</script>

<style>

</style>