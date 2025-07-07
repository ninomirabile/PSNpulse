"""
PSN Pulse Backend - Main FastAPI Application
"""

from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Optional, Dict, Any, List
import json
import os
from datetime import datetime, date
from pathlib import Path

from app.models.schemas import (
    MigrationStatus,
    HealthData,
    SecurityRisk,
    APIResponse
)
from app.core.config import settings
from app.core.auth import verify_api_key

app = FastAPI(
    title="PSN Pulse API",
    description="API per il tracking della migrazione PSN",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data loading
def load_mock_data() -> Dict[str, Any]:
    """Load mock data from JSON files"""
    # Use absolute path from current working directory
    mock_data_path = Path.cwd() / "data" / "mock"
    mock_data = {}
    
    print(f"Loading mock data from: {mock_data_path}")
    
    try:
        # Migration status mock data
        migration_file = mock_data_path / "migration_status.json"
        print(f"Migration file path: {migration_file}")
        print(f"Migration file exists: {migration_file.exists()}")
        
        if migration_file.exists():
            with open(migration_file, 'r', encoding='utf-8') as f:
                migration_data = json.load(f)
                print(f"Loaded migration data: {migration_data}")
                mock_data["migration"] = migration_data
        
        # Security risks mock data
        security_file = mock_data_path / "security_risks.json"
        print(f"Security file path: {security_file}")
        print(f"Security file exists: {security_file.exists()}")
        
        if security_file.exists():
            with open(security_file, 'r', encoding='utf-8') as f:
                security_data = json.load(f)
                print(f"Loaded security data: {security_data}")
                mock_data["security"] = security_data
                
    except Exception as e:
        print(f"Warning: Could not load mock data: {e}")
        # Fallback mock data
        mock_data = {
            "migration": {
                "progress": 45,
                "deadline": "2025-12-31",
                "critical_areas": ["Patient Records", "Billing System"],
                "completed_modules": ["User Management", "Basic Security"],
                "pending_modules": ["Data Migration", "API Integration"]
            },
            "security": {
                "risk_level": "medium",
                "tips": [
                    "Enable encryption for all data transfers",
                    "Implement multi-factor authentication",
                    "Regular security audits",
                    "Update access controls"
                ],
                "vulnerabilities": [
                    {"type": "Data Exposure", "severity": "medium", "status": "open"},
                    {"type": "Access Control", "severity": "low", "status": "resolved"}
                ]
            }
        }
    
    print(f"Final mock data: {mock_data}")
    return mock_data

# Global mock data
MOCK_DATA = load_mock_data()

@app.get("/", response_model=APIResponse)
async def root():
    """Root endpoint with API information"""
    return APIResponse(
        success=True,
        message="PSN Pulse API is running",
        data={
            "version": "1.0.0",
            "status": "active",
            "endpoints": {
                "migration_status": "/migration-status",
                "health_data": "/health-data",
                "security_risks": "/security-risks",
                "docs": "/docs"
            }
        }
    )

@app.get("/migration-status", response_model=APIResponse)
async def get_migration_status(
    api_key: str = Depends(verify_api_key)
):
    """Get current migration status and progress"""
    migration_data = MOCK_DATA.get("migration", {})
    print("DEBUG migration_data:", migration_data)
    return APIResponse(
        success=True,
        message="Migration status retrieved successfully",
        data=migration_data
    )

@app.post("/health-data", response_model=APIResponse)
async def submit_health_data(
    health_data: HealthData,
    api_key: str = Depends(verify_api_key)
):
    """Submit healthcare data for PSN integration"""
    # Validate and process health data
    try:
        # Mock processing - in real implementation, this would integrate with PSN APIs
        processed_data = {
            "record_id": health_data.record_id,
            "status": "processed",
            "psn_integration": "pending",
            "validation_errors": [],
            "timestamp": datetime.now().isoformat()
        }
        
        # Simulate processing time
        if health_data.data_type == "patient_record":
            processed_data["psn_integration"] = "completed"
        elif health_data.data_type == "billing":
            processed_data["psn_integration"] = "in_progress"
        
        return APIResponse(
            success=True,
            message="Health data submitted successfully",
            data=processed_data
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error processing health data: {str(e)}"
        )

@app.get("/security-risks", response_model=APIResponse)
async def get_security_risks(
    api_key: str = Depends(verify_api_key)
):
    """Get current security risk assessment"""
    security_data = MOCK_DATA.get("security", {})
    return APIResponse(
        success=True,
        message="Security risks retrieved successfully",
        data=security_data
    )

@app.get("/pnrr-deadlines", response_model=APIResponse)
async def get_pnrr_deadlines(
    api_key: str = Depends(verify_api_key)
):
    """Get PNRR deadlines and notifications"""
    deadlines = [
        {
            "type": "rendicontazione",
            "deadline": "2025-12-31",
            "description": "Scadenza rendicontazione PNRR",
            "priority": "high",
            "days_remaining": 365
        },
        {
            "type": "completamento",
            "deadline": "2026-03-31",
            "description": "Completamento migrazione PSN",
            "priority": "critical",
            "days_remaining": 456
        }
    ]
    
    return APIResponse(
        success=True,
        message="PNRR deadlines retrieved successfully",
        data={"deadlines": deadlines}
    )

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error",
            "data": None
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 