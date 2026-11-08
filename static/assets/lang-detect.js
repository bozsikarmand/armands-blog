(function () {
  var lang = navigator.language || navigator.userLanguage;
  window.location.href = (lang && lang.toLowerCase().indexOf('hu') === 0) ? '/hu/' : '/en/';
})();
