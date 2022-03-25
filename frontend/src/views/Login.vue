<template>
  <div class="container">
    <p class="alert alert-danger" role="alert" v-if="error_email">
      {{ error_email }}
    </p>
    <p class="alert alert-danger" role="alert" v-if="error_password">
      {{ error_password }}
    </p>
    <div class="row">
      <div class="col"></div>
      <div class="col-5">
        <br />
        <h2 class="title" align="center">Login</h2>
        <div class="form-row">
          <div class="form-group">
            <input
              type="email"
              class="form-control"
              name="email"
              id="email"
              v-model="email"
              required
              placeholder="email"
              autocomplete="off"
            />
          </div>
        </div>
        <br />
        <div class="form-row">
          <div class="form-group">
            <input
              type="password"
              class="form-control"
              name="password"
              id="password"
              v-model="password"
              required
              placeholder="password"
              autocomplete="off"
            />
          </div>
        </div>
        <br />
        <button @click="login" class="btn btn-primary">Sign in</button>
        <br /><br />
        <p>New User? <a href="register">Create</a> a new account.</p>
      </div>
      <div class="col"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserLogin",
  data() {
    return {
      email: "",
      password: "",
      error_email: "",
      error_password: "",
      auth: "",
      is_authenticated: false,
    };
  },
  methods: {
    async login() {
      try {
        fetch("http://127.0.0.1:5000/login?include_auth_token", {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (login_data) => {
            const { response } = login_data;
            if (response.errors) {
              const { email, password } = response.errors;
              console.log({ email, password });
              this.error_email = email ? email[0] : "";
              this.error_password = password ? password[0] : "";
              console.log(this.error_email, this.error_password);
            } else {
              this.auth = response.user.authentication_token;
              sessionStorage.setItem(
                "auth-token",
                response.user.authentication_token
              );
              sessionStorage.setItem("email", this.email);
              this.$router.push("dashboard");
            }
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Can't login in: ", error);
      }
    },
  },
  // computed: {
  //   if (this.auth){
  //     this.authenticated = true;
  //   }
  // }
};
</script>

<style scoped></style>
