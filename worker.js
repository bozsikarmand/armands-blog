// Egységes 404-kezelés: nyelv az útvonalból (/en/*, /hu/*) vagy Accept-Language
// fejlécből (root útvonalak). A tematikus, keresős /{lang}/404.html szolgál ki
// 404-es státusszal – redirect és kétnyelvű villanás nélkül, pixelre ugyanaz,
// mint amit a nyelvi útvonalak kapnak.

// Nyelvenkénti 404 útvonalak (a CV-n az angol a gyökérben él)
const NOT_FOUND_PAGES = {
  en: '/en/404.html',
  hu: '/hu/404.html',
};

export default {
  async fetch(request, env) {
    const res = await env.ASSETS.fetch(request);
    if (res.status !== 404) return res;

    const url = new URL(request.url);
    const path = url.pathname;

    let lang = null;
    if (path.startsWith('/hu/') || path === '/hu') lang = 'hu';
    else if (path.startsWith('/en/') || path === '/en') lang = 'en';
    else {
      // Root szintű ismeretlen útvonal: a böngésző nyelvi beállítása dönt
      const accept = (request.headers.get('Accept-Language') || '').toLowerCase();
      lang = accept.startsWith('hu') ? 'hu' : 'en';
    }

    const themed = await env.ASSETS.fetch(new Request(new URL(NOT_FOUND_PAGES[lang], url), request));
    if (themed.status !== 200) return res; // biztonsági visszaesés
    return new Response(themed.body, { status: 404, headers: themed.headers });
  },
};
