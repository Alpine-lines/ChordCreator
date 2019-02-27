<template>
  <v-layout align-center justify-start column>
    <v-flex>
      <v-card style="width: 100%">
        <div class="container">
          <h2 class="title" style="color: #1976d2">View All Chord Sheets</h2>
          <v-spacer/>
        </div>
      </v-card>
    </v-flex>

    <v-flex>
      <v-card v-for="sheet in sheets" v-bind:key="sheet.id">
        <v-card-text class="text-xs-center">
          <p class="title" style="color: #1976d2">{{ sheet.name }}</p>
          <p
            class="subtitle"
            style="color: #1976d2"
          >Created On: {{ new Date(sheet.created_at).toDateString() }}</p>
          <v-btn outline class="justify-center" color="#1976d2">
            <router-link
              :to="`/dashboard/view-sheets/${sheet.id}`"
              class="card-footer-item"
              style="color: #1976d2"
            >View Chord Sheet {{ sheet.id }}</router-link>
          </v-btn>
        </v-card-text>
        <v-card-actions class="justify-center" color="#1976d2">
          <v-item-group align-start justify-start row>
            <v-item>
              <v-dialog v-model="editDialog">
                <v-btn fab outline color="#1976d2" slot="activator">
                  <v-icon color="#1976d2">edit</v-icon>
                </v-btn>
                <v-card>
                  <v-card-title>
                    <span class="headline">Edit Sheet</span>
                  </v-card-title>
                  <v-card-text>
                    <v-container grid-list-md>
                      <v-layout wrap column>
                        <v-flex xs12 sm6 md4>
                          <v-text-field label="Sheet Name:" required></v-text-field>
                        </v-flex>
                        <v-flex>
                          <v-btn outline color="#1976d2" @click="chordDialog = true">Add Chords</v-btn>
                        </v-flex>
                      </v-layout>
                    </v-container>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" flat @click="editDialog = false">Close</v-btn>
                    <v-btn color="blue darken-1" flat @click="updateSheet(sheet.id)">Save</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-item>
            <v-item>
              <v-dialog v-model="newDialog" scrollable max-width="400px">
                <v-btn fab outline color="#1976d2" slot="activator">
                  <v-icon color="#1976d2">add_circle</v-icon>
                </v-btn>
                <v-card>
                  <v-card-title>Create new Chord Sheet.</v-card-title>
                  <v-divider></v-divider>
                  <v-card-text style="height: 400px">
                    <v-container grid-list-md>
                      <v-layout wrap column>
                        <v-flex xs12 sm6 md4>
                          <v-text-field label="Sheet Name:" required v-model="newSheetName"></v-text-field>
                        </v-flex>
                        <v-flex></v-flex>
                      </v-layout>
                    </v-container>
                  </v-card-text>
                  <v-divider></v-divider>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" flat @click="newDialog = false">Close</v-btn>
                    <v-btn color="blue darken-1" flat @click="updateSheet(sheet.id)">Save</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-item>
            <v-item>
              <v-dialog v-model="deleteDialog">
                <v-btn fab outline color="#1976d2" slot="activator">
                  <v-icon color="#1976d2">remove_circle</v-icon>
                </v-btn>
                <v-card>
                  <v-card-title class="headline">Delete Chord Sheet</v-card-title>
                  <v-card-text>Deleting this chord sheet is permanent. Once this sheet has been deleted it cannot be recovered. Select 'DELETE' to delete or 'Cancel' to close this dialog.</v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="green darken-1" flat @click="deleteDialog = false">Cancel</v-btn>
                    <v-btn color="green darken-1" flat @click="deleteSheet(sheet.id)">DELETE</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-item>
          </v-item-group>
          <div>
            <v-dialog v-model="chordDialog">
              <v-card style="height:auto">
                <v-card-title>Dialog 2</v-card-title>
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
                <v-card-actions>
                  <v-btn color="primary" flat @click="dialog2=false">Close</v-btn>
                  <v-btn color="blue darken-1" flat @click="updateSheet(sheet.id)">Save</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>



<script>
import { mapState } from "vuex";

export default {
  name: "view-sheets",
  data() {
    return {
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
      newSheetName: "",
      editDialog: false,
      newDialog: false,
      dialogm1: "",
      deleteDialog: false,
      chordDialog: false
    };
  },
  methods: {
    updateSheet(sheetId) {
      console.log("update complete");
      this.editDialog = false;
      this.chordDialog = false;
    },
    newSheet(sheetId) {
      console.log("new sheet created");
      this.newDialog = false;
    },
    deleteSheet(sheetId) {
      console.log("delete complete");
      this.deleteDialog = false;
    }
  },
  computed: mapState({
    sheets: state => state.sheets.sheets
  })
};
</script>


<style lang="scss">
@import "~bulma/bulma";
</style>