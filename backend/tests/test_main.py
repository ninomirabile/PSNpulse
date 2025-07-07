"""
PSN Pulse Backend Tests
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAPIEndpoints:
    """Test API endpoints"""
    
    def test_root_endpoint(self):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "PSN Pulse API is running" in data["message"]
    
    def test_migration_status_without_auth(self):
        """Test migration status without authentication"""
        response = client.get("/migration-status")
        assert response.status_code == 422  # Missing API key
    
    def test_migration_status_with_auth(self):
        """Test migration status with authentication"""
        headers = {"X-API-Key": "psn-pulse-dev-2024"}
        response = client.get("/migration-status", headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "progress" in data["data"]
        assert "deadline" in data["data"]
    
    def test_security_risks_with_auth(self):
        """Test security risks endpoint with authentication"""
        headers = {"X-API-Key": "psn-pulse-dev-2024"}
        response = client.get("/security-risks", headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "risk_level" in data["data"]
        assert "tips" in data["data"]
    
    def test_pnrr_deadlines_with_auth(self):
        """Test PNRR deadlines endpoint with authentication"""
        headers = {"X-API-Key": "psn-pulse-dev-2024"}
        response = client.get("/pnrr-deadlines", headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "deadlines" in data["data"]
    
    def test_health_data_submission(self):
        """Test health data submission"""
        headers = {"X-API-Key": "psn-pulse-dev-2024"}
        health_data = {
            "record_id": "test-123",
            "data_type": "patient_record",
            "content": {"patient_name": "Test Patient", "diagnosis": "Test"},
            "patient_id": "patient-123"
        }
        response = client.post("/health-data", json=health_data, headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "Health data submitted successfully" in data["message"]

class TestAuthentication:
    """Test authentication"""
    
    def test_invalid_api_key(self):
        """Test with invalid API key"""
        headers = {"X-API-Key": "invalid-key"}
        response = client.get("/migration-status", headers=headers)
        assert response.status_code == 401
    
    def test_missing_api_key(self):
        """Test without API key"""
        response = client.get("/migration-status")
        assert response.status_code == 422

if __name__ == "__main__":
    pytest.main([__file__]) 