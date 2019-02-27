<template>
  <div>
    <v-layout align-start justify-start column xs12 sm5 md4>
      <v-flex>
        <v-card class="pa-3">
          <v-flex>
            <div>
              <h2 class="blue-text">View All Chord Sheets</h2>
            </div>
          </v-flex>
          <v-flex>
            <v-layout align-start justify-start row>
              <v-flex>
                <v-dialog v-model="newDialog" scrollable>
                  <v-btn icon slot="activator" @click>
                    <v-icon outline color="#1976d2">note_add</v-icon>
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
                      <v-btn color="blue darken-1" flat @click="newSheet()">Save</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-flex>
              <v-flex>
                <v-btn icon @click="active=true">
                  <v-icon outline color="#1976d2">apps</v-icon>
                </v-btn>
              </v-flex>
              <v-flex>
                <v-layout row justify-center>
                  <v-dialog
                    v-model="dialog"
                    fullscreen
                    hide-overlay
                    transition="dialog-bottom-transition"
                  >
                    <v-btn icon slot="activator" @click>
                      <v-icon outline color="#1976d2">settings</v-icon>
                    </v-btn>

                    <v-card>
                      <v-toolbar dark color="primary">
                        <v-btn icon dark @click="dialog = false">
                          <v-icon>close</v-icon>
                        </v-btn>
                        <v-toolbar-title>Settings</v-toolbar-title>
                        <v-spacer></v-spacer>
                        <v-toolbar-items>
                          <v-btn dark flat @click="dialog = false">Save</v-btn>
                        </v-toolbar-items>
                      </v-toolbar>
                      <v-list three-line subheader>
                        <v-subheader>User Controls</v-subheader>
                        <v-list-tile avatar>
                          <v-list-tile-content>
                            <v-list-tile-title>Content filtering</v-list-tile-title>
                            <v-list-tile-sub-title>Set the content filtering level to restrict apps that can be downloaded</v-list-tile-sub-title>
                          </v-list-tile-content>
                        </v-list-tile>
                        <v-list-tile avatar>
                          <v-list-tile-content>
                            <v-list-tile-title>Password</v-list-tile-title>
                            <v-list-tile-sub-title>Require password for purchase or use password to restrict purchase</v-list-tile-sub-title>
                          </v-list-tile-content>
                        </v-list-tile>
                      </v-list>
                      <v-divider></v-divider>
                      <v-list three-line subheader>
                        <v-subheader>General</v-subheader>
                        <v-list-tile avatar>
                          <v-list-tile-action>
                            <v-checkbox v-model="notifications"></v-checkbox>
                          </v-list-tile-action>
                          <v-list-tile-content>
                            <v-list-tile-title>Notifications</v-list-tile-title>
                            <v-list-tile-sub-title>Notify me about updates to apps or games that I downloaded</v-list-tile-sub-title>
                          </v-list-tile-content>
                        </v-list-tile>
                        <v-list-tile avatar>
                          <v-list-tile-action>
                            <v-checkbox v-model="sound"></v-checkbox>
                          </v-list-tile-action>
                          <v-list-tile-content>
                            <v-list-tile-title>Sound</v-list-tile-title>
                            <v-list-tile-sub-title>Auto-update apps at any time. Data charges may apply</v-list-tile-sub-title>
                          </v-list-tile-content>
                        </v-list-tile>
                        <v-list-tile avatar>
                          <v-list-tile-action>
                            <v-checkbox v-model="widgets"></v-checkbox>
                          </v-list-tile-action>
                          <v-list-tile-content>
                            <v-list-tile-title>Auto-add widgets</v-list-tile-title>
                            <v-list-tile-sub-title>Automatically add home screen widgets</v-list-tile-sub-title>
                          </v-list-tile-content>
                        </v-list-tile>
                      </v-list>
                    </v-card>
                  </v-dialog>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-flex>
        </v-card>
      </v-flex>
      <v-flex>
        <v-card>
          <ul>
            <li v-for="sheet in sheets" :key="sheet.id">
              <v-layout align-space-between justify-start column>
                <v-flex>
                  <v-btn
                    outline
                    color="#1976d2"
                    style="width:75%"
                    left
                    @click="toggleChords(sheet)"
                    :to="`/dashboard/view-sheets/${sheet.id}`"
                  >
                    <div>
                      <v-icon flat color="#1976d2" class="icon">music_note</v-icon>
                      {{ sheet.name }}
                    </div>
                  </v-btn>
                </v-flex>
                <v-flex>
                  <ul v-show="sheet.navIsOpen">
                    <li v-for="chord in sheet.chords" :key="chord.id">
                      <div>
                        <v-layout row>
                          <v-flex align-start>
                            <v-btn
                              flat
                              outline
                              class="chord-button"
                              color="#1976d2"
                              @click="toChord(chord.sheet_id)"
                            >
                              <v-icon flat color="#1976d2">queue_music</v-icon>
                              <div class="blue-text">{{ chord.name }}</div>
                            </v-btn>
                          </v-flex>
                        </v-layout>
                      </div>
                    </li>
                  </ul>
                </v-flex>
              </v-layout>
            </li>
          </ul>
        </v-card>
      </v-flex>
      <v-flex>
        <div class="text-xs-center">
          <v-bottom-sheet v-model="active">
            <v-list>
              <v-subheader>Open in</v-subheader>
              <v-list-tile v-for="tile in tiles" :key="tile.title" @click="bottomNav(tile.url)">
                <v-list-tile-avatar>
                  <v-avatar size="32px" tile>
                    <v-icon>{{ tile.icon }}</v-icon>
                  </v-avatar>
                </v-list-tile-avatar>
                <v-list-tile-title>{{ tile.title }}</v-list-tile-title>
              </v-list-tile>
            </v-list>
          </v-bottom-sheet>
        </div>
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
import { mapState } from "vuex";
import axios from "axios";
import { createNewSheet } from "@/api/index.js";

export default {
  methods: {
    toggleChords(sheet) {
      sheet.navIsOpen = !sheet.navIsOpen;
    },
    bottomNav(url) {
      this.$router.push(url);
    },
    toChord(chordId) {
      this.$router.push(`/dashboard/view-chords/${chordId}`);
    },
    newSheet() {
      const newSheet = {
        name: this.newSheetName,
        chords: []
      };
      axios.post("http://localhost:5000/api/sheets/", newSheet);
      console.log(newSheet);
      this.newDialog = false;
    }
  },
  data: () => ({
    open: ["public"],
    tree: [],
    active: false,
    tiles: [
      {
        title: "New Chord Sheet",
        icon: "create_new_folder",
        url: "/dashboard/new-sheet"
      },
      {
        title: "Play Chords",
        icon: "play_arrow",
        url: "/play-chord"
      },
      {
        title: "Delete Chord Sheet",
        icon: "remove_circle",
        url: "/dashboard/manage-sheet/"
      }
    ],
    dialog: false,
    newDialog: false,
    notifications: false,
    sound: true,
    widgets: false,
    newSheetName: "",
    newSheetChords: [
      {
        name: "A"
      },
      {
        name: "B"
      }
    ]
  }),
  computed: mapState({
    sheets: state => state.sheets.sheets,
    currentSheet: state => state.currentSheet,
    sheet: "currentSheet"
  })
};
</script>


<style>
.sheet-button {
  width: 60%;
  padding: 2.5%;
}
.icon {
  float: left;
  color: #1976d2;
}
.blue-text {
  color: #1976d2;
  text-transform: initial;
}
.chord-button {
  width: 60%;
  padding: 0.5%;
  color: #1976d2;
}
.crud-button {
  padding: 5%;
}
</style>
