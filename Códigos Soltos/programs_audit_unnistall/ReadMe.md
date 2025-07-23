# 🧹 Programs Audit & Uninstall Tool (PowerShell)

Este projeto foi criado para **auditar e remover programas indesejados** em máquinas Windows, com suporte validado para:
- Windows 7 32 bits (com upgrade para PowerShell 5.1)
- Windows 10 (em testes)

## 📦 Estrutura do Projeto

```

programs\_audit\_uninstall/
├── listar\_todos.ps1          # Lista todos os programas instalados
├── remover\_programas.ps1     # Remove os programas definidos em Remover.txt
├── Remover.txt               # Lista de programas a remover (um por linha)
├── ReadMeFirst.txt           # Instruções detalhadas para Windows 7
├── Win7-KB3191566-x86.zip    # Atualização para PS 5.1 no Windows 7

````

---

## 🛠️ Pré-requisitos

### 🔷 PowerShell 5.0 ou superior

#### ⚠️ Windows 7 (32 bits)
1. Verifique a versão do PowerShell:
   - Se for de 2009 → PS 1.0 → precisa atualizar.
   - Se for de 2016 → PS 5.0 → já compatível.

2. Copie a pasta `programs_audit_uninstall` para `C:\`.

3. Extraia o conteúdo de `Win7-KB3191566-x86.zip` na mesma pasta.

4. Abra o PowerShell como Administrador e execute:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
   .\Install-WMF5.1
````

5. Reinicie o computador após a instalação.

---

## ▶️ Uso do Script (para PS 5.0 ou superior)

1. Copie a pasta `programs_audit_uninstall` para `C:\`.

2. Abra o PowerShell como Administrador e navegue até a pasta:

   ```powershell
   cd "C:\programs_audit_uninstall"
   ```

3. Habilite execução de scripts:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
   ```

4. Liste os programas instalados:

   ```powershell
   .\listar_todos.ps1
   ```

5. Edite o arquivo `Remover.txt` e adicione os programas a remover (um por linha). Exemplo:

   ```
   Recuva
   ```

6. Execute a remoção:

   ```powershell
   .\remover_programas.ps1
   ```

---

## 🚧 Status de Testes

| Sistema Operacional | Status       | Observações                     |
| ------------------- | ------------ | ------------------------------- |
| Windows 7 32 bits   | ✅ OK         | Testado com upgrade para PS 5.1 |
| Windows 10          | 🔄 Em testes |                                 |

---

## ⚠️ Avisos

* Scripts utilizam métodos internos para localizar e desinstalar programas listados. Use com cautela.
* Recomendado rodar **listar\_todos.ps1** antes de configurar a lista de remoção.
* O CMD não foi utilizado nesta auditoria por apresentar limitações técnicas importantes:

   - O comando wmic product é notoriamente lento, impreciso e retorna apenas programas instalados via Windows Installer (.msi), ignorando a maioria dos softwares comuns instalados por .exe.

   - Já o reg query, apesar de mais completo, demanda parsing complexo, o que compromete a legibilidade e manutenção do código em ambientes com múltiplos registros duplicados ou corrompidos.

---

## 📃 Licença

Projeto aberto para fins educacionais e administrativos. Uso por sua conta e risco.


