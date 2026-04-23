self.addEventListener('install', (event) => {
  console.log('Service worker installed');
});

self.addEventListener('fetch', (event) => {
  // We'll add caching strategies here later.
  event.respondWith(fetch(event.request));
});
