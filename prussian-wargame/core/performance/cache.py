import redis
from functools import lru_cache
import hashlib
import json

class TacticalCache:
    """Cache für häufige taktische Entscheidungen"""

    def __init__(self):
        self.redis_client = redis.Redis(
            host='localhost',
            port=6379,
            decode_responses=True
        )
        self.cache_ttl = 3600  # 1 Stunde

    def get_or_compute(self, situation: Dict, compute_func):
        """Cache-or-Compute Pattern"""

        # Erstelle deterministischen Key
        situation_key = self._create_key(situation)

        # Prüfe Cache
        cached = self.redis_client.get(situation_key)
        if cached:
            return json.loads(cached)

        # Berechne wenn nicht im Cache
        result = compute_func(situation)

        # Speichere im Cache
        self.redis_client.setex(
            situation_key,
            self.cache_ttl,
            json.dumps(result)
        )

        return result

    def _create_key(self, situation: Dict) -> str:
        """Erstelle deterministischen Cache-Key"""
        # Sortiere Dictionary für Konsistenz
        sorted_situation = json.dumps(situation, sort_keys=True)
        return f"tactical:{hashlib.md5(sorted_situation.encode()).hexdigest()}"
