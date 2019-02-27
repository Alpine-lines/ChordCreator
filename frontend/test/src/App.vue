<template>
  <div id="app">
    <main-nav/>
    <router-view/>
  </div>
</template>

<script>
import MainNav from "@/components/MainNav";

export default {
  name: "App",
  components: {
    MainNav
  },
  data() {
    return {
      sheets: []
    };
  }
};
</script>

<style>
</style>
