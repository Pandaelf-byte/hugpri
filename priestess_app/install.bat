@echo off
echo 🔮 Priestess AI Installation Script
echo =====================================

echo.
echo 📦 Installing Python dependencies...
pip install -r requirements.txt

echo.
echo ✅ Installation complete!
echo.
echo 🚀 You can now run Priestess AI using:
echo    python run_priestess.py
echo    OR
echo    python priestess_cli.py chat --start-server

echo.
echo 📚 For help run:
echo    python priestess_cli.py --help

pause

