# Changelog

Tutte le modifiche notevoli a questo progetto saranno documentate in questo file.

Il formato è basato su [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e questo progetto aderisce al [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Supporto per notifiche PNRR in tempo reale
- Export report in formato PDF/Excel
- Integrazione con API PSN reali
- Database persistente PostgreSQL
- Autenticazione avanzata OAuth2
- Guida rapida sempre accessibile dalla dashboard
- Logout e flusso utente chiaro
- Sezione "Cos'è questa dashboard" e onboarding migliorato
- Dashboard autoesplicativa con milestone, aree critiche, azioni rapide

### Changed
- Miglioramenti performance dashboard
- Ottimizzazione caricamento moduli
- Migliorata la coerenza tra documentazione e interfaccia reale

### Fixed
- Bug di sincronizzazione dati
- Problemi di compatibilità browser

## [1.0.0] - 2024-01-30

### Added
- **Dashboard principale** con visualizzazione stato migrazione PSN
- **Modulo Sanity** per gestione dati sanitari
- **Modulo Cybersecurity Tracker** per monitoraggio rischi sicurezza
- **Modulo Interoperability Tool** per integrazione sistemi legacy
- **Autenticazione API Key** (non persistente server-side)
- **Web Component** `<psn-pulse-widget>` per embedding
- **Backend FastAPI** con endpoint completi:
  - `GET /migration-status` - Stato migrazione
  - `POST /health-data` - Invio dati sanitari
  - `GET /security-risks` - Valutazione rischi
  - `GET /pnrr-deadlines` - Scadenze PNRR
- **Frontend Svelte** con Vite e Tailwind CSS
- **Docker support** per produzione e sviluppo
- **Script di avvio** automatici (`start.sh`, `docker-start.sh`)
- **Test unitari** per backend e frontend
- **Documentazione completa** con README e API docs
- **Mock data** realistici per testing
- **CORS configurato** per integrazione PA
- **Health checks** per container Docker
- **Hot reload** in modalità sviluppo

### Technical Details
- **Backend**: FastAPI 0.104.1, Python 3.11+, Pydantic v2
- **Frontend**: Svelte 4.2.8, Vite 5.0.0, Tailwind CSS 3.3.6
- **Database**: SQLite (preparato per PostgreSQL)
- **Container**: Docker con Alpine Linux
- **Testing**: pytest, Vitest
- **Linting**: black, flake8, eslint, prettier

### Security
- API Key authentication (non persistente)
- CORS configurato per domini PA
- Input validation con Pydantic
- Sanitizzazione dati sanitari

### Documentation
- README completo con setup e utilizzo
- API documentation automatica (Swagger/ReDoc)
- Contributing guidelines
- Code of Conduct
- Changelog
- License MIT

---

## Note di Rilascio

### Versioning
- **Major**: Cambiamenti incompatibili con versioni precedenti
- **Minor**: Nuove funzionalità compatibili con versioni precedenti
- **Patch**: Bug fixes e miglioramenti minori

### Supporto
- **Versione corrente**: Supporto completo
- **Versione precedente**: Supporto bug fixes per 6 mesi
- **Versioni legacy**: Supporto limitato

### Migrazione
Per aggiornamenti tra versioni major, consultare la guida di migrazione specifica. 