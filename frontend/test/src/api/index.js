import axios from "axios";

const API_URL = "http://127.0.0.1:5000/api";
// return axios.get(`{API_URL}/`)

export function fetchSheets() {
  return axios.get(`${API_URL}/sheets/`);
}

export function createNewSheet(sheet) {
  return axios.post((`localhost:5000/api/sheets/`, sheet));
}

export function fetchSheet(sheetId) {
  return axios.get(`${API_URL}/sheets/${sheetId}/`);
}

export function fetchChord(sheetId, chordId) {
  return axios.get(`${API_URL}/${sheetId}/${chordId}`);
}

export function createNewChord(sheetId, chord) {
  return axios.put(`${API_URL}/sheets/${sheetId}`, chord);
}

export function alterChord(sheetId, chordId, root) {
  return axios.put(`${API_URL}/${sheetId}/${chordId}/`, root);
}

export function removeChord(sheetId, chordId) {
  return axios.delete(`${API_URL}/${sheetId}/${chordId}/`);
}

export function getInversion(sheetId, chordId, inversionId) {
  return axios.get(`${API_URL}/sheets/${sheetId}/${chordId}/${inversionId}`);
}

export function deleteSheet(sheetId) {
  return axios.delete(`${API_URL}/sheets/${sheetId}/`);
}
