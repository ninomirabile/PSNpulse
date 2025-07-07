<script>
  let apiKey = '';
  let error = '';

  function handleLogin() {
    if (!apiKey.trim()) {
      error = 'Inserisci una API Key valida';
      return;
    }
    localStorage.setItem('psn_api_key', apiKey.trim());
    window.location.hash = '#/dashboard';
  }
</script>

<div class="flex flex-col items-center justify-center h-[70vh]">
  <div class="bg-white shadow rounded p-6 w-full max-w-sm">
    <h2 class="text-lg font-semibold mb-2">Login Admin</h2>
    <input type="text" placeholder="Inserisci API Key" bind:value={apiKey} class="border rounded px-3 py-2 mb-4 w-full" />
    <button class="bg-blue-700 text-white px-4 py-2 rounded hover:bg-blue-800 transition w-full" on:click={handleLogin}>Accedi</button>
    {#if error}
      <div class="text-red-600 text-xs mt-2">{error}</div>
    {/if}
    <div class="text-xs text-gray-500 mt-4">API Key di test: <b>psn-pulse-dev-2024</b></div>
  </div>
</div> 