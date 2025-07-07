#!/usr/bin/env bash

set -e

# Colori per output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Funzione cleanup
cleanup() {
    echo -e "\n${YELLOW}Interruzione rilevata, pulizia in corso...${NC}"
    pkill -f uvicorn 2>/dev/null || true
    pkill -f vite 2>/dev/null || true
    echo -e "${GREEN}Pulizia completata${NC}"
    exit 0
}

# Trap per gestire interruzioni
trap cleanup SIGINT SIGTERM

# Controllo prerequisiti
check_prerequisites() {
    echo -e "${GREEN}Controllo prerequisiti...${NC}"
    
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}Errore: Python 3 non trovato${NC}"
        exit 1
    fi
    
    if ! command -v node &> /dev/null; then
        echo -e "${RED}Errore: Node.js non trovato${NC}"
        exit 1
    fi
    
    if ! command -v npm &> /dev/null; then
        echo -e "${RED}Errore: npm non trovato${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Prerequisiti OK${NC}"
}

# Avvio backend
start_backend() {
    echo -e "${GREEN}Avvio backend FastAPI...${NC}"
    cd backend
    
    # Creazione virtualenv se non esiste
    if [ ! -d "venv" ]; then
        echo -e "${YELLOW}Creazione virtualenv backend...${NC}"
        python3 -m venv venv
    fi
    
    # Attivazione virtualenv e installazione dipendenze
    source venv/bin/activate
    echo -e "${YELLOW}Installazione dipendenze backend...${NC}"
    pip install -r requirements.txt > /dev/null 2>&1
    
    # Avvio backend in background
    echo -e "${YELLOW}Avvio server backend...${NC}"
    nohup uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 > ../backend.log 2>&1 &
    BACKEND_PID=$!
    
    # Attesa avvio backend
    sleep 3
    if kill -0 $BACKEND_PID 2>/dev/null; then
        echo -e "${GREEN}✓ Backend avviato su http://localhost:8000 (PID $BACKEND_PID)${NC}"
    else
        echo -e "${RED}✗ Errore avvio backend. Controlla backend.log${NC}"
        exit 1
    fi
    
    cd ..
}

# Avvio frontend
start_frontend() {
    echo -e "${GREEN}Avvio frontend Svelte...${NC}"
    cd frontend
    
    # Installazione dipendenze se mancano
    if [ ! -d "node_modules" ]; then
        echo -e "${YELLOW}Installazione dipendenze frontend...${NC}"
        npm install > /dev/null 2>&1
    fi
    
    # Avvio frontend in background
    echo -e "${YELLOW}Avvio server frontend...${NC}"
    nohup npm run dev -- --host > ../frontend.log 2>&1 &
    FRONTEND_PID=$!
    
    # Attesa avvio frontend
    sleep 5
    if kill -0 $FRONTEND_PID 2>/dev/null; then
        echo -e "${GREEN}✓ Frontend avviato su http://localhost:5173 (PID $FRONTEND_PID)${NC}"
    else
        echo -e "${RED}✗ Errore avvio frontend. Controlla frontend.log${NC}"
        exit 1
    fi
    
    cd ..
}

# Funzione principale
main() {
    echo -e "${GREEN}=== PSN Pulse - Avvio Applicazione ===${NC}"
    
    check_prerequisites
    start_backend
    start_frontend
    
    # Informazioni finali
    echo -e "\n${GREEN}🎉 Tutto pronto!${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "Frontend: ${GREEN}http://localhost:5173${NC}"
    echo -e "Backend:  ${GREEN}http://localhost:8000${NC}"
    echo -e "API Docs: ${GREEN}http://localhost:8000/docs${NC}"
    echo -e "Log:      ${YELLOW}backend.log${NC}, ${YELLOW}frontend.log${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}Per fermare: ./stop.sh o Ctrl+C${NC}"
    echo -e "${YELLOW}API Key di test: psn-pulse-dev-2024${NC}"
    
    # Mantieni script attivo
    echo -e "\n${GREEN}Applicazione in esecuzione... (Ctrl+C per fermare)${NC}"
    wait
}

# Esecuzione
main 