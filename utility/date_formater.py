from datetime import datetime, timezone

def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%m/%d/%y")
