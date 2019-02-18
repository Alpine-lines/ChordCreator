<template>
  <nav class="navbar is-light" role="navigation" aria-label="main navigation">
    <div class="nav-menu">
      <div class="nav-start">
        <router-link to="/" class="navbar-item">Home</router-link>
        <router-link to="/new-chord" class="navbar-item">Create Chord</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navigation"
};
</script>

<style lang="scss">
@import "~bulma/bulma";
</style> 