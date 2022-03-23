<template>
  <div>
  <h1 class="display-6">Welcome to your Dashboard!</h1>
  <br>
    <table align = "center" class = "table table-bordered">
    <thead class="thead-light">
      <tr>
        <th>Deck Name</th>
        <th>Last Reviewed at</th>
        <th>Last score</th>
        <th>Average Score</th>
        <th>Edit Deck</th>
        <th>Delete</th>
        <th>Start Quiz</th>
      </tr>
    </thead>
    <tbody>

    </tbody>
    <!-- <tbody>
      {% for deck in decks %}
        {% for score in score_info %}
          {% if score['userUCR_foreignid'] == uid and score['deckUCR_foreignid'] == deck['deck_id']%}
            <tr>
              <td>{{ deck['deck_name'] }}</td> 
              <td>{{score['time']}}</td>
              <td>{{score['correct']}}</td>
              <td>{{ deck['deck_average_score'] }}</td>
              <td>
                <form action='{{ url_for("edit_deck",email = email,deck_name = deck["deck_name"]) }}' align = 'center'>
                  <button class="btn btn-outline-secondary" type="submit">Edit Deck</button>
                </form>
              </td>
              <td>
                <form action='/dashboard/{{email}}/{{deck["deck_name"]}}/delete_deck' align = 'center'>
                  <button class="btn btn-outline-secondary" type="submit">Delete Deck</button>
                </form>
              </td>
              <td>
                <form action='/dashboard/{{email}}/{{deck["deck_name"]}}/quiz' align = 'center'>
                  <button class="btn btn-outline-secondary" type="submit">Take Quiz</button>
                </form>
              </td>
            </tr>
          {% endif %}
        {% endfor %}
      {% endfor %}
    </tbody> -->
  </table>
  <!-- <form action='{{ url_for("create_deck",email = email) }}' align = 'center'>
    <button class="btn btn-outline-secondary" type="submit">Create New Deck</button>
</form> -->
  </div>
</template>

<script>
export default {
  name : 'dashboard',
  props: { email_id : String },
  data() {
    return {
      email : "",
      auth_token : ""
    }
  },
  // beforeMount(){
  //   this.auth_token = sessionStorage.getItem('auth-token')
  //   this.email = sessionStorage.getItem('email')
  //   console.log(this.email)
  //   fetch("http://127.0.0.1:5000/api/<>user", {
  //             method: "GET",
  //             headers: {
  //                    'Content-Type':'application/json;charset=utf-8',
  //                    'Authentication-Token':response.user.authentication_token
  //              }
  //           })
  //               .then(r => console.log(r.json()))
  // }

}
</script>

<style>

</style>