<script>
  export let apiKey;
  import { onMount } from 'svelte';
  let risk = null;
  let loading = true;
  let error = '';

  onMount(async () => {
    loading = true;
    try {
      const res = await fetch('http://localhost:8000/security-risks', {
        headers: { 'X-API-Key': apiKey }
      });
      const data = await res.json();
      if (data.success) {
        risk = data.data;
      } else {
        error = data.message;
      }
    } catch (e) {
      error = 'Errore di connessione al backend';
    }
    loading = false;
  });
</script>

<div>
  <h3 class="font-semibold mb-2">Cybersecurity Tracker</h3>
  {#if loading}
    <div class="text-gray-500">Caricamento rischi...</div>
  {:else if error}
    <div class="text-red-600">{error}</div>
  {:else}
    <div class="mb-2">
      <span class="font-bold">Livello rischio:</span> <span class="capitalize">{risk.risk_level}</span>
    </div>
    <div class="mb-2">
      <span class="font-bold">Suggerimenti:</span>
      <ul class="list-disc ml-5 text-sm">
        {#each risk?.tips ?? [] as tip}
          <li>{tip}</li>
        {/each}
      </ul>
    </div>
    <div>
      <span class="font-bold">Vulnerabilità:</span>
      <ul class="list-disc ml-5 text-sm">
        {#each risk?.vulnerabilities ?? [] as v}
          <li>{v.type} ({v.severity}) - {v.status}</li>
        {/each}
      </ul>
    </div>
  {/if}
</div> 