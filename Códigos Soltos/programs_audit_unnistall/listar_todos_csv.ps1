$instalados = @()

# Programas 64 bits
$reg64 = [Microsoft.Win32.RegistryKey]::OpenBaseKey('LocalMachine', 'Registry64')
$subKey64 = $reg64.OpenSubKey('SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
$subKey64.GetSubKeyNames() | ForEach-Object {
    $app = $subKey64.OpenSubKey($_)
    if ($app.GetValue('DisplayName')) {
        $instalados += [PSCustomObject]@{
            DisplayName    = $app.GetValue('DisplayName')
            DisplayVersion = $app.GetValue('DisplayVersion')
            Publisher      = $app.GetValue('Publisher')
            InstallDate    = $app.GetValue('InstallDate')
        }
    }
}

# Programas 32 bits
$reg32 = [Microsoft.Win32.RegistryKey]::OpenBaseKey('LocalMachine', 'Registry32')
$subKey32 = $reg32.OpenSubKey('SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
$subKey32.GetSubKeyNames() | ForEach-Object {
    $app = $subKey32.OpenSubKey($_)
    if ($app.GetValue('DisplayName')) {
        $instalados += [PSCustomObject]@{
            DisplayName    = $app.GetValue('DisplayName')
            DisplayVersion = $app.GetValue('DisplayVersion')
            Publisher      = $app.GetValue('Publisher')
            InstallDate    = $app.GetValue('InstallDate')
        }
    }
}

# Exportar
$instalados | Sort-Object DisplayName | Export-Csv "C:\Relatorio_Programas.csv" -NoTypeInformation -Encoding UTF8
Write-Host "Relatório gerado com sucesso."
