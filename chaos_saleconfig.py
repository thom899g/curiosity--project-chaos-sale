"""
Configuration management for CHAOS SALE API.
Centralizes all settings with environment variable fallbacks.
"""
import os
import json
import logging
from typing import Dict, Any, Optional
from dataclasses import dataclass, field
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DataTier(str, Enum):
    """Pricing tiers for telemetry data"""
    STANDARD = "standard"  # Per 100