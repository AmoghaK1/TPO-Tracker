from scraper import start_driver, login, get_companies
from storage import load_old_companies, save_companies
from notifier import send_telegram


def main():
    driver = None

    try:
        driver = start_driver()

        login(driver)

        current = get_companies(driver)
        old = load_old_companies()

        new_companies = list(set(current) - set(old))

        print("New Companies:", new_companies)

        # Send Telegram alert when new companies appear.
        if new_companies:
            message = (
                "🚀 New Companies Added:\n"
                + "\n".join(new_companies)
                + "\n\nApply here: https://tpo.vierp.in"
            )
            send_telegram(message)

        save_companies(current)
    finally:
        if driver is not None:
            driver.quit()

if __name__ == "__main__":
    main()