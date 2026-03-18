import time
from typing import Dict


_user_action_timestamps: Dict[int, float] = {}

COOLDOWN_SECONDS = 1.0


def is_on_cooldown(user_id: int) -> bool:
    now = time.time()
    last_time = _user_action_timestamps.get(user_id, 0.0)
    return (now - last_time) < COOLDOWN_SECONDS


def update_user_action(user_id: int) -> None:
    _user_action_timestamps[user_id] = time.time()
