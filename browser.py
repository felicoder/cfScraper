from seleniumbase import SB


def getCF(url, uAgent=None, proxy=None, delay=None, headless=False):
    options = {
        "uc": True,
        "locale_code": "en",
        "undetected": True,
        "headless": headless,
        "incognito": True,
        "disable_csp": True,
        "use_wire": True

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

        sb.uc_open_with_reconnect(url, 10)
        sb.uc_gui_handle_captcha()
        sb.sleep(delay)
        cookies = sb.get_cookies()
        cf_clearance_value = next((cookie['value'] for cookie in cookies if cookie['name'] == 'cf_clearance'), None)
        return cf_clearance_value, user_agent
print(getCF("https://fetlife.com/join"))