(function () {
  document.querySelectorAll('.prev').forEach(function (b) {
    b.addEventListener('click', function () {
      var v = b.parentNode, f = document.createElement('iframe');
      f.title = 'Preview'; f.loading = 'lazy'; f.src = v.dataset.src;
      f.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-forms allow-popups');
      v.appendChild(f); b.remove();
    });
  });
  var th = document.getElementById('th');
  if (th) th.addEventListener('click', function () {
    var r = document.documentElement;
    var dark = r.dataset.theme === 'dark' || (!r.dataset.theme && matchMedia('(prefers-color-scheme:dark)').matches);
    var n = dark ? 'light' : 'dark'; r.dataset.theme = n;
    try { localStorage.setItem('th', n); } catch (e) {}
  });
  var a = document.getElementById('cm'), t = document.getElementById('cmt');
  if (a && t) {
    var m = ['calvfinka', 'yahoo.com'].join('@');
    a.href = 'mailto:' + m + '?subject=' + encodeURIComponent(a.dataset.sub || '');
    t.textContent = m;
  }
})();
