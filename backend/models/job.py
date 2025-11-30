from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from db.database import Base


class StoryJob(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String(36), index=True, unique=True)
    session_id = Column(String(36), index=True)
    theme = Column(String(500))
    status = Column(String(20))
    story_id = Column(Integer, nullable=True)
    error = Column(String(1000), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )
