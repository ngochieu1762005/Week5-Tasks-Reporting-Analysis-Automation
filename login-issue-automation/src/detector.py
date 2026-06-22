LOGIN_KEYWORDS = [
    "login", "log in", "cannot login", "can't login", "unable to login",
    "account locked", "account disabled", "account inactive",
    "password reset", "access lms", "cannot access account"
]

SECURITY_KEYWORDS = [
    "hacked", "compromised", "unauthorized", "phishing",
    "password leaked", "suspicious access", "account takeover"
]


def is_login_issue(title: str, description: str) -> bool:
    text = f"{title or ''} {description or ''}".lower()
    return any(keyword in text for keyword in LOGIN_KEYWORDS)


def has_security_risk(title: str, description: str) -> bool:
    text = f"{title or ''} {description or ''}".lower()
    return any(keyword in text for keyword in SECURITY_KEYWORDS)
