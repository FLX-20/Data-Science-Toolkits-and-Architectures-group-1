from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime, timezone


class InputData(db.Model):
    __tablename__ = 'input_data'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    label = db.Column(db.Text, nullable=False, default="unknown")
    dataset_name = db.Column(db.Text, nullable=False, default="MNIST")
    is_training = db.Column(db.SmallInteger, nullable=False, default=1)


class Predictions(db.Model):
    __tablename__ = 'predictions'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'input_data.id', ondelete='CASCADE'), nullable=False)
    predicted_label = db.Column(db.String, nullable=False)
    model_name = db.Column(db.String, nullable=False)
    prediction_timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
