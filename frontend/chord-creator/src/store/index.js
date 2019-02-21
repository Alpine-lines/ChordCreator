// src/store/index.js

import Vue from "vue";
import Vuex from "vuex";

import {
  fetchSheets,
  fetchSheet,
  createNewSheet,
  deleteSheet,
  fetchChord,
  createNewChord,
  updateChord,
  deleteChord,
  getInversion
} from "../api";

Vue.use(Vuex);

const state = {
  // single source of data
  sheets: [],
  currentSheet: {},
  currentChord: {},
  currentInversion: {}
};

const actions = {
  // asynchronous operations
  loadSheets(context) {
    return fetchSheets()
      .then(response => {
        //console.log(response)
        context.commit("setSheets", { sheets: response.data });
      })
      .catch(err => {
        console.log(err);
      });
  },
  loadSheet(context, { sheetId }) {
    return fetchSheet(sheetId)
      .then(response => {
        //console.log(response)
        context.commit("setSheet", { sheet: response.data });
      })
      .catch(err => {
        console.log(err);
      });
  },
  loadChord(context, { sheetId, chordId }) {
    return fetchChord(sheetId, chordId)
      .then(response => {
        //console.log(response)
        context.commit("setChord", { chord: response.data });
      })
      .catch(err => {
        console.log(err);
      });
  },
  loadInversion(context, { sheetId, chordId, inversionId }) {
    return fetchInversion(sheetId, chordId, inversionId)
      .then(response => {
        //console.log(response)
        context.commit("setInversion", { inversion: response.data });
      })
      .catch(err => {
        console.log(err);
      });
  },
  newSheet(context, { sheet }) {
    return createNewSheet(sheet)
      .then(response => {
        //console.log(response)
        context.dispatch("loadSheets");
        context.dispatch("loadSheet", response.data.id);
      })
      .catch(err => {
        console.log(err);
      });
  },
  deleteSheet(context, { sheetId }) {
    return deleteSheet(sheetId)
      .then(response => {
        //console.log(response)
        context.dispatch("loadSheets");
      })
      .catch(err => {
        console.log(err);
      });
  },
  newChord(context, { sheetId, chord }) {
    return createNewChord(sheetId, chord)
      .then(response => {
        //console.log(response)
        context.dispatch("loadSheets");
        context.dispatch("loadSheet", {
          sheetId: response.data.sheet_id
        });
        context.dispatch("loadChord", {
          sheetId: response.data.sheet_id,
          chordId: response.data.id
        });
      })
      .catch(err => {
        console.log(err);
      });
  },
  updateChord(context, { chordId, root }) {
    return alterChord(chordId, root)
      .then(response => {
        //console.log(response)
        context.dispatch("loadSheets");
        context.dispatch("loadSheet", {
          sheetId: response.data.sheet_id
        });
        context.dispatch("loadChord", {
          sheetId: response.data.sheet_id,
          chordId: response.data.id
        });
      })
      .catch(err => {
        console.log(err);
      });
  },
  deleteChord(context, { sheetId, chordId }) {
    return removeChord(sheetId, chordId)
      .then(response => {
        //console.log(response)
        context.dispatch("loadSheets");
        context.dispatch("loadSheet", {
          sheetId: response.data.sheet_id
        });
      })
      .catch(err => {
        console.log(err);
      });
  }
};

const mutations = {
  // isolated data mutations
  setSheets(state, payload) {
    state.sheets = payload.sheets;
  },
  setSheet(state, payload) {
    state.currentSheet = payload.sheet;
  },
  setChord(state, payload) {
    state.currentChord = payload.chord;
  },
  setInversion(state, payload) {
    state.currentInversion = payload.inversion;
  }
};

const getters = {
  // reusable data accessors
  getSheets: state => {
    return state.sheets;
  }
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
});

export default store;
