<<<<<<< HEAD
// Extensão "Rap de Anime e Mangá" para FreeBeat
const PLAYLIST_URL = 'https://raw.githubusercontent.com/escritor3/eloisa/main/playlist.json';

module.exports = {
  id: 'music_eloisa_repo',
  name: 'Música Eloisa',
  version: '1.0.0',
  hasCatalog: true,

  async getCatalog(api) {
    const data = await api.httpGetJson(PLAYLIST_URL);
    return api.normalizeSongs(data);
  },

  async search(query, api) {
    const data = await api.httpGetJson(PLAYLIST_URL);
    const songs = api.normalizeSongs(data);
    const q = query.toLowerCase();
    return songs.filter(
      (s) =>
        s.titulo.toLowerCase().includes(q) ||
        (s.artista && s.artista.toLowerCase().includes(q)) ||
        (s.genero && s.genero.toLowerCase().includes(q))
    );
  },
=======
// Extensão "Rap de Anime e Mangá" para FreeBeat
const PLAYLIST_URL = 'https://raw.githubusercontent.com/escritor3/eloisa/main/playlist.json';

module.exports = {
  id: 'music_eloisa_repo',
  name: 'Música Eloisa',
  version: '1.0.0',
  hasCatalog: true,

  async getCatalog(api) {
    const data = await api.httpGetJson(PLAYLIST_URL);
    return api.normalizeSongs(data);
  },

  async search(query, api) {
    const data = await api.httpGetJson(PLAYLIST_URL);
    const songs = api.normalizeSongs(data);
    const q = query.toLowerCase();
    return songs.filter(
      (s) =>
        s.titulo.toLowerCase().includes(q) ||
        (s.artista && s.artista.toLowerCase().includes(q)) ||
        (s.genero && s.genero.toLowerCase().includes(q))
    );
  },
>>>>>>> 65d9ef299eeee0af66ae220be5d49bf1a1fc4c0a
};