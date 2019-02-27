<template>
  <div>
    <v-container align-start fluid style="float: left">
      <v-layout>
        <v-flex>
          <dash-nav/>
        </v-flex>
        <v-flex>
          <router-view/>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import DashNav from "@/components/DashNav";

export default {
  name: "dashboard",
  components: {
    DashNav
  },
  data() {
    return {
      sheets: []
    };
  },
  beforeMount() {
    this.$store.dispatch("loadSheets");
    //console.log(this.$store.getters.getSheets);
  },
  mounted() {
    this.$router.push("/dashboard/view-sheets");
  }
};
</script>


<style scoped>
</style>