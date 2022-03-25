import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import UserDashboard from "../views/UserDashboard.vue";
import CreateDeck from "../views/CreateDeck.vue";
import AddCards from "../views/AddCards.vue";
import EditDeck from "../views/EditDeck.vue";
import EditCards from "../views/EditCards.vue";
import DeckQuiz from "../views/DeckQuiz.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/login",
    name: "UserLogin",
    component: Login,
  },
  {
    path: "/register",
    name: "UserRegister",
    component: Register,
  },
  {
    path: "/dashboard",
    name: "UserDashboard",
    component: UserDashboard,
  },
  {
    path: "/createDeck",
    name: "createDeck",
    component: CreateDeck,
  },
  {
    path: "/addCards",
    name: "AddCards",
    component: AddCards,
  },
  {
    path: "/dashboard/deck/:deck_name/edit",
    name: "EditDeck",
    component: EditDeck,
  },
  {
    path: "/dashboard/deck/:deck_name/edit/cards",
    name: "EditCards",
    component: EditCards,
  },
  {
    path: "/dashboard/deck/:deck_name/quiz",
    name: "DeckQuiz",
    component: DeckQuiz,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
