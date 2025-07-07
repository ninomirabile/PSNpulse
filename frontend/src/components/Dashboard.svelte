<script>
  import { onMount, tick } from 'svelte';
  import { SanityModule, CybersecurityTracker, InteroperabilityTool } from './index.js';
  import Chart from 'chart.js/auto';

  let apiKey = '';
  export let showGuide;
  let migrationStatus = null;
  let loading = true;
  let error = '';

  // Tooltip per aree critiche
  let tooltip = '';
  let tooltipX = 0;
  let tooltipY = 0;
  let showTooltip = false;

  // Chart refs
  let barChartRef;
  let pieChartRef;
  let timelineChartRef;
  let barChart, pieChart, timelineChart;

  const areaDescriptions = {
    "Fascicolo Sanitario Elettronico": "Digitalizzazione e migrazione fascicoli clinici.",
    "Integrazione Referti Digitali": "Referti laboratori e radiologia integrati nel cloud.",
    "Interoperabilità Sistemi Legacy": "Connessione tra sistemi storici e cloud.",
    "Gestione Consensi Pazienti": "Gestione digitale dei consensi privacy e GDPR.",
    "Backup e Disaster Recovery": "Implementazione procedure di backup e ripristino."
  };

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

  function handleHideGuide() {
    showGuide = false;
  }

  function showAreaTooltip(area, event) {
    tooltip = areaDescriptions[area] || area;
    tooltipX = event.clientX;
    tooltipY = event.clientY;
    showTooltip = true;
  }
  function hideAreaTooltip() {
    showTooltip = false;
  }

  // Nuova funzione per controllare autenticazione e fetch dati
  async function checkAuthAndFetch() {
    apiKey = localStorage.getItem('psn_api_key') || '';
    if (!apiKey) {
      window.location.hash = '#/login';
      return;
    }
    await loadData();
  }

  onMount(() => {
    apiKey = localStorage.getItem('psn_api_key') || '';
    if (!apiKey) {
      window.location.hash = '#/login';
      return;
    }
    checkAuthAndFetch();
    window.addEventListener('hashchange', () => {
      apiKey = localStorage.getItem('psn_api_key') || '';
      if (!apiKey) {
        window.location.hash = '#/login';
        return;
      }
      checkAuthAndFetch();
    });
    return () => window.removeEventListener('hashchange', checkAuthAndFetch);
  });

  async function loadData() {
    loading = true;
    error = '';
    try {
      const res = await fetch('http://localhost:8000/migration-status', {
        headers: { 'X-API-Key': apiKey }
      });
      const data = await res.json();
      if (res.ok) {
        migrationStatus = data.data || data;
        await tick();
      } else {
        error = data.message || 'Errore di connessione al backend';
      }
    } catch (e) {
      error = 'Errore di connessione al backend';
    }
    loading = false;
  }

  // Reactive statement: chiama renderCharts solo quando tutto è pronto
  $: if (migrationStatus && barChartRef && pieChartRef && timelineChartRef) {
    renderCharts();
  }

  function renderCharts() {
    if (!barChartRef || !pieChartRef || !timelineChartRef) {
      console.log('DEBUG: uno dei canvas ref non è pronto', { barChartRef, pieChartRef, timelineChartRef });
      return;
    }
    console.log('DEBUG migrationStatus:', migrationStatus);
    const completed = (migrationStatus?.completed_modules ?? []).length;
    const pending = (migrationStatus?.pending_modules ?? []).length;
    const milestonesArr = migrationStatus?.milestones ?? [];
    const inProgress = milestonesArr.filter(m => m.status === 'in_progress').length;
    console.log('DEBUG completed:', completed, 'pending:', pending, 'milestonesArr:', milestonesArr, 'inProgress:', inProgress);
    barChart = new Chart(barChartRef, {
      type: 'bar',
      data: {
        labels: ['Completati', 'In corso', 'Da iniziare'],
        datasets: [{
          label: 'Moduli Sanitari',
          data: [completed, inProgress, pending],
          backgroundColor: ['#2563eb', '#f59e42', '#e11d48']
        }]
      },
      options: {
        plugins: { legend: { display: false } },
        responsive: true,
        scales: { y: { beginAtZero: true, ticks: { stepSize: 1 } } }
      }
    });
    const total = completed + inProgress + pending;
    pieChart = new Chart(pieChartRef, {
      type: 'pie',
      data: {
        labels: ['Completati', 'In corso', 'Da iniziare'],
        datasets: [{
          data: [completed, inProgress, pending],
          backgroundColor: ['#2563eb', '#f59e42', '#e11d48']
        }]
      },
      options: {
        plugins: { legend: { position: 'bottom' } },
        responsive: true
      }
    });
    const msLabels = milestonesArr.map(m => m.name);
    const msStatus = milestonesArr.map(m => m.status === 'completed' ? 1 : m.status === 'in_progress' ? 0.5 : 0);
    timelineChart = new Chart(timelineChartRef, {
      type: 'line',
      data: {
        labels: msLabels,
        datasets: [{
          label: 'Avanzamento Milestone',
          data: msStatus,
          fill: false,
          borderColor: '#2563eb',
          backgroundColor: '#2563eb',
          tension: 0.2
        }]
      },
      options: {
        scales: {
          y: {
            min: 0,
            max: 1,
            ticks: {
              callback: function(value) {
                if (value === 1) return 'Completata';
                if (value === 0.5) return 'In corso';
                return 'Da iniziare';
              },
              stepSize: 0.5
            }
          }
        },
        plugins: { legend: { display: false } },
        responsive: true
      }
    });
  }
