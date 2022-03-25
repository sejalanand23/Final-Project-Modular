<template>
  <div class="container">
    <p class="alert alert-danger" role="alert" v-if="incorrect_message">
      {{ incorrect_message }}
    </p>
    <p class="alert alert-success" role="alert" v-if="success_message">
      {{ success_message }}
    </p>
    <div v-if="quiz_mode === true" class="row">
      <div class="col"></div>
      <div class="col-7" align="center">
        <br />
        <h2 class="title" align="center">Quiz for {{ deck_name }}</h2>
        <br />
        <br />
        <div v-for="card in cards.slice(a, b)" :key="card.card_id">
          <div
            class="card text-center text-dark bg-light mb-3"
            style="max-width: 30rem"
          >
            <div class="card-header">Card Front</div>
            <div class="card-body">
              <h4 class="card-title">{{ card.card_front }}</h4>
              <div class="form-row">
                <div class="form-group">
                  <input
                    v-if="answered === false"
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
          <button
            v-if="(answered === false) & (lastQues === false)"
            @click="submit(card.card_back)"
            class="btn btn-outline-dark"
            style="max-width: 10rem"
          >
            Submit Answer
          </button>
          <button
            v-if="(answered == true) & (lastQues == false)"
            @click="next"
            class="btn btn-outline-dark"
            style="max-width: 10rem"
          >
            Next Question
          </button>
          <button
            v-if="lastQues === true"
            @click="result"
            class="btn btn-outline-dark"
            style="max-width: 10rem"
          >
            Show Result
          </button>
        </div>
      </div>
      <div class="col"></div>
    </div>

    <div v-if="quiz_mode == false" class="row">
      <div class="col"></div>
      <div class="col-5">
        <br />
        <h2 class="title" align="center">
          Your score is: {{ this.score }} out of {{ this.total }}
        </h2>
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
      answered: false,
      lastQues: false,
      deck_name: "",
      card_back: "",
      incorrect_message: "",
      success_message: "",
      answer: "",
      auth_token: "",
      email: "",
      cards: [],
      quiz_mode: true,
      total: 0,
      a: 0,
      b: 1,
      score: 0,
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
        this.total = this.cards.length;
      })
      .catch((error) => console.log(error));
  },
  methods: {
    submit(card_back) {
      this.card_back = card_back;
      console.log(this.card_back);
      console.log(this.answer);
      this.answered = true;
      if (this.card_back.toLowerCase() == this.answer.toLowerCase()) {
        this.success_message = "Correct Answer! 👍 ";
        this.score++;
      } else {
        this.incorrect_message = `Wrong Answer ❌ The correct answer is: ${this.card_back}`;
      }
      if (this.b == this.total) {
        this.lastQues = true;
      }
      this.answer = "";
    },
    next() {
      if (this.b + 1 <= this.total) {
        this.a++;
        this.b++;
        console.log(this.b);
        this.success_message = "";
        this.incorrect_message = "";
        this.answered = false;
      }
    },
    result() {
      this.success_message = "";
      this.incorrect_message = "";
      this.quiz_mode = false;
    },
  },
};
</script>

<style scoped>
.btn {
  margin: 0 auto;
}
</style>
