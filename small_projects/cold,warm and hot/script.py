def check_temp(ask):
    if ask >= 28:
        return "HOT"
    elif ask >= 18 and ask < 28:
        return 'WARM'
    elif ask > 18:
        return "COLD"
    else:
        return "NOT VALID Valid values provided"
