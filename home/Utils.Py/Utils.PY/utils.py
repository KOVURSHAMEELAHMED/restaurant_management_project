def estimate_table_turnover_time(table_capacity):
    """
    Estimates the dining duration in minutes based on table size.
    """
    if table_capacity <= 2:
        return 60
    elif table_capacity <= 4:
        return 90
    else:
        return 120