<template>
  <div>
    <p class="alert alert-danger" role="alert" v-if="error_message">
      {{ error_message }}
    </p>
    <p class="alert alert-success" role="alert" v-if="success_message">
      {{ success_message }}
    </p>
    <!-- <ul>
            <li v-for="message in messages" :key="message"> {{message}} </li>
    </ul> -->
    <h1 class="display-6">Welcome to your Dashboard!</h1>
    <br />
    <table align="center" class="table table-bordered">
      <thead class="thead-light">
        <tr>
          <th>Deck Name</th>
          <th>Last Reviewed at</th>
          <th>Last score</th>
          <th>Average Score</th>
          <th>Add Cards</th>
          <th>Edit Deck Name</th>
          <th>View/Edit Cards</th>
          <th>Delete Deck</th>
          <th>Take Quiz</th>
        </tr>
      </thead>
      <tbody></tbody>
      <tbody>
        <tr v-for="deck in decks" :key="deck.deck_id">
          <td>{{ deck.deck_name }}</td>
          <td>{{ deck.time ? deck.time : "No quiz taken" }}</td>
          <td>
            {{
              deck.quiz_count != 0
                ? deck.correct.toFixed(2) + "%"
                : "No quiz taken"
            }}
          </td>
          <td>
            {{
              deck.deck_average_score != null
                ? deck.deck_average_score.toFixed(2) + "%"
                : "No quiz taken"
            }}
          </td>
          <td>
            <button class="btn btn-outline-dark">
              <router-link
                style="text-decoration: none; color: inherit"
                :to="{ name: 'AddCards', params: { deck_data: deck } }"
              >
                Add Cards
              </router-link>
            </button>
          </td>
          <td>
            <button class="btn btn-outline-dark">
              <router-link
                style="text-decoration: none; color: inherit"
                :to="`/dashboard/deck/${deck.deck_name}/edit`"
                >Edit</router-link
              >
            </button>
          </td>
          <td>
            <button class="btn btn-outline-dark">
              <router-link
                style="text-decoration: none; color: inherit"
                :to="`/dashboard/deck/${deck.deck_name}/edit/cards`"
              >
                View/Edit
              </router-link>
            </button>
          </td>
          <td>
            <button
              @click="deleteDeck(deck.deck_name)"
              class="btn btn-outline-dark"
            >
              Delete
            </button>
          </td>
          <td>
            <button class="btn btn-outline-dark" @click="storeID(deck.deck_id)">
              <router-link
                style="text-decoration: none; color: inherit"
                :to="`/dashboard/deck/${deck.deck_name}/quiz`"
              >
                Start Quiz
              </router-link>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <router-link class="btn btn-outline-dark" to="/createDeck"
      >Create a new Deck</router-link
    >
    <br />
    <br />
    <button class="btn btn-outline-dark" @click="export_data">
      Export Decks as CSV
    </button>
  </div>
</template>

<script>
export default {
  name: "UserDashboard",
  data() {
    return {
      email: "",
      auth_token: "",
      decks: [],
      error_message: "",
      success_message: "",
      // messages : []
    };
  },
  // mounted: function() {
  //     source = new EventSource("/stream");
  //     source.addEventListener('export', event => {
  //         let data = JSON.parse(event.data);
  //         this.messages.push(data.message)
  //     }, false);
  //   },
  async created() {
    sessionStorage.removeItem("deck_id");
    this.auth_token = sessionStorage.getItem("auth-token");
    this.email = sessionStorage.getItem("email");
    console.log(this.email);
    return fetch(`http://127.0.0.1:5000/api/deck/${this.email}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json;charset=utf-8",
        "Authentication-Token": `${this.auth_token}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        this.decks = data;
      })
      .catch((error) => console.log(error));
  },
  methods: {
    async deleteDeck(deck_name) {
      try {
        fetch("http://127.0.0.1:5000/api/deck", {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.auth_token}`,
          },
          body: JSON.stringify({ email: this.email, deck_name: deck_name }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (deck_data) => {
            const response = deck_data;
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
    storeID(deck_id) {
      sessionStorage.setItem("deck_id", deck_id);
    },
    async export_data() {
      return fetch(`http://127.0.0.1:5000/api/export/decks/${this.email}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.auth_token}`,
        },
      })
        .then((res) => res.json())
        .then((r) => {
          console.log(r);
          this.success_message = "Export Complete. File is downloaded.";
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style>
.btn {
  white-space: nowrap;
}
</style>
