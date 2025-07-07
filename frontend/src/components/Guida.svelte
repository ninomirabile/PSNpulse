<script>
  // Navigazione manuale per svelte-spa-router
  const exampleHealthPayload = `{
  "record_id": "rec-001",
  "data_type": "patient_record",
  "content": {
    "patient_name": "Mario Rossi",
    "dob": "1980-01-01",
    "diagnosis": "Ipertensione"
  },
  "patient_id": "pat-123",
  "facility_id": "osp-001"
}`;
  const exampleSecurityPayload = `GET /security-risks\nHeader: X-API-Key: psn-pulse-dev-2024`;
  const exampleInteropPayload = `POST /health-data\nHeader: X-API-Key: psn-pulse-dev-2024\nBody: { ... }`;
</script>

<div class="max-w-3xl mx-auto p-6">
  <h1 class="text-2xl font-bold mb-4 text-blue-900">Guida a PSN Pulse</h1>
  <p class="mb-4 text-gray-700">
    <b>PSN Pulse</b> è la dashboard pensata per dirigenti e responsabili sanitari che devono monitorare la migrazione dei dati clinici verso il cloud nazionale (PSN).
    Qui trovi una guida rapida all’uso, esempi pratici e risposte alle domande più frequenti.
  </p>

  <h2 class="text-lg font-semibold mt-6 mb-2">Cosa puoi fare con PSN Pulse?</h2>
  <ul class="list-disc ml-6 mb-4 text-gray-800">
    <li>Vedere a che punto sei con la migrazione delle cartelle cliniche</li>
    <li>Controllare lo stato di ogni modulo sanitario (anagrafe, referti, fascicolo, ecc.)</li>
    <li>Ricevere alert di sicurezza e consigli attuabili</li>
    <li>Monitorare le scadenze PNRR e le milestone</li>
    <li>Simulare scenari o inviare dati di test</li>
  </ul>

  <h2 class="text-lg font-semibold mt-6 mb-2">Esempi di payload/API</h2>
  <div class="mb-4">
    <b>Sanity Module (POST /health-data)</b>
    <pre class="bg-gray-50 border rounded p-2 overflow-x-auto text-xs">{exampleHealthPayload}</pre>
    <b>Cybersecurity Tracker (GET /security-risks)</b>
    <pre class="bg-gray-50 border rounded p-2 overflow-x-auto text-xs">{exampleSecurityPayload}</pre>
    <b>Interoperability Tool (POST /health-data)</b>
    <pre class="bg-gray-50 border rounded p-2 overflow-x-auto text-xs">{exampleInteropPayload}</pre>
  </div>

  <h2 class="text-lg font-semibold mt-6 mb-2">FAQ</h2>
  <ul class="list-disc ml-6 text-gray-800">
    <li><b>Chi alimenta i dati?</b> <br/>Nella demo sono mock, ma nella realtà possono essere caricati dagli operatori IT, fornitori cloud o tramite API automatiche.</li>
    <li><b>Posso integrare la dashboard nei sistemi esistenti?</b> <br/>Sì, è disponibile anche come Web Component.</li>
    <li><b>Come accedo?</b> <br/>Con una API Key fornita dall’amministratore (per test: <code>psn-pulse-dev-2024</code>).</li>
    <li><b>Posso simulare scenari?</b> <br/>Sì, puoi inviare dati di test e vedere come cambiano i grafici e gli alert.</li>
  </ul>

  <button class="mt-8 bg-blue-700 text-white px-4 py-2 rounded hover:bg-blue-800" on:click={() => window.location.hash = '#/dashboard'}>Torna alla dashboard</button>
</div> 