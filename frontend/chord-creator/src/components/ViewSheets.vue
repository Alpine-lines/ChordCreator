<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">View All Chord Sheets!</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="card" v-for="sheet in sheets" v-bind:key="sheet.id">
          <div class="card-content">
            <p class="title">{{ sheet.name}}</p>
            <p class="subtitle">{{ new Date(sheet.created_at).toDateString() }}</p>
          </div>
          <div>
            <router-link
              :to="`/dashboard/view-sheets/${sheet.id}`"
              class="card-footer-item"
            >View Chord Sheet {{ sheet.id }}</router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: mapState({
    sheets: state => state.sheets.sheets
  }),
  beforeMount() {
    this.$store.dispatch("loadSheets");
    console.log(this.$store.getters.getSheets);
  }
};
</script>

<style lang="scss">
@import "~bulma/bulma";
</style>   