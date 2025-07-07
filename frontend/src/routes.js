import Dashboard from './components/Dashboard.svelte';
import Guida from './components/Guida.svelte';
import Login from './components/Login.svelte';

export default {
  '/': Login,
  '/login': Login,
  '/dashboard': Dashboard,
  '/guida': Guida
}; 