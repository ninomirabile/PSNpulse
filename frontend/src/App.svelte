<script>
  import Router, { link } from 'svelte-spa-router';
  import routes from './routes.js';
  let apiKey = localStorage.getItem('psn_api_key') || '';
  let showLogin = !apiKey;
  let showGuide = false;
  let loginInput;

  // Aggiorna apiKey su ogni cambio route/hashchange
  window.addEventListener('hashchange', () => {
    apiKey = localStorage.getItem('psn_api_key') || '';
  });

  function handleLogin(key) {
    apiKey = key;
    localStorage.setItem('psn_api_key', key);
    showLogin = false;
  }

  function handleLogout() {
    apiKey = '';
    localStorage.removeItem('psn_api_key');
    showLogin = true;
    showGuide = false;
    setTimeout(() => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
      if (loginInput) loginInput.focus();
      window.location.hash = '#/login';
    }, 100);
  }
</script>

<main class="min-h-screen bg-gray-50 text-gray-900">
  <header class="bg-blue-900 text-white p-4 flex items-center justify-between">
    <div class="flex items-center gap-4">
      <h1 class="text-xl font-bold tracking-wide">PSN Pulse</h1>
      <span class="text-xs italic hidden md:inline">Monitoraggio Migrazione Cloud PA</span>
    </div>
    <div class="flex items-center gap-4">
      <a href="/guida" use:link class="bg-blue-700 hover:bg-blue-800 px-3 py-1 rounded text-xs">Guida</a>
      {#if apiKey}
        <span class="text-xs">API Key: {apiKey}</span>
        <button class="bg-white text-blue-900 px-3 py-1 rounded text-xs ml-2 hover:bg-blue-100 border border-blue-200" on:click={handleLogout}>Logout</button>
      {/if}
    </div>
  </header>
  <section class="max-w-3xl mx-auto mt-6 mb-4 bg-white rounded shadow p-4">
    <h2 class="text-lg font-semibold mb-1">Cos'è questa dashboard?</h2>
    <p class="text-sm text-gray-700 mb-2">
      PSN Pulse ti aiuta a monitorare l'avanzamento della migrazione dei dati e dei sistemi della tua PA verso il cloud nazionale (PSN). Visualizza lo stato, le aree critiche, le milestone e i rischi di cybersecurity. Puoi anche inviare dati di test e simulare scenari.
    </p>
    <ul class="list-disc ml-6 text-xs text-gray-600">
      <li>Accedi con la tua API Key (per test: <b>psn-pulse-dev-2024</b>)</li>
      <li>Consulta la guida rapida in ogni momento dal bottone in alto</li>
      <li>Esci in ogni momento con il logout</li>
    </ul>
  </section>
  <Router {routes} />
</main> 