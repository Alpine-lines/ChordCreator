<template>
  <div>
    <div class="container">
      <dashboardNavigation/>
    </div>
    <router-view/>
  </div>
</template>

<script>
import DashboardNavigation from "@/components/DashboardNavigation";
import ViewSheets from "@/components/ViewSheets";
import NewSheet from "@/components/NewSheet";
import NewChord from "@/components/NewChord";

export default {
  name: "Dashboard",
  mounted() {
    this.openViewSheets();
  },
  components: {
    DashboardNavigation
  },
  methods: {
    openViewSheets: function() {
      this.$router.push({ path: "/dashboard/view-sheets" });
    }
  }
};
</script>

<style lang="scss">
@import "~bulma/bulma";
</style>  