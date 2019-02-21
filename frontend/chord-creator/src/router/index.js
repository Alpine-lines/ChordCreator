import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home";
import Dashboard from "@/views/Dashboard";
import ViewSheets from "@/components/ViewSheets";
import ViewSheet from "@/components/ViewSheet";
import NewSheet from "@/components/NewSheet";
import NewChord from "@/components/NewChord";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/dashboard",
      name: "Dashboard",
      component: Dashboard,
      children: [
        {
          path: "view-sheets",
          name: "ViewSheets",
          component: ViewSheets
        },
        {
          path: "view-sheets/:id",
          name: "ViewSheet",
          component: ViewSheet
        },
        {
          path: "new-sheet",
          name: "NewSheet",
          component: NewSheet
        },
        {
          path: "new-chord",
          name: "NewChord",
          component: NewChord
        }
      ]
    }
  ],
  mode: "history"
});
