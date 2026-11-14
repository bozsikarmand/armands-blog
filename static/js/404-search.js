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
        // Fuse 3.x: ignoreLocation helyett
        distance: 100000,
      });
      if (input.value.trim()) update();
    })
    .catch(function () {});

  input.addEventListener('input', function () {
    menu.textContent = '';
    var q = input.value.trim();
    if (!q || !fuse) { box.hidden = true; return; }
    var results = fuse.search(q).slice(0, 8);
    if (!results.length) { box.hidden = true; return; }
    var hint = document.createElement('div');
    hint.className = 'au-search__hint';
    hint.innerHTML = '<span><b>&uarr;&darr;</b> navigálás</span><span><b>&crarr;</b> nyitás</span><span><b>esc</b> bezárás</span>';
    menu.appendChild(hint);
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

  input.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { box.hidden = true; input.blur(); return; }
    if (box.hidden) return;
    var items = menu.querySelectorAll('.result-item');
    if (!items.length) return;
    var idx = Array.prototype.indexOf.call(items, menu.querySelector('.result-item.is-active'));
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      if (idx >= 0) items[idx].classList.remove('is-active');
      idx = e.key === 'ArrowDown'
        ? (idx + 1) % items.length
        : (idx <= 0 ? items.length - 1 : idx - 1);
      items[idx].classList.add('is-active');
      items[idx].scrollIntoView({ block: 'nearest' });
    } else if ((e.key === 'Enter' || e.key === 'NumpadEnter') && idx >= 0) {
      e.preventDefault();
      items[idx].click();
    }
  });
})();
