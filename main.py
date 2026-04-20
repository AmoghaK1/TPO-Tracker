from scraper import start_driver, login, get_companies
from storage import load_old_companies, save_companies
from notifier import send_telegram


def main():
    driver = start_driver()

    login(driver)

    current = get_companies(driver)
    old = load_old_companies()

    new_companies = list(set(current) - set(old))

    print("🆕 New Companies:", new_companies)

    # 🔥 SEND TELEGRAM ALERT
    if new_companies:
        message = "🚀 New Companies Added:\n" + "\n".join(new_companies)
        send_telegram(message)

    save_companies(current)

    input("Press Enter to close...")
    driver.quit()

if __name__ == "__main__":
    main()