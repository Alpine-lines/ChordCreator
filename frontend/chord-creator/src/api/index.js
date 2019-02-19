import axios from "axios";

const API_URL = "http://127.0.0.1:5000/api";
// return axios.get(`{API_URL}/`)

export function fetchSheets() {
  return axios.get(`{API_URL}/sheets/`);
}

export function createNewSheet(sheet) {
  return axios.post((`{API_URL}/sheets/`, sheet));
}

export function fetchSheet(sheetId) {
  return axios.get(`{API_URL}/sheets/{sheetId}/`);
}

export function getChord(sheetId, chordId) {
  return axios.get(`{API_URL}/{sheetId}/{chordId}`);
}

export function addChord(chord) {
  return axios.put(`{API_URL}/sheets/{sheetId}`);
}

export function updateChord(sheetId, chordId, root) {
  return axios.put(`{API_URL}/{sheetId}/{chordId}/`, { root: root });
}

export function deleteChord(sheetId, chordId) {
  return axios.delete(`{API_URL}/{sheetId}/{chordId}/`);
}

export function getInversions(sheetId, chordId) {
  return axios.get(`API_URL/sheets/<int:sheetId>/<int:chordId>/inversions`);
}

export function deleteSheet(sheetId) {
  return axios.delete(`{API_URL}/sheets/{sheetId}/`);
}
