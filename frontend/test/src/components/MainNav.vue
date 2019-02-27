<template>
  <v-toolbar dark color="blue">
    <v-toolbar-title class="white--text">Chord Creator</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn icon to="/">
      <v-icon>home</v-icon>
    </v-btn>

    <v-btn icon to="/dashboard">
      <v-icon>apps</v-icon>
    </v-btn>

    <!--v-btn icon to="">
      <v-icon>refresh</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>more_vert</v-icon>
    </v-btn-->
  </v-toolbar>
</template>

<script>
export default {
  name: "main-nav",
  data() {
    return {
      sheets: []
    };
  }
};
</script>


<style scoped>
</style>