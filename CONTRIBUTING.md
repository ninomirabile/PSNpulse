# Contributing to PSN Pulse

## Come funziona l'app

PSN Pulse è una dashboard per monitorare la migrazione dati/sistemi delle PA verso il cloud nazionale (PSN). L'utente accede con una API Key, visualizza lo stato della migrazione (progresso, milestone, aree critiche), monitora rischi di cybersecurity e può inviare dati di test. La guida rapida è sempre accessibile dal menu in alto. Logout sempre disponibile.

## Come testare

1. Avvia backend e frontend (`./start.sh`)
2. Accedi con API Key di test: `psn-pulse-dev-2024`
3. Consulta la guida rapida in alto per payload di esempio
4. Prova le azioni rapide: invio dati, simulazione criticità, scarica report
5. Usa il logout per uscire e testare il flusso

## Contribuire a UX e onboarding
- Mantieni la dashboard autoesplicativa
- Aggiorna la guida rapida se cambi il flusso
- Documenta sempre payload e azioni rapide

## Come Contribuire

### Segnalazione Bug

Prima di creare un issue per un bug, assicurati di:

1. **Cercare** se il problema è già stato segnalato
2. **Verificare** che il bug sia riproducibile
3. **Includere** informazioni dettagliate:
   - Sistema operativo
   - Versione di Node.js/Python
   - Passi per riprodurre il bug
   - Comportamento atteso vs. comportamento reale

### Richiesta di Nuove Funzionalità

Per richiedere nuove funzionalità:

1. **Descrivere** chiaramente la funzionalità richiesta
2. **Spiegare** il caso d'uso e il valore aggiunto
3. **Proporre** un approccio implementativo se possibile

### Contributi di Codice

#### Setup dell'Ambiente di Sviluppo

1. **Fork** del repository
2. **Clone** del tuo fork:
   ```bash
   git clone https://github.com/tuo-username/PSNpulse.git
   cd PSNpulse
   ```

3. **Setup** dell'ambiente:
   ```bash
   # Avvio rapido
   ./start.sh
   
   # Oppure manualmente
   cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
   cd frontend && npm install
   ```

#### Convenzioni di Codice

##### Backend (Python/FastAPI)
- **Formattazione**: Usa `black` per la formattazione
- **Linting**: Usa `flake8` per il linting
- **Type hints**: Includi type hints dove appropriato
- **Docstring**: Documenta funzioni e classi
- **Test**: Aggiungi test per nuove funzionalità

```bash
cd backend
black .
flake8 .
pytest
```

##### Frontend (Svelte/JavaScript)
- **Formattazione**: Usa `prettier` per la formattazione
- **Linting**: Usa `eslint` per il linting
- **Componenti**: Segui le convenzioni Svelte
- **Test**: Aggiungi test per nuovi componenti

```bash
cd frontend
npm run format
npm run lint
npm test
```

#### Convenzioni Git

- **Branch**: Usa branch descrittivi: `feature/nome-funzionalita`, `bugfix/descrizione-bug`
- **Commit**: Usa commit semantici:
  - `feat:` per nuove funzionalità
  - `fix:` per correzioni di bug
  - `docs:` per documentazione
  - `style:` per formattazione
  - `refactor:` per refactoring
  - `test:` per test
  - `chore:` per manutenzione

- **Pull Request**: 
  - Descrivi chiaramente le modifiche
  - Includi test se appropriato
  - Assicurati che tutti i test passino
  - Aggiorna la documentazione se necessario

#### Struttura del Codice

##### Backend
```
backend/
├── app/
│   ├── main.py          # Entry point FastAPI
│   ├── models/          # Modelli Pydantic
│   ├── core/            # Configurazione e autenticazione
│   └── api/             # Endpoint API (futuro)
├── tests/               # Test unitari
└── data/mock/           # Dati mock
```

##### Frontend
```
frontend/
├── src/
│   ├── components/      # Componenti Svelte
│   ├── lib/            # Utility e helper
│   └── app.css         # Stili globali
├── public/             # Asset statici
└── tests/              # Test componenti
```

### Processo di Review

1. **Pull Request** viene creata
2. **CI/CD** esegue test automatici
3. **Review** da parte dei maintainer
4. **Approvazione** e merge

### Standard di Qualità

- **Test**: Mantieni una copertura di test adeguata
- **Documentazione**: Aggiorna README e documentazione API
- **Performance**: Considera l'impatto sulle performance
- **Sicurezza**: Segui le best practice di sicurezza
- **Accessibilità**: Assicura l'accessibilità dell'interfaccia

### Comunicazione

- **Issues**: Usa i template forniti
- **Discussioni**: Usa GitHub Discussions per domande generali
- **Chat**: Per comunicazione rapida, usa i commenti nelle PR

## Riconoscimenti

I contributori saranno riconosciuti nel file [CONTRIBUTORS.md](CONTRIBUTORS.md).

## Licenza

Contribuendo a PSN Pulse, accetti che le tue modifiche saranno rilasciate sotto la licenza Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

**Nota**: Questo progetto è rilasciato sotto licenza non commerciale. L'uso commerciale non è permesso senza autorizzazione esplicita.

---

Grazie per contribuire a PSN Pulse! 🚀 