## Iniciar projeto:

Verificar se NODE, NPM e Angular estão instalados:
```
node -v
npm -v
npm install -g @angular/cli
```
### Caso não localize no NG VERSION:

#### 1. opção 01:

PS C:\WINDOWS\system32> Set-ExecutionPolicy Unrestricted

```
Alteração da Política de Execução
A política de execução ajuda a proteger contra scripts não confiáveis. A alteração da política de execução pode
implicar exposição aos riscos de segurança descritos no tópico da ajuda about_Execution_Policies em
https://go.microsoft.com/fwlink/?LinkID=135170. Deseja alterar a política de execução?
[S] Sim  [A] Sim para Todos  [N] Não  [T] Não para Todos  [U] Suspender  [?] Ajuda (o padrão é "N"): s
PS C:\WINDOWS\system32>
```

#### 2. opção 02:

inserir a pasta do npm no PATH nas variáveis de ambiente:

```
npm config get prefix
```

### Iniciar projeto:
```
ng new [project-name] --no-standalone
```