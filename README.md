# TPO-Tracker 🚀

An automated bot that scrapes the Training and Placement Cell (TPO) website of **Vishwakarma Institute of Technology (VIT) Pune** daily and sends real-time Telegram notifications whenever new companies are added for placements.

## Overview

This bot automates the tedious process of manually checking the TPO placement portal every day. It:
- ✅ Automatically logs into the VIIT TPO portal
- ✅ Scrapes the latest list of companies
- ✅ Compares with previously scraped data
- ✅ Sends instant Telegram notifications when new companies are discovered
- ✅ Runs on a scheduled basis (daily via Windows Task Scheduler)
- ✅ Maintains a local database of companies in JSON format

Perfect for students who want to stay updated on placement opportunities without manually checking the portal multiple times a day.

## Tech Stack

- **Language**: Python 3.10
- **Web Scraping**: Selenium WebDriver
- **Driver Management**: webdriver-manager (automatic ChromeDriver updates)
- **HTTP Requests**: requests library
- **Configuration**: python-dotenv (environment variables)
- **Notifications**: Telegram Bot API
- **Scheduling**: Windows Task Scheduler
- **Data Storage**: JSON

## Prerequisites

Before setting up the bot, make sure you have:
- Windows 10 or Windows 11
- Python 3.7+ installed
- A Telegram account and a bot token
- Your VIIT student credentials (email and password)
- Git (optional, but recommended)

## Setup Guide

Follow these step-by-step instructions to set up the bot on your system.

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/TPO-tracker.git
cd TPO-tracker
```

Or download and extract the ZIP file from GitHub.

### Step 2: Set Up Python Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

You should see `(.venv)` at the beginning of your terminal prompt.

### Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This installs:
- selenium (web automation)
- webdriver-manager (automatic ChromeDriver management)
- requests (HTTP library)
- python-dotenv (environment variable management)

### Step 4: Create Telegram Bot

1. Open Telegram and search for **BotFather**
2. Send `/start` and then `/newbot`
3. Follow the prompts to create a new bot
4. Copy the **Bot Token** (you'll need this in Step 5)
5. Send a message to your newly created bot
6. Go to this URL to get your **Chat ID**: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Replace `<YOUR_BOT_TOKEN>` with your actual bot token
   - Look for the `"id"` field in the response (this is your Chat ID)

### Step 5: Configure Environment Variables

Create a `.env` file in the project root directory (same folder as `main.py`):

```bash
# VIIT TPO Portal Credentials
USERNAME=your_viit_email@viit.ac.in
PASSWORD=your_viit_password

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

**Important Security Note**: Never commit the `.env` file to version control. Add it to `.gitignore` to keep your credentials safe.

Also create a `logs` folder in the project root before running the bot for the first time, since it is ignored by Git and will not be created from the repository.

### Step 6: Test the Bot

Before scheduling, test if everything works:

```bash
python main.py
```

Expected output:
- The bot will open a Chrome browser window (may show `[automated test software]` notification)
- It will log into your VIIT account
- It will scrape companies from the TPO portal
- If it's the first run, it will save all companies and send a Telegram message
- On subsequent runs, it will only notify about NEW companies

Check your Telegram chat to verify you receive notifications.

### Step 7: Set Up Windows Task Scheduler

To run the bot automatically every day:

#### Option A: Using the Batch File (Recommended)

1. Open the `run_tracker.bat` file in the project directory
2. This file is pre-configured to:
   - Activate your virtual environment
   - Run the bot script
   - Handle errors gracefully

#### Option B: Manual Task Scheduler Setup

1. **Open Task Scheduler**
   - Press `Win + R`, type `taskschd.msc`, and press Enter

2. **Create a New Task**
   - Click "Create Basic Task..." in the right panel
   - Name: `TPO Bot - Daily Check`
   - Description: `Automated TPO Company Scraper`