</script>

{#if showGuide}
  <div class="bg-blue-100 border border-blue-300 rounded p-4 mb-6 relative">
    <div class="flex justify-between items-center mb-2">
      <span class="font-semibold text-blue-900">Guida rapida all'uso di PSN Pulse</span>
      <button class="text-blue-700 hover:underline text-sm" on:click={handleHideGuide}>Chiudi guida</button>
    </div>
    <ul class="list-disc ml-6 text-sm mb-2">
      <li>Accedi con <b>API Key di test:</b> <code>psn-pulse-dev-2024</code></li>
      <li>Visualizza lo stato della migrazione, rischi sicurezza e invia dati sanitari mock</li>
      <li>Testa le API direttamente con gli esempi qui sotto (puoi copiare e incollare in Postman/curl)</li>
    </ul>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
      <div>
        <b>Sanity Module (POST /health-data)</b>
        <pre class="bg-gray-50 border rounded p-2 overflow-x-auto">{exampleHealthPayload}</pre>
      </div>
      <div>
        <b>Cybersecurity Tracker (GET /security-risks)</b>
        <pre class="bg-gray-50 border rounded p-2 overflow-x-auto">{exampleSecurityPayload}</pre>
      </div>
      <div>
        <b>Interoperability Tool (POST /health-data)</b>
        <pre class="bg-gray-50 border rounded p-2 overflow-x-auto">{exampleInteropPayload}</pre>
      </div>
    </div>
  </div>
{/if}

<div class="p-6 max-w-4xl mx-auto">
  <h2 class="text-2xl font-bold mb-4">Dashboard Migrazione PSN</h2>
  <div class="mb-4 text-sm text-gray-700">
    <b>Benvenuto!</b> Questa dashboard ti permette di monitorare in tempo reale l'avanzamento della migrazione dati/sistemi della tua PA verso il cloud nazionale (PSN). Consulta le milestone, le aree critiche e i rischi per agire tempestivamente.
  </div>
  {#if loading}
    <div class="text-gray-500">Caricamento dati...</div>
  {:else if error}
    <div class="text-red-600">{error}</div>
  {:else if migrationStatus}
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div class="bg-white rounded shadow p-4">
        <h3 class="font-semibold mb-2">Stato moduli sanitari</h3>
        <canvas bind:this={barChartRef} width="300" height="200" style="background: #eee"></canvas>
      </div>
      <div class="bg-white rounded shadow p-4">
        <h3 class="font-semibold mb-2">Distribuzione moduli</h3>
        <canvas bind:this={pieChartRef} width="300" height="200" style="background: #eee"></canvas>
      </div>
    </div>
    <div class="bg-white rounded shadow p-4 mb-6">
      <h3 class="font-semibold mb-2">Timeline milestone</h3>
      <canvas bind:this={timelineChartRef} width="600" height="120" style="background: #eee"></canvas>
    </div>
    <div class="bg-white rounded shadow p-4"><SanityModule {apiKey} /></div>
    <div class="bg-white rounded shadow p-4"><CybersecurityTracker {apiKey} /></div>
    <div class="bg-white rounded shadow p-4"><InteroperabilityTool {apiKey} /></div>
  {:else}
    <div class="text-gray-500">Nessun dato disponibile</div>
  {/if}
</div> 