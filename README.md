# MonkeyType-Bot

## Overview
MonkeyType-Bot is an automation script that uses Selenium to interact with the MonkeyType website. The bot automatically types words displayed on the website, simulating a typing test.

## Requirements
- Python 3.x
- Selenium
- Chrome WebDriver
- Keyboard module

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/MonkeyType-Bot.git
    ```
2. Navigate to the project directory:
    ```sh
    cd MonkeyType-Bot
    ```
3. Install the required Python packages:
    ```sh
    pip install selenium keyboard
    ```
4. Download the Chrome WebDriver and place it in the `webdriver/chromedriver` directory.

## Usage
1. Open the `script.py` file and update the `DRIVER_PATH`, `WORDS_XPATH`, and `URL` variables if necessary.
2. Run the script:
    ```sh
    python script.py
    ```
3. The bot will start the browser, navigate to the MonkeyType website, and begin typing the words automatically.
4. Press the `ESC` key to stop the bot.

## Notes
- Ensure that the Chrome browser is installed on your system.
- The `WORDS_XPATH` may need to be updated if the website structure changes.

## License
This project is licensed under the MIT License.