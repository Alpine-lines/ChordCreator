<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">{{ sheets[0].name }}</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-10 is-offset-1">
            <div
              v-for="(chord, idx) in sheets[0].chords"
              v-bind:key="chord.id"
              v-show="currentChord === idx"
            >
              <!-- new v-show directive -->
              <div class="column is-offset-3 is-6">
                <!-- <h4 class='title'>{{ idx }}) {{ question.text }}</h4> -->
                <h4 class="title has-text-centered">Name: {{ chord.name }}</h4>
                <h2 class="title has-text-centered">Notes: {{ chord.notes }}</h2>
              </div>
              <div class="column is-offset-4 is-4">
                <div class="control">
                  <div>
                    <ul v-for="inversion in chord.inversions" v-bind:key="inversion.id">
                      <li>{{ inversion.name }}: {{ inversion.notes }}</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- new pagination buttons -->
            <div class="column is-offset-one-quarter is-half">
              <nav class="pagination is-centered" role="navigation" aria-label="pagination">
                <a class="pagination-previous" @click.stop="goToPrevious">
                  <i class="fa fa-chevron-left" aria-hidden="true"></i> &nbsp;&nbsp; Back
                </a>
                <a class="pagination-next" @click.stop="goToNext">
                  Next &nbsp;&nbsp;
                  <i class="fa fa-chevron-right" aria-hidden="true"></i>
                </a>
              </nav>
            </div>

            <!-- new submit button >
            <div class="column has-text-centered">
              <a
                v-if="sheets[0]Complete"
                class="button is-focused is-primary is-large"
                @click.stop="this.$route.push('/')"
              >Exit</a>
            </div-->
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      currentChord: 0
    };
  },
  computed: mapState({
    sheets: state => state.sheets.sheets
  }),
  sheetId() {
    this.$route.params.id;
  },
  beforeMount: function() {
    this.$store.dispatch("loadSheet", {
      sheetId: parseInt(this.$route.params.id)
    });
  },
  methods: {
    goToNext: function() {
      if (this.currentChord === this.sheets[0].chords.length - 1) {
        this.currentChord = 0;
      } else {
        this.currentChord++;
      }
    },
    goToPrevious: function() {
      if (this.currentChord === 0) {
        this.currentChord = this.sheets[0].chords.lenth - 1;
      } else {
        this.currentChord--;
      }
    }
  }
};
</script>

<style lang="scss">
@import "~bulma/bulma";
</style> 