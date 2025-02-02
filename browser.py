from seleniumbase import SB


def getCF(url, uAgent=None, proxy=None, delay=None, headless=False):
    options = {
        "uc": True,
        "locale_code": "en",
        "undetected": True,
        "headless": headless
    }
    print(delay)
    if not delay:
        delay = 30
    if proxy:
        options["proxy"] = proxy  # Add proxy only if provided
    if uAgent:
        options["agent"] = uAgent  # Add proxy only if provided
    print(options)
    with SB(**options) as sb:
        user_agent = sb.get_user_agent()
        url = url
        sb.activate_cdp_mode(url)
        sb.sleep(delay)
        cookies = sb.get_cookies()
        cf_clearance_value = next((cookie['value'] for cookie in cookies if cookie['name'] == 'cf_clearance'), None)
        return cf_clearance_value, user_agent
