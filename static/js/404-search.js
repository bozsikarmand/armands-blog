// 404-oldali kereső: a nyelvi searchindex.json-ben keres (Fuse.js),
// találatokra kattintva az adott oldalra ugrik.
(function () {
  var input = document.getElementById('search-404');
  var menu = document.getElementById('search-404-results');
  var box = document.getElementById('search-404-box');
  if (!input || !menu || !box || typeof Fuse === 'undefined') return;

  var indexUrl = box.getAttribute('data-index');
  var fuse = null;

  fetch(indexUrl)
    .then(function (r) { return r.json(); })
    .then(function (data) {
      fuse = new Fuse(data, {
        keys: ['title', 'content'],
        threshold: 0.4,
        ignoreLocation: true,
      });
    })
    .catch(function () {});

  input.addEventListener('input', function () {
    menu.textContent = '';
    var q = input.value.trim();
    if (!q || !fuse) { box.hidden = true; return; }
    var results = fuse.search(q).slice(0, 8);
    if (!results.length) { box.hidden = true; return; }
    results.forEach(function (r) {
      // Fuse >= 6: {item: {...}}; régebbi: maga az elem
      var item = r.item ? r.item : r;
      if (!item || !item.uri) return;
      var a = document.createElement('a');
      a.href = item.uri;
      a.textContent = item.title;
      a.className = 'result-item';
      menu.appendChild(a);
    });
    box.hidden = false;
  });

  document.addEventListener('click', function (e) {
    if (!box.contains(e.target) && e.target !== input) box.hidden = true;
  });
})();
