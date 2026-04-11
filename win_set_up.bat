@echo off
powershell -NoProfile -Command "Write-Host ('-- Welcome To K Programming Set Up      --') -ForegroundColor Blue"
powershell -NoProfile -Command "Write-Host ('-- Developer : Niranjan Kumar K         --') -ForegroundColor Green"
powershell -NoProfile -Command "Write-Host ('-- Version   : 1.0                      --') -ForegroundColor Red"
powershell -NoProfile -Command "Write-Host ('-- setting up......................     --') -ForegroundColor Yellow"

if not exist C:\k_programming mkdir C:\k_programming

curl -L https://kni-org.github.io/k/k.exe -o C:\k_programming\k.exe

for /f "tokens=2*" %%A in ('reg query HKCU\Environment /v PATH') do set OLDPATH=%%B
setx PATH "%OLDPATH%;C:\k_programming"

powershell -NoProfile -Command "Write-Host ('-- Successfully installed k programming --') -ForegroundColor Green"
powershell -NoProfile -Command "Write-Host ('-- Restart CMD and run: k --version --') -ForegroundColor Cyan"

del win_set_up.bat
