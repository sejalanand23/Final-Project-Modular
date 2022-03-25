<template>
  <div class="container">
    <p class="alert alert-danger" role="alert" v-if="error_message">
      {{ error_message }}
    </p>
    <div class="row">
      <div class="col"></div>
      <div class="col-7" align="center">
        <br />
        <h2 class="title" align="center">Quiz for {{ deck_name }}</h2>
        <br />
        <br />
        <div
          class="card text-center text-dark bg-light mb-3"
          style="max-width: 30rem"
        >
          <div class="card-header">Card Front</div>
          <div
            v-for="card in cards.slice(0, 1)"
            :key="card.card_id"
            class="card-body"
          >
            <h4 class="card-title">{{ card.card_front }}</h4>
            <div class="form-row">
              <div class="form-group">
                <input
                  type="text"
                  class="form-control"
                  name="answer"
                  id="answer"
                  v-model="answer"
                  required
                  placeholder="Enter Answer "
                  autocomplete="off"
                />
              </div>
            </div>
            <br />
          </div>
        </div>

        <div
          class="card text-center text-dark bg-light mb-3"
          style="max-width: 30rem"
        >
          <div class="card-body">
            <h6 class="card-subtitle mb-2">Select Difficulty Level</h6>
            <br />
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                name="difficulty"
                id="easy"
                value="easy"
                checked
              />
              <label class="form-check-label" for="easy"> Easy </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                name="difficulty"
                id="medium"
                value="medium"
              />
              <label class="form-check-label" for="medium"> Medium </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                name="difficulty"
                id="hard"
                value="hard"
              />
              <label class="form-check-label" for="hard"> Hard </label>
            </div>
            <br />
          </div>
        </div>
        <button @click="submit" class="btn btn-primary">Submit</button>
      </div>
      <div class="col"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DeckQuiz",
  data() {
    return {
      deck_name: "",
      error_message: "",
      answer: "",
      auth_token: "",
      email: "",
      cards: [],
    };
  },

  async created() {
    this.deck_name = this.$route.params.deck_name;
    this.auth_token = sessionStorage.getItem("auth-token");
    this.email = sessionStorage.getItem("email");
    return fetch(
      `http://127.0.0.1:5000/api/quiz/${this.email}/${this.deck_name}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.auth_token}`,
        },
      }
    )
      .then((res) => res.json())
      .then((data) => {
        this.cards = data;
      })
      .catch((error) => console.log(error));
  },
};
</script>

<style></style>
