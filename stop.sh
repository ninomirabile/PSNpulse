#!/usr/bin/env bash

# Colori per output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${YELLOW}Arresto PSN Pulse...${NC}"

# Ferma processi backend
echo -e "${YELLOW}Fermando backend...${NC}"
pkill -f uvicorn 2>/dev/null || true

# Ferma processi frontend
echo -e "${YELLOW}Fermando frontend...${NC}"
pkill -f vite 2>/dev/null || true

# Attesa chiusura processi
sleep 2

# Verifica che tutto sia fermato
if pgrep -f uvicorn > /dev/null; then
    echo -e "${RED}Backend ancora in esecuzione, forzando chiusura...${NC}"
    pkill -9 -f uvicorn 2>/dev/null || true
fi

if pgrep -f vite > /dev/null; then
    echo -e "${RED}Frontend ancora in esecuzione, forzando chiusura...${NC}"
    pkill -9 -f vite 2>/dev/null || true
fi

echo -e "${GREEN}✓ PSN Pulse fermato${NC}" 