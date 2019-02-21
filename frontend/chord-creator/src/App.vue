<template>
  <div id="app">
    <navigation/>
    <router-view/>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation";
import Dashboard from "@/views/Dashboard";

export default {
  name: "App",
  components: {
    Navigation,
    Dashboard
  }
};
</script>

<style lang="scss">
@import "~bulma/bulma";
</style> 
 