-- EXEMPLO 01:

DROP PROCEDURE IF EXISTS somar;

DELIMITER $
CREATE PROCEDURE somar(IN numero1 INT, IN numero2 INT)
BEGIN
	SELECT numero1 + numero2;
END $
DELIMITER ;

CALL somar(10,20);

-- PUXA A HORA ATUAL DO COMPUTADOR;
SELECT NOW();

-- CALCULAR IDADE:

DROP PROCEDURE IF EXISTS calcular_idade;

DELIMITER $
CREATE PROCEDURE calcular_idade(IN ano_nascimento INT)
BEGIN
	SELECT YEAR(NOW()) - ano_nascimento as 'idade';
END $
DELIMITER ;

CALL calcular_idade(1991);

-- COMANDO EXEMPLO

DROP PROCEDURE IF EXISTS criar_despesa;

DELIMITER $ 
CREATE PROCEDURE criar_despesa(
	IN id_categoria INT,
    IN nome VARCHAR(30),
    IN valor DOUBLE,
    IN data_vencimento DATE)
BEGIN 
	INSERT INTO despesas (id_categoria, nome, valor, data_vencimento) VALUE
    (id_categoria, nome, valor, data_vencimento);

    SELECT * FROM despesas ORDER BY id DESC LIMIT 1;
END $
DELIMITER $ 
CALL criar_despesa(1,'CINEMA',50,str_to_date('18/09/2024','%d/%m/%Y'));

-- EXIBIR TODOS OS DADOS:

956

-- ATUALIZAR REGISTRO NO BD:
DROP PROCEDURE IF EXISTS realizar_pagamento;

DELIMITER $ 
CREATE PROCEDURE realizar_pagamento (
	IN nome_de_despesa VARCHAR(50),
    IN forma_de_pagamento VARCHAR(50))
BEGIN 
	DECLARE id_despesa INT;
    SELECT id INTO id_despesa FROM despesas WHERE nome = nome_de_despesa;
    UPDATE despesas SET 
		forma_pagamento = forma_de_pagamento,
        status = 1,
        data_pagamento = date(now())
	WHERE id = id_despesa;
END $
DELIMITER ;

CALL realizar_pagamento('Aluguel','cartão de débito');

-- EXEMPLO FUNCTION:
DROP FUNCTION IF EXISTS concatena_nome_sobrenome;
DELIMITER $
CREATE FUNCTION concatena_nome_sobrenome(nome VARCHAR(30), sobrenome VARCHAR(100)) RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    RETURN CONCAT(nome, ' ', sobrenome);
END $
DELIMITER ;
SELECT concatena_nome_sobrenome('Wolnei', 'Hellmann Dircksen') as 'nome e sobrenome';

-- EXEMPLO FUNCTION COM IF
DROP FUNCTION IF EXISTS calcular_desconto;
DELIMITER $
CREATE FUNCTION calcular_desconto(quantidade_pedido INT) RETURNS DOUBLE
DETERMINISTIC
BEGIN
	DECLARE percentual DOUBLE;
    IF quantidade_pedido <= 2 THEN
		SET percentual := 0;
    ELSEIF quantidade_pedido <= 5 THEN
		SET percentual := 2.5;
    ELSEIF quantidade_pedido <= 10 THEN
		SET percentual := 4.7;
    ELSEIF quantidade_pedido <= 20 THEN
		SET percentual := 6.51;
    ELSEIF quantidade_pedido > 50 THEN
		SET percentual := 10;
    ELSE 
        SET percentual := 15;
	END IF;
    RETURN percentual;
END $
DELIMITER ;

SELECT calcular_desconto(5) as 'desconto';

-- CALCULAR IMC:
-- EXEMPLO FUNCTION COM IF
-- EXEMPLO FUNCTION COM IF
DROP FUNCTION IF EXISTS calcular_imc;
DELIMITER $
CREATE FUNCTION calcular_imc(peso double, altura double) RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
    DECLARE imc DOUBLE; 
    DECLARE classificacao VARCHAR(100);
    SET imc = peso / (altura * altura);
    IF imc < 18.5 THEN
		SET classificacao := 'Abaixo do peso';
    ELSEIF imc >= 18.5 AND imc < 25 THEN
		SET classificacao := 'Peso normal';
    ELSEIF imc >= 25 AND imc < 30 THEN
		SET classificacao := 'Sobrepeso';
    ELSEIF imc >= 30 AND imc < 35 THEN
		SET classificacao := 'Obesidade grau I';
    ELSEIF imc >= 35 AND imc < 40 THEN
		SET classificacao := 'Obesidade grau II';
    ELSE 
        SET classificacao := 'Obesidade grau III';
	END IF;
    RETURN classificacao;
END $
DELIMITER ;