3. **Set Trigger**
   - Choose "Daily"
   - Set start time (e.g., 8:00 AM)
   - Set recurrence to "Every 1 day"

4. **Set Action**
   - Choose "Start a program"
   - Program: `C:\Windows\System32\cmd.exe`
   - Arguments: `/c "G:\PROGRAMMING\MAJOR PROJECTS\TPO-tracker\run_tracker.bat"`
   - Replace the path with your actual project directory

5. **Set Conditions**
   - Uncheck "Stop the task if it runs longer than..."
   - Check "Wake the computer to run this task" (optional)

6. **Click OK** and enter your Windows password when prompted

### Step 8: Verify Scheduling

1. Open Task Scheduler
2. Find "TPO Bot - Daily Check" in the task list
3. Right-click and select "Run" to test
4. Check your Telegram for the notification

## Project Structure

```
TPO-tracker/
├── main.py              # Main entry point
├── scraper.py          # Selenium scraper logic
├── storage.py          # JSON data storage
├── notifier.py         # Telegram notification sender
├── config.py           # Configuration management
├── requirements.txt    # Python dependencies
├── run_tracker.bat     # Windows batch file for scheduling
├── .env                # Environment variables (create this)
├── .gitignore          # Git ignore file
├── data/
│   └── companies.json  # Stored company data
├── logs/
│   └── log.txt        # Application logs
└── README.md          # This file
```

## Usage

### Manual Execution

```bash
.venv\Scripts\activate
python main.py
```

### Scheduled Execution

The bot runs automatically via Windows Task Scheduler. To manually trigger a run:
1. Open Task Scheduler
2. Find "TPO Bot - Daily Check"
3. Right-click and select "Run"

### Checking Logs

Logs are saved in the `logs/` directory. Check `logs/log.txt` for troubleshooting.

### Manual Company Data Check

To view the stored company data:
- Open `data/companies.json` - this file contains all previously scraped companies

## Troubleshooting

### Issue: Bot doesn't send notifications
- **Solution**: Verify your Telegram Bot Token and Chat ID are correct in `.env`
- Test the token: `https://api.telegram.org/bot<TOKEN>/getMe`

### Issue: Login fails
- **Solution**: 
  - Check if your VIIT credentials are correct
  - Ensure your VIIT account isn't locked
  - Try logging in manually to the TPO portal first

### Issue: ChromeDriver errors
- **Solution**: 
  - Restart your system
  - webdriver-manager should auto-download the correct driver
  - Delete the `venv` folder and reinstall dependencies

### Issue: Task Scheduler doesn't run
- **Solution**:
  - Right-click Task Scheduler task and check "Run with highest privileges"
  - Verify the batch file path is correct (use absolute paths)
  - Check Task Scheduler logs for errors

### Issue: "No module named 'selenium'"
- **Solution**: Ensure you've activated the virtual environment before running

## Security Considerations

⚠️ **Important**:
1. **Never commit `.env` to GitHub** - keep your credentials private
2. Use a bot token created specifically for this bot (can be revoked anytime)
3. Don't share your credentials or bot token with anyone
4. The `.env` file should be in `.gitignore` (already configured)

## Customization

### Change Check Frequency
Modify the Task Scheduler trigger to run at different times (e.g., every 6 hours, multiple times a day)

### Custom Telegram Message
Edit `notifier.py` to customize the notification format

### Add Email Notifications
Extend `notifier.py` to send emails in addition to Telegram messages

## Contributing

Feel free to fork this repository and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.

## Disclaimer

This bot is for educational purposes. Use it responsibly:
- Don't overwhelm the server with requests
- Respect the TPO portal's terms of service
- The author is not responsible for any issues arising from using this bot

## Support

If you encounter issues or have questions:
1. Check the Troubleshooting section above
2. Review your `.env` configuration
3. Check the logs in `logs/log.txt`
4. Open an issue on GitHub

## Author

Created for VIIT students to stay updated on placement opportunities.

---

**Last Updated**: May 2026
