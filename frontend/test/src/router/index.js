import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "",
      name: "_home",
      component: () => import("@/components/Home")
    },
    {
      path: "/",
      name: "home",
      component: () => import("@/components/Home")
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: () => import("@/components/Dashboard"),
      children: [
        {
          path: "view-sheets",
          name: "view-sheets",
          component: () => import("@/components/ViewSheets")
        },
        {
          path: "view-sheets/:id",
          name: "view-sheet",
          component: () => import("@/components/ViewSheet")
          /*children: [
            {
              path: "add-chord",
              name: "add-chord",
              component: () => import("@/components/ViewSheet")
            },
            {
              path: "update_chord/:chordId",
              name: "update_chord",
              component: () => import("@/components/ViewSheet")
            },
            {
              path: "play-chord/:chordId",
              name: "play-chord",
              component: () => import("@/components/ViewSheet")
            }
          ]*/
        },
        {
          path: "view-chords/:id",
          name: "view-chords",
          component: () => import("@/components/ViewChords")
        }
      ]
    },
    {
      path: "*",
      redirect: () => import("@/components/Home")
    }
  ]
});
