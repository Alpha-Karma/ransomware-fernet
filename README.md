# ransomware-fernet

Teste de um ransomware simples com Fernet.

obs: Ainda estou vendo porque da erro na importação do "cryptography.fernet", não sei se é por estar offline ou algum erro meu no código.

Funcionamento: Ultilizando o módulo Fernet (criptografia simétrica em AES e HMAC) é gerado uma chave aleatoria e criptografa todos os arquivos da pasta.
para descriptografar, será necessário saber a senha do arquivo chave para executa-lo e assim recuperar todos os arquivos.

