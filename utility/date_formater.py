from datetime import datetime, timezone

def parse_date(date_str: str) -> datetime:
    print("unparsed_time",date_str)
    date = datetime.strptime(date_str, "%m/%d/%y").replace(tzinfo=timezone.utc)
    print("parsed date:", date)
    return date