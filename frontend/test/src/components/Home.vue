<template>
  <v-content>
    <section>
      <v-parallax src="@/assets/hero.jpeg" height="600">
        <v-layout column align-center justify-center class="white--text">
          <img class="center" :src="require('@/assets/vuetify.png')">
          <v-btn class="blue lighten-2 mt-5" dark large to="/dashboard">Get Started</v-btn>
        </v-layout>
      </v-parallax>
    </section>

    <section>
      <v-layout column wrap align-center>
        <v-flex xs12 sm4>
          <div class="text-xs-center">
            <h2
              class="headline"
            >Chord Creator allows you to generate Chord objects which can be stored in Sheets.</h2>
            <span class="subheading">Chord sheets include multiple inversions and sheet music.</span>
          </div>
        </v-flex>
        <v-flex xs12>
          <v-container grid-list-xl>
            <v-layout row wrap align-center>
              <v-flex xs12 md4>
                <v-card class="elevation-0 transparent">
                  <v-card-text class="text-xs-center">
                    <v-icon x-large class="blue--text text--lighten-2">build</v-icon>
                  </v-card-text>
                  <v-card-title primary-title class="layout justify-center">
                    <div class="headline text-xs-center">Full-Stack Engineering</div>
                  </v-card-title>
                  <v-card-text>
                    Chord Creator is a simple web application built using Vue.js and Python's Flask micro-framework.
                    The Full Stack web app architecture allows us to generate data on a server and store it in a
                    database. We can then access this data on the frontend using a graphical user interface.
                  </v-card-text>
                  <v-card-actions>
                    <v-btn
                      outline
                      color
                      to="https://github.com/Alpine-lines/ChordCreator"
                    >View Source</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
              <v-flex xs12 md4>
                <v-card class="elevation-0 transparent">
                  <v-card-text class="text-xs-center">
                    <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                  </v-card-text>
                  <v-card-title primary-title class="layout justify-center">
                    <div class="headline">Flask Backend</div>
                  </v-card-title>
                  <v-card-text>
                    The REST API includes GET, POST, PUT, and DELETE requests for Chord objects and the Sheets that hold them. Every endpoint is
                    accesible via the frontend GUI. When users make POST requests to generate new chords, sheet music files are generated
                    and stored on the server. A reference to theses images is then stored in the database so that the images can be pulled from
                    the server.
                  </v-card-text>
                  <v-card-actions>
                    <v-btn
                      outline
                      color
                      to="https://github.com/Alpine-lines/ChordCreator"
                    >View Source</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
              <v-flex xs12 md4>
                <v-card class="elevation-0 transparent">
                  <v-card-text class="text-xs-center">
                    <v-icon x-large class="blue--text text--lighten-2">color_lens</v-icon>
                  </v-card-text>
                  <v-card-title primary-title class="layout justify-center">
                    <div class="headline text-xs-center">Vue.js Frontend</div>
                  </v-card-title>
                  <v-card-text>
                    The Vue.js frontend from this application was built using the vue router, the vuex state management system, axios, and vuetify.
                    The vuex state management system allows us to dyanamically manage application state in real-time, updating only the parts of
                    the page the have actually changed.
                  </v-card-text>
                  <v-card-actions>
                    <v-btn
                      outline
                      color
                      to="https://github.com/Alpine-lines/ChordCreator"
                    >View Source</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </section>

    <section>
      <v-container grid-list-xl>
        <v-layout row wrap justify-center class="my-5">
          <v-flex xs12 sm4>
            <v-card class="elevation-0 transparent">
              <v-card-title primary-title class="layout justify-center">
                <div class="headline">Company info</div>
              </v-card-title>
              <v-card-text>Alpine Lines Llc. is a Full Stack Web Development Consultancy Agency focused on the application of data science and Machine Learning</v-card-text>
            </v-card>
          </v-flex>
          <v-flex xs12 sm4 offset-sm1>
            <v-card class="elevation-0 transparent">
              <v-card-title primary-title class="layout justify-center">
                <div class="headline">Contact us</div>
              </v-card-title>
              <v-card-text>Contact us for help on your next big JavaScript or Python Project.</v-card-text>
              <v-list class="transparent">
                <v-list-tile>
                  <v-list-tile-action>
                    <v-icon class="blue--text text--lighten-2">phone</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>720-339-9400</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-action>
                    <v-icon class="blue--text text--lighten-2">place</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>Boulder, CO. USA</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-action>
                    <v-icon class="blue--text text--lighten-2">email</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>alpinelines.llc@gmail.com</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </v-list>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </section>

    <v-footer class="blue darken-2">
      <v-layout row wrap align-center>
        <v-flex xs12>
          <div class="white--text ml-3"></div>
        </v-flex>
      </v-layout>
    </v-footer>
  </v-content>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "home",
  computed: mapState({
    sheets: state => state.sheets.sheets
  }),
  data() {
    return {
      images: {
        example: require("@/assets/example.jpg")
      },
      title: "Your Logo"
    };
  }
};
</script>


<style scoped>
</style>
