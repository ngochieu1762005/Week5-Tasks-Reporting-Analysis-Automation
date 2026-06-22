class LMSClient:
    """Demo LMS client. Replace this class with the real LMS API client in production."""

    def __init__(self, fail_for_email=None):
        self.fail_for_email = fail_for_email or set()

    def reactivate_account(self, email: str) -> bool:
        if not email:
            return False
        if email in self.fail_for_email:
            return False
        return True
