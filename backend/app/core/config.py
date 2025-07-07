"""
PSN Pulse Configuration
Using Pydantic Settings for environment variable management
"""

from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """Application settings"""
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "PSN Pulse API"
    VERSION: str = "1.0.0"
    
    # Security
    API_KEY_SALT: str = "psn-pulse-salt-2024"
    SECRET_KEY: str = "your-secret-key-change-in-production"
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "https://your-pa-domain.gov.it"
    ]
    
    # PSN Configuration
    PSN_API_URL: str = "https://api.psn.gov.it"
    MOCK_DATA_PATH: str = "./data/mock/"
    
    # Database (future)
    DATABASE_URL: str = "sqlite:///./psnpulse.db"
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Global settings instance
settings = Settings()

# Validate required settings
def validate_settings():
    """Validate critical settings"""
    if not settings.API_KEY_SALT or settings.API_KEY_SALT == "psn-pulse-salt-2024":
        print("Warning: Using default API_KEY_SALT. Change in production!")
    
    if not settings.SECRET_KEY or settings.SECRET_KEY == "your-secret-key-change-in-production":
        print("Warning: Using default SECRET_KEY. Change in production!")

# Run validation on import
validate_settings() 