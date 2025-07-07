<script>
  export let apiKey;
  let recordId = '';
  let dataType = 'patient_record';
  let content = '';
  let status = '';
  let loading = false;
  let error = '';

  async function submitData() {
    loading = true;
    error = '';
    status = '';
    try {
      const res = await fetch('http://localhost:8000/health-data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-API-Key': apiKey
        },
        body: JSON.stringify({
          record_id: recordId,
          data_type: dataType,
          content: { raw: content }
        })
      });
      const data = await res.json();
      if (data.success) {
        status = `Stato: ${data.data.psn_integration}`;
      } else {
        error = data.message;
      }
    } catch (e) {
      error = 'Errore di connessione al backend';
    }
    loading = false;
  }
</script>

<div>
  <h3 class="font-semibold mb-2">Sanity Module</h3>
  <div class="mb-2">
    <input class="border rounded px-2 py-1 w-full mb-2" placeholder="Record ID" bind:value={recordId} />
    <select class="border rounded px-2 py-1 w-full mb-2" bind:value={dataType}>
      <option value="patient_record">Cartella clinica</option>
      <option value="billing">Fatturazione</option>
      <option value="lab_results">Referti laboratorio</option>
      <option value="prescriptions">Prescrizioni</option>
      <option value="administrative">Amministrativo</option>
    </select>
    <textarea class="border rounded px-2 py-1 w-full mb-2" placeholder="Contenuto dati (JSON o testo)" bind:value={content}></textarea>
    <button class="bg-blue-700 text-white px-3 py-1 rounded hover:bg-blue-800 transition w-full" on:click={submitData} disabled={loading}>
      {loading ? 'Invio...' : 'Invia Dati'}
    </button>
  </div>
  {#if status}
    <div class="text-green-700 text-sm mb-1">{status}</div>
  {/if}
  {#if error}
    <div class="text-red-600 text-sm">{error}</div>
  {/if}
</div> 