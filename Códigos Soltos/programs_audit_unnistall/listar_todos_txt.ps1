Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* ,
                 HKLM:\Software\Wow6432Node\Microsoft\* |
Where-Object { $_.DisplayName } |
Select-Object DisplayName, DisplayVersion, Publisher, InstallDate |
Sort-Object DisplayName |
Out-File "C:\Relatorio_Programas_Instalados.txt"
Write-Host "Relatorio criado no &{Out-file}"
