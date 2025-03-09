# **MonkeyType Bot 🚀**
A **Selenium-based bot** that automates typing on [MonkeyType](https://monkeytype.com/), an online typing speed test platform.  

## **📌 Features**
- Automatically types words from the MonkeyType test.  
- Uses **Selenium WebDriver** for automation.  
- Stops execution when the `Esc` key is pressed.  
- Implements **explicit waits** for better stability.  

---

## **🛠️ Requirements**
Ensure you have the following installed:  

1. **Python 3.7+** ([Download](https://www.python.org/downloads/))  
2. **Google Chrome** ([Download](https://www.google.com/chrome/))  
3. **Chrome WebDriver** ([Download](https://sites.google.com/chromium.org/driver/))  
4. Required Python packages:  

   ```bash
   pip install selenium keyboard
   ```

---

## **🚀 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/MonkeyType-BOT.git
cd MonkeyType-BOT
```

### **2️⃣ Download Chrome WebDriver**
- Go to [Chrome WebDriver](https://sites.google.com/chromium.org/driver/).  
- Download the **matching version** for your Chrome browser.  
- Place the `chromedriver.exe` in the `webdriver/chromedriver/` folder inside your project.  

---

## **⚡ Usage**
Run the bot using:  

```bash
python bot.py
```

### **🛠️ Configuration**
Edit the script (`bot.py`) to update:  

- **WebDriver Path** (`DRIVER_PATH`)  
  ```python
  DRIVER_PATH = './webdriver/chromedriver/chromedriver.exe'
  ```
  Update this based on where your WebDriver is located.  

- **Website URL**  
  ```python
  URL = 'https://monkeytype.com/'
  ```
  No need to change unless the website changes its structure.  

- **XPath for Words** (`WORDS_XPATH`)  
  ```python
  WORDS_XPATH = '/html/body/div[11]/main/div/div[3]/div[7]/div[4]/div'
  ```
  This may change if MonkeyType updates its site layout.  

---

## **🎯 How It Works**
1. Opens [MonkeyType](https://monkeytype.com/).  
2. Waits for the typing area to load.  
3. Extracts words from the page.  
4. Types the words automatically.  
5. Stops if you press the **Esc** key.  

---

## **⚠️ Disclaimer**
- **Use at your own risk**. Automating typing tests may violate the website’s **terms of service**.  
- This project is for **educational purposes only**.  

---

## **🤝 Contributing**
Feel free to open **issues** or submit **pull requests** if you find bugs or improvements!  

---

## **📜 License**
This project is **open-source** under the MIT License.  

---

## **🔗 Author**
👤 **Savvythelegend**  
🔗 [GitHub Profile](https://github.com/Savvythelegend)  
