<!--
README for: https://github.com/Chirag-pandit/Harry-Poter-ban-jao
Tip: Add your GIFs/PNGs in /assets before pushing:
- assets/harry-title.gif       (banner/hero animation)
- assets/harry-cloak-demo.gif  (screen capture of cloak effect)
-->

<div align="center">
  <img src="assets/harry-title.gif" alt="Harry Potter Cloak Banner" width="720" />
  <h1>🧙‍♂️ Harry Potter Invisibility Cloak — Python + OpenCV</h1>

  <p>
    Real-time invisibility cloak effect built with <b>Python & OpenCV</b>.<br/>
    Press <b>C</b> to capture the background, wear a solid colored cloak (Red/Green/Blue/White), 
    and <i>poof!</i> — you disappear like Harry Potter 🪄.
  </p>

  <!-- Badges -->
  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white" alt="Python"></a>
    <a href="https://opencv.org/"><img src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white" alt="OpenCV"></a>
    <img src="https://img.shields.io/badge/OS-Windows%20%7C%20macOS%20%7C%20Linux-informational" alt="OS">
    <img src="https://img.shields.io/badge/License-MIT-success" alt="License">
  </p>
</div>

---

## ✨ Demo

<p align="center">
  <img src="assets/harry-cloak-demo.gif" alt="Invisibility Cloak Demo" width="720"/>
</p>

---

## 🗂️ Project Structure


---

## 🚀 Quick Start

```bash
# 1) Clone repo
git clone https://github.com/Chirag-pandit/Harry-Poter-ban-jao.git
cd Harry-Poter-ban-jao

# 2) (Optional) Create & activate venv
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run
python src/cloak.py
