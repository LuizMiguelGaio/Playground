$lista = Get-Content "C:\programs_audit_unnistall\Remover.txt"

$regPaths = @(
  "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*",
  "HKLM:\Software\Wow6432Node\Microsoft\*"
)

foreach ($nome in $lista) {
    foreach ($path in $regPaths) {
        $apps = Get-ItemProperty $path | Where-Object { $_.DisplayName -like "*$nome*" }
        foreach ($app in $apps) {
            $uninstall = $app.UninstallString
            if ($uninstall) {
                Write-Output "Removendo: $($app.DisplayName)"
                try {
                    if ($uninstall -match "msiexec") {
                        Start-Process "cmd.exe" "/c $uninstall /quiet /norestart" -Wait
                    } else {
                        Start-Process "cmd.exe" "/c `"$uninstall`" /S /quiet /norestart" -Wait
                    }
                } catch {
                    Write-Warning "Erro ao remover: $($app.DisplayName)"
                }
            }
        }
    }
}
