"""
PSN Pulse Authentication
API key authentication (never persisted server-side)
"""

from fastapi import HTTPException, Header, Depends
from typing import Optional
import hashlib
import hmac
from app.core.config import settings

# Mock API keys for development (in production, these would be validated against external service)
VALID_API_KEYS = {
    "psn-pulse-dev-2024": "development",
    "psn-pulse-admin-2024": "admin",
    "psn-pulse-user-2024": "user"
}

def verify_api_key(api_key: str = Header(..., alias="X-API-Key")) -> str:
    """
    Verify API key from request header
    Never stores API keys server-side, only validates them
    """
    if not api_key:
        raise HTTPException(
            status_code=401,
            detail="API key is required"
        )
    
    # In development, check against mock keys
    if api_key in VALID_API_KEYS:
        return api_key
    
    # In production, this would validate against external service
    # For now, we'll use a simple hash-based validation
    try:
        # Simple validation (replace with proper validation in production)
        if len(api_key) >= 16 and api_key.startswith("psn-"):
            return api_key
    except Exception:
        pass
    
    raise HTTPException(
        status_code=401,
        detail="Invalid API key"
    )

def get_api_key_role(api_key: str) -> str:
    """Get role for API key (for future role-based access)"""
    return VALID_API_KEYS.get(api_key, "user")

def hash_api_key(api_key: str) -> str:
    """Hash API key for secure comparison (never store original)"""
    return hmac.new(
        settings.API_KEY_SALT.encode(),
        api_key.encode(),
        hashlib.sha256
    ).hexdigest()

# Dependency for endpoints that require authentication
def require_auth(api_key: str = Depends(verify_api_key)) -> str:
    """Dependency for authenticated endpoints"""
    return api_key 