import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home";
import NewChord from "@/views/NewChord";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/new-chord",
      name: "New Chord",
      component: NewChord
    }
  ]
});
