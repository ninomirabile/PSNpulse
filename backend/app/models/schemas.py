"""
PSN Pulse Pydantic Schemas
Using Pydantic v2 for data validation
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any, Union
from datetime import datetime, date
from enum import Enum

class DataType(str, Enum):
    """Healthcare data types"""
    PATIENT_RECORD = "patient_record"
    BILLING = "billing"
    LAB_RESULTS = "lab_results"
    PRESCRIPTIONS = "prescriptions"
    ADMINISTRATIVE = "administrative"

class RiskLevel(str, Enum):
    """Security risk levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class VulnerabilitySeverity(str, Enum):
    """Vulnerability severity levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class VulnerabilityStatus(str, Enum):
    """Vulnerability status"""
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class MigrationStatus(BaseModel):
    """Migration status and progress"""
    progress: int = Field(..., ge=0, le=100, description="Migration progress percentage")
    deadline: str = Field(..., description="Migration deadline date")
    critical_areas: List[str] = Field(default_factory=list, description="Critical areas requiring attention")
    completed_modules: List[str] = Field(default_factory=list, description="Completed migration modules")
    pending_modules: List[str] = Field(default_factory=list, description="Pending migration modules")
    milestones: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="Migration milestones")
    
    @validator('progress')
    def validate_progress(cls, v):
        if not 0 <= v <= 100:
            raise ValueError('Progress must be between 0 and 100')
        return v

class HealthData(BaseModel):
    """Healthcare data for PSN integration"""
    record_id: str = Field(..., min_length=1, description="Unique record identifier")
    data_type: DataType = Field(..., description="Type of healthcare data")
    content: Dict[str, Any] = Field(..., description="Data content")
    patient_id: Optional[str] = Field(None, description="Patient identifier")
    facility_id: Optional[str] = Field(None, description="Healthcare facility identifier")
    timestamp: Optional[datetime] = Field(default_factory=datetime.now, description="Data timestamp")
    
    @validator('record_id')
    def validate_record_id(cls, v):
        if not v.strip():
            raise ValueError('Record ID cannot be empty')
        return v.strip()

class Vulnerability(BaseModel):
    """Security vulnerability information"""
    type: str = Field(..., description="Vulnerability type")
    severity: VulnerabilitySeverity = Field(..., description="Vulnerability severity")
    status: VulnerabilityStatus = Field(..., description="Vulnerability status")
    description: Optional[str] = Field(None, description="Vulnerability description")
    discovered_date: Optional[datetime] = Field(None, description="Discovery date")
    resolution_date: Optional[datetime] = Field(None, description="Resolution date")

class SecurityRisk(BaseModel):
    """Security risk assessment"""
    risk_level: RiskLevel = Field(..., description="Overall risk level")
    tips: List[str] = Field(default_factory=list, description="Security improvement tips")
    vulnerabilities: List[Vulnerability] = Field(default_factory=list, description="List of vulnerabilities")
    last_assessment: Optional[datetime] = Field(default_factory=datetime.now, description="Last assessment timestamp")
    recent_incidents: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="Recent security incidents")
    security_officer: Optional[str] = Field(None, description="Security officer name")
    compliance_status: Optional[Dict[str, str]] = Field(default_factory=dict, description="Compliance status for various standards")

class APIResponse(BaseModel):
    """Standard API response format"""
    success: bool = Field(..., description="Request success status")
    message: str = Field(..., description="Response message")
    data: Optional[Union[Dict[str, Any], BaseModel]] = Field(None, description="Response data")
    timestamp: datetime = Field(default_factory=datetime.now, description="Response timestamp")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class PNRRDeadline(BaseModel):
    """PNRR deadline information"""
    type: str = Field(..., description="Deadline type")
    deadline: str = Field(..., description="Deadline date")
    description: str = Field(..., description="Deadline description")
    priority: str = Field(..., description="Priority level")
    days_remaining: int = Field(..., ge=0, description="Days remaining until deadline")

class LoginRequest(BaseModel):
    """API key login request"""
    api_key: str = Field(..., min_length=1, description="API key for authentication")

class LoginResponse(BaseModel):
    """Login response"""
    success: bool = Field(..., description="Login success status")
    message: str = Field(..., description="Login message")
    token: Optional[str] = Field(None, description="Session token (if applicable)")
    expires_at: Optional[datetime] = Field(None, description="Token expiration time") 