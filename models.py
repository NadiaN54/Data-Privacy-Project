
class TargetRecord(BaseModel):
    id: str
    age: int = Field(ge=0, le=120)
    zip_code: str
    occupation: str
    gender: str
    medical_flag: str = "unknown"


class AuditRequest(BaseModel):
    target_records: list[TargetRecord] = Field(min_length=1)
    top_k: int = Field(default=4, ge=2, le=10)


class SyntheticRequest(BaseModel):
    record_count: int = Field(default=40, ge=4, le=500)
    planted_match_rate: float = Field(default=.4, ge=0, le=1)
    seed: int = Field(default=42, ge=0)


class Tier(str):
    pass


class ReleasedRecord(BaseModel):
    """Internal release preview; null means the field is suppressed."""
    id: str
    age: int | str | None
    zip_code: str | None
    occupation: str | None
    gender: str | None
    medical_flag: str | None


    @field_validator("age")
    @classmethod
    
