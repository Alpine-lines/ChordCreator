<template>
  <v-container fluid class="pa-0">
    <v-layout fill-height column>
      <v-flex justify-center>
        <!--v-card>
          <div class="container has-text-left">
            <h2 class="title" style="color: #1976d2"></h2>
          </div>
        </v-card-->
      </v-flex>
      <v-flex justify-center>
        <div
          v-for="(chord, idx) in currentSheet.sheet.chords"
          v-bind:key="chord.id"
          v-show="currentChord === idx"
        >
          <v-card>
            <v-toolbar color="white">
              <v-toolbar-title>
                <v-btn outline color="#1976d2" @click.stop="goToPrevious">
                  <v-icon>navigate_before</v-icon>
                </v-btn>
                <v-btn outline color="#1976d2" @click.stop="goToNext">
                  <v-icon>navigate_next</v-icon>
                </v-btn>
              </v-toolbar-title>
              <v-spacer/>
              <v-spacer/>
              <h4 class="title has-text-centered" style="color: black">
                <br>
                {{ currentSheet.sheet.name }}: {{ chord.name }}
              </h4>
              <v-spacer/>
              <v-item-group>
                <v-item>
                  <v-dialog v-model="newDialog">
                    <v-btn fab outline color="#1976d2" slot="activator">
                      <v-icon color="#1976d2">add_circle_outline</v-icon>
                    </v-btn>
                    <v-card>
                      <v-card-title>Create new Chord.</v-card-title>
                      <v-divider></v-divider>
                      <v-card-text>
                        <v-select
                          :items="shorthand_meaning"
                          label="All Chords"
                          dense
                          scrollable
                          attach
                          item-value="name"
                        ></v-select>
                      </v-card-text>
                      <v-divider></v-divider>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" flat @click="newDialog = false">Close</v-btn>
                        <v-btn color="blue darken-1" flat @click="newChord()">Save</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-item>
                <v-item>
                  <v-dialog v-model="editDialog">
                    <v-btn fab outline color="#1976d2" slot="activator">
                      <v-icon color="#1976d2">edit</v-icon>
                    </v-btn>
                    <v-card>
                      <v-card-title>Update Chord.</v-card-title>
                      <v-divider></v-divider>
                      <v-card-text>
                        <v-select
                          :items="shorthand_meaning"
                          label="Chords"
                          dense
                          scrollable
                          attach
                          item-value="name"
                        ></v-select>
                      </v-card-text>
                      <v-divider></v-divider>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" flat @click="editDialog = false">Close</v-btn>
                        <v-btn
                          color="blue darken-1"
                          flat
                          @click="updateChord(chord.sheet_id, chord.id)"
                        >Save</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-item>
                <v-item>
                  <v-dialog v-model="deleteDialog">
                    <v-btn fab outline color="#1976d2" slot="activator">
                      <v-icon color="#1976d2">clear</v-icon>
                    </v-btn>
                    <v-card>
                      <v-card-title class="headline">Delete Chord Sheet</v-card-title>
                      <v-card-text>Deleting this chord sheet is permanent. Once this sheet has been deleted it cannot be recovered. Select 'DELETE' to delete or 'Cancel' to close this dialog.</v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="green darken-1" flat @click="deleteDialog = false">Cancel</v-btn>
                        <v-btn
                          color="green darken-1"
                          flat
                          @click="deleteChord(chord.sheet_id, chord.id)"
                        >DELETE</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-item>
              </v-item-group>
            </v-toolbar>
            <v-container>
              <div class="container has-text-centered">
                <h2 class="title" style="color: black">Notes: {{ chord.notes }}</h2>
                <h5 style="color: black">Inversions:</h5>
                <ul v-for="inversion in chord.inversions" v-bind:key="inversion.id">
                  <li style="color: black">{{ parseInt(inversion.name)+1 }}: {{ inversion.notes }}</li>
                </ul>
                <v-img
                  :src="require('../assets/example.jpg')"
                  position="center center"
                  style="height:350px"
                  contain
                ></v-img>
              </div>
            </v-container>
          </v-card>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      currentChord: 0,
      shorthand_meaning: [
        "m",
        "M",
        "",
        "dim",
        "aug",
        "+",
        "7#5",
        "M7+5",
        "M7+",
        "m7+",
        "7+",
        "sus47",
        "sus4",
        "sus2",
        "sus",
        "11",
        "sus4b9",
        "susb9",
        "m7",
        "M7",
        "dom7",
        "7",
        "m7b5",
        "dim7",
        "m/M7",
        "mM7",
        "m6",
        "M6",
        "6",
        "6/7",
        "67",
        "6/9",
        "69",
        "9",
        "7b9",
        "7#9",
        "M9",
        "m9",
        "7#11",
        "m11",
        "M13",
        "m13",
        "13",
        "7b5",
        "hendrix",
        "7b12",
        "5"
      ],
      deleteDialog: false,
      editDialog: false,
      newDialog: false
    };
  },
  computed: mapState({
    sheets: state => state.sheets.sheets,
    currentSheet: state => state.currentSheet,
    sheet: "currentSheet"
  }),
  beforeMount: function() {
    this.$store.dispatch("loadSheet", {
      sheetId: parseInt(this.$route.params.id)
    });
    console.log(this.$store.getters.getCurrentSheet);
  },
  mounted() {
    console.log(this.currentSheet);
  },
  methods: {
    goToNext: function() {
      if (this.currentChord === this.currentSheet.sheet.chords.length - 1) {
        this.currentChord = 0;
      } else {
        this.currentChord++;
      }
    },
    goToPrevious: function() {
      if (this.currentChord === 0) {
        this.currentChord = this.currentSheet.sheet.chords.length - 1;
      } else {
        this.currentChord--;
      }
    },
    deleteChord(sheetId, chordId) {},
    updateChord(sheetId, chordId) {},
    newChord(chord) {}
  }
};
</script>
<style>
.blue {
  text-decoration-color: #1976d2;
}
.sheet-music {
  height: 20%;
  width: 20%;
}
</style>
 