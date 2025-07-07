#!/usr/bin/env bash

# Colori per output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Funzione di aiuto
show_help() {
    echo -e "${GREEN}PSN Pulse - Docker Avvio${NC}"
    echo ""
    echo "Uso: $0 [OPZIONE]"
    echo ""
    echo "Opzioni:"
    echo "  prod     Avvia in modalità produzione (default)"
    echo "  dev      Avvia in modalità sviluppo (hot reload)"
    echo "  stop     Ferma tutti i container"
    echo "  logs     Mostra i log dei container"
    echo "  clean    Rimuove container e immagini"
    echo "  help     Mostra questo aiuto"
    echo ""
    echo "Esempi:"
    echo "  $0 prod    # Avvia in produzione"
    echo "  $0 dev     # Avvia in sviluppo"
    echo "  $0 stop    # Ferma tutto"
}

# Controllo Docker
check_docker() {
    if ! command -v docker &> /dev/null; then
        echo -e "${RED}Errore: Docker non trovato${NC}"
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        echo -e "${RED}Errore: Docker Compose non trovato${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Docker OK${NC}"
}

# Avvio produzione
start_prod() {
    echo -e "${GREEN}Avvio PSN Pulse in modalità produzione...${NC}"
    docker-compose up --build -d
    
    echo -e "\n${GREEN}🎉 PSN Pulse avviato in produzione!${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "Frontend: ${GREEN}http://localhost:5173${NC}"
    echo -e "Backend:  ${GREEN}http://localhost:8000${NC}"
    echo -e "API Docs: ${GREEN}http://localhost:8000/docs${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}API Key di test: psn-pulse-dev-2024${NC}"
    echo -e "${YELLOW}Per fermare: $0 stop${NC}"
}

# Avvio sviluppo
start_dev() {
    echo -e "${GREEN}Avvio PSN Pulse in modalità sviluppo...${NC}"
    docker-compose -f docker-compose.dev.yml up --build -d
    
    echo -e "\n${GREEN}🎉 PSN Pulse avviato in sviluppo!${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "Frontend: ${GREEN}http://localhost:5173${NC} (hot reload)"
    echo -e "Backend:  ${GREEN}http://localhost:8000${NC} (hot reload)"
    echo -e "API Docs: ${GREEN}http://localhost:8000/docs${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}API Key di test: psn-pulse-dev-2024${NC}"
    echo -e "${YELLOW}Per fermare: $0 stop${NC}"
}

# Ferma container
stop_containers() {
    echo -e "${YELLOW}Fermando container PSN Pulse...${NC}"
    docker-compose down 2>/dev/null || true
    docker-compose -f docker-compose.dev.yml down 2>/dev/null || true
    echo -e "${GREEN}✓ Container fermati${NC}"
}

# Mostra log
show_logs() {
    echo -e "${YELLOW}Log dei container PSN Pulse:${NC}"
    docker-compose logs -f
}

# Pulizia
clean_docker() {
    echo -e "${YELLOW}Pulizia Docker...${NC}"
    docker-compose down --rmi all --volumes --remove-orphans 2>/dev/null || true
    docker-compose -f docker-compose.dev.yml down --rmi all --volumes --remove-orphans 2>/dev/null || true
    echo -e "${GREEN}✓ Pulizia completata${NC}"
}

# Main
main() {
    case "${1:-prod}" in
        "prod")
            check_docker
            start_prod
            ;;
        "dev")
            check_docker
            start_dev
            ;;
        "stop")
            stop_containers
            ;;
        "logs")
            show_logs
            ;;
        "clean")
            clean_docker
            ;;
        "help"|"-h"|"--help")
            show_help
            ;;
        *)
            echo -e "${RED}Opzione non valida: $1${NC}"
            show_help
            exit 1
            ;;
    esac
}

main "$@" 