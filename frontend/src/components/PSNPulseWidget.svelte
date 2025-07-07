<script>
  export let apiKey = '';
  export let theme = 'light';
  export let modules = 'sanity,security,interop';
  import Dashboard from './Dashboard.svelte';
</script>

<div class={theme === 'dark' ? 'bg-gray-900 text-white' : 'bg-white text-gray-900'}>
  <Dashboard {apiKey} />
</div>

<style>
:host {
  display: block;
  font-family: inherit;
}
</style> 