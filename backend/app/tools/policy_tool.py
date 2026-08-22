"""Policy retrieval tools."""

from app.services.lookup_service import get_policy


def retrieve_policy(policy_name: str):
    """Retrieve policy information for agent reasoning."""
    return get_policy(policy_name)
