<template>
  <div class="container">
    <p class="alert alert-danger" role="alert" v-if="error_message">
      {{ error_message }}
    </p>
    <div class="row">
      <div class="col"></div>
      <div class="col-5">
        <br />
        <h2 class="title" align="center">Create a new Deck</h2>
        <br />
        <div class="form-row">
          <div class="form-group">
            <input
              type="text"
              class="form-control"
              name="deck_name"
              id="deck_name"
              v-model="deck_name"
              required
              placeholder="Deck Name"
              autocomplete="off"
            />
          </div>
        </div>
        <br />
        <button v-on:click="addCards" class="btn btn-primary">
          Add Cards to Deck
        </button>
      </div>
      <div class="col"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "createDeck",
  data() {
    return {
      email: "",
      deck_name: "",
      auth_token: "",
      error_message: "",
      deck: [],
    };
  },
  mounted() {
    this.email = sessionStorage.getItem("email");
    this.auth_token = sessionStorage.getItem("auth-token");
  },
  methods: {
    async addCards() {
      if (!this.deck_name) {
        this.error_message = "Deck name cannot be empty";
      } else {
        try {
          fetch("http://127.0.0.1:5000/api/deck", {
            method: "POST",
            headers: {
              "Content-Type": "application/json;charset=utf-8",
              "Authentication-Token": `${this.auth_token}`,
            },
            body: JSON.stringify({
              email: this.email,
              deck_name: this.deck_name,
            }),
          })
            .then((resp) => {
              return resp.json();
            })
            .then((deck_data) => {
              const response = deck_data;
              if (response.message) {
                this.error_message = response.message;
                console.log(response.message);
              } else {
                this.deck = deck_data;
                console.log(this.deck);
                console.log("Deck Added");
                this.$router.push({
                  name: "AddCards",
                  params: { deck_data: this.deck },
                });
              }
            })
            .catch((error) => {
              console.log(error);
            });
        } catch (error) {
          console.log(error);
        }
      }
    },
  },
};
</script>

<style></style>
