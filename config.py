import os
from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    """Application configuration settings"""
    OPENAI_MODEL: str = "gpt-4"
    DEFAULT_DURATION: int = 5
    DEFAULT_ASPECT_RATIO: str = "9:16"
    CACHE_TTL: int = 3600
    MAX_SCRIPT_LENGTH: int = 5000
    MIN_SCRIPT_LENGTH: int = 10
    
    @classmethod
    def from_env(cls):
        """Load configuration from environment variables"""
        return cls(
            OPENAI_MODEL=os.getenv("OPENAI_MODEL", cls.OPENAI_MODEL),
            DEFAULT_DURATION=int(os.getenv("DEFAULT_DURATION", cls.DEFAULT_DURATION)),
            DEFAULT_ASPECT_RATIO=os.getenv("DEFAULT_ASPECT_RATIO", cls.DEFAULT_ASPECT_RATIO),
            CACHE_TTL=int(os.getenv("CACHE_TTL", cls.CACHE_TTL)),
            MAX_SCRIPT_LENGTH=int(os.getenv("MAX_SCRIPT_LENGTH", cls.MAX_SCRIPT_LENGTH)),
            MIN_SCRIPT_LENGTH=int(os.getenv("MIN_SCRIPT_LENGTH", cls.MIN_SCRIPT_LENGTH)),
        )

# Tone and format guidance for better prompts
TONE_GUIDANCE: Dict[str, str] = {
    'inspiring': "Focus on uplifting, aspirational visuals with bright, hopeful imagery",
    'urgent': "Use dynamic, fast-paced, attention-grabbing scenes with high energy",
    'calm': "Emphasize peaceful, serene, and tranquil visuals with soft lighting",
    'funny': "Include playful, lighthearted, and amusing visual elements",
    'serious': "Use professional, authoritative, and formal visual compositions",
    'emotional': "Focus on heartfelt, touching, and deeply moving imagery",
    'uplifting': "Highlight positive, encouraging, and motivational visuals",
    'mysterious': "Create intriguing, enigmatic, and suspenseful atmospheric scenes"
}

FORMAT_GUIDANCE: Dict[str, str] = {
    'UGC': "Suggest authentic, relatable, user-generated style visuals with natural lighting",
    'talking_head': "Focus on supporting visuals that complement a speaker presentation",
    'testimonial': "Use trust-building, credible, and personal experience-focused imagery"
}
