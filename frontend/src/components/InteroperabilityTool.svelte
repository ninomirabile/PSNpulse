<script>
  export let apiKey;
</script>

<div>
  <h3 class="font-semibold mb-2">Interoperability Tool</h3>
  <div class="mb-2 text-sm">
    <b>Guida integrazione sistemi legacy:</b>
    <ol class="list-decimal ml-5">
      <li>Consulta la <a href="http://localhost:8000/docs" target="_blank" class="text-blue-700 underline">documentazione API PSN</a>.</li>
      <li>Configura endpoint REST per l'invio dati.</li>
      <li>Utilizza la chiave API fornita per autenticare le richieste.</li>
      <li>Testa l'integrazione con i dati mock disponibili.</li>
      <li>Contatta il supporto PSN per casi avanzati.</li>
    </ol>
  </div>
  <div class="bg-gray-100 rounded p-2 text-xs">
    <b>Endpoint mock:</b> <br />
    <code>POST http://localhost:8000/health-data</code>
  </div>
</div> 