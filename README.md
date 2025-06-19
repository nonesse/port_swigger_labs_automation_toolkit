# PortSwigger Labs Automation Toolkit

This project is a collection of Python scripts designed to automate solving labs from [PortSwigger Web Security Academy](https://portswigger.net/web-security). So far, it only covers SQL Injection (SQLi).

---

## SQL Injection Scripts

### 🚀 How to use

1. Clone this repository:
   ```bash
   git clone https://github.com/nonesse/port_swigger_labs_automation_toolkit.git
   ```

2. Move to the `sqli` folder:
    ```bash
    cd sqli
    ```

3. Install the dependencies listed in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

4. Adapt the `url` variable inside the script you intend to use.  
   This is necessary because each PortSwigger lab generates a unique URL per user/session.

5. Run the script:
    ```bash
    python3 script_name.py
    ```

### 💬 Output example
![Image](/sql_injections_output.png)

---

## ⚠️ Legal Notice
This tool is intended **solely for educational and ethical penetration testing purposes**. Do not use it against systems you do not own or have explicit permission to test. Unauthorized use may be illegal. The author is not responsible for any misuse or damage caused by this software.