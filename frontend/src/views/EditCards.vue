<template>
  <div class="container">
    <p class="alert alert-danger" role="alert" v-if="error_message">
      {{ error_message }}
    </p>
    <p class="alert alert-success" role="alert" v-if="success_message">
      {{ success_message }}
    </p>
    <h1 class="display-6">Cards in Deck: {{ this.deck_name }}</h1>
    <br />
    <table align="center" class="table table-bordered">
      <thead class="thead-light">
        <tr>
          <th>Card Front</th>
          <th>Card Back</th>
          <th>Delete Card</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="card in cards" :key="card.card_id">
          <td>{{ card.card_front }}</td>
          <td>{{ card.card_back }}</td>
          <td>
            <button
              @click="deleteCard(card.card_id)"
              class="btn btn-outline-dark"
            >
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "EditCards",
  data() {
    return {
      deck_name: "",
      error_message: "",
      success_message: "",
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
  methods: {
    async deleteCard(card_id) {
      try {
        fetch(`http://127.0.0.1:5000/api/card/${card_id}`, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.auth_token}`,
          },
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (card_data) => {
            const response = card_data;
            console.log(response);
            if (!response) {
              this.error_message = response.message;
              console.log(response.message);
            } else {
              console.log("Deck Deleted");
              this.$router.go();
            }
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style></style>
