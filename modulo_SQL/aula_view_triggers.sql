CREATE DATABASE super_dev_jogos;
USE super_dev_jogos;

CREATE TABLE Marcas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE Consoles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    marca_id INT NOT NULL,
    FOREIGN KEY (marca_id) REFERENCES Marcas(id)
);

CREATE TABLE Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL
);

CREATE TABLE Vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    data_hora_venda DATETIME NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES Consoles(id)
);

INSERT INTO Marcas (nome) VALUES
('Sony'),
('Microsoft'),
('Nintendo'),
('Sega'),
('Atari');

INSERT INTO Consoles (nome, preco, marca_id) VALUES
('PlayStation 5', 4999.99, 1),
('Xbox Series X', 4599.99, 2),
('Nintendo Switch', 2999.99, 3),
('PlayStation 4', 2799.99, 1),
('Xbox One', 2599.99, 2),
('Nintendo Wii U', 1899.99, 3),
('Sega Genesis', 499.99, 4),
('Atari 2600', 299.99, 5),
('PlayStation 3', 1499.99, 1),
('Xbox 360', 1399.99, 2);

INSERT INTO Clientes (nome, cpf) VALUES
('João Silva', '123.456.789-01'),
('Maria Oliveira', '234.567.890-12'),
('Pedro Souza', '345.678.901-23'),
('Ana Santos', '456.789.012-34'),
('Carlos Lima', '567.890.123-45'),
('Lucia Rodrigues', '678.901.234-56'),
('Marcos Almeida', '789.012.345-67'),
('Patricia Ferreira', '890.123.456-78'),
('Rafael Gomes', '901.234.567-89'),
('Juliana Costa', '012.345.678-90');

INSERT INTO Vendas (id_produto, quantidade, data_hora_venda) VALUES
(1, 2, '2020-01-15 10:30:00'),
(2, 1, '2020-02-20 14:45:00'),
(3, 3, '2020-03-05 09:20:00'),
(4, 1, '2020-04-18 16:50:00'),
(5, 2, '2020-05-22 11:15:00'),
(6, 1, '2020-06-30 13:40:00'),
(7, 4, '2020-07-10 15:05:00'),
(8, 2, '2020-08-25 17:30:00'),
(9, 1, '2020-09-14 12:00:00'),
(10, 3, '2020-10-19 14:25:00'),
(1, 2, '2021-01-10 10:30:00'),
(2, 1, '2021-02-15 14:45:00'),
(3, 3, '2021-03-20 09:20:00'),
(4, 1, '2021-04-25 16:50:00'),
(5, 2, '2021-05-30 11:15:00'),
(6, 1, '2021-06-05 13:40:00'),
(7, 4, '2021-07-10 15:05:00'),
(8, 2, '2021-08-15 17:30:00'),
(9, 1, '2021-09-20 12:00:00'),
(10, 3, '2021-10-25 14:25:00'),
(1, 2, '2019-01-05 10:30:00'),
(2, 1, '2019-02-10 14:45:00'),
(3, 3, '2019-03-15 09:20:00'),
(4, 1, '2019-04-20 16:50:00'),
(5, 2, '2019-05-25 11:15:00'),
(6, 1, '2019-06-30 13:40:00'),
(7, 4, '2019-07-05 15:05:00'),
(8, 2, '2019-08-10 17:30:00'),
(9, 1, '2019-09-15 12:00:00'),
(10, 3, '2019-10-20 14:25:00'),
(1, 2, '2018-01-20 10:30:00'),
(2, 1, '2018-02-25 14:45:00'),
(3, 3, '2018-03-30 09:20:00'),
(4, 1, '2018-04-05 16:50:00'),
(5, 2, '2018-05-10 11:15:00'),
(6, 1, '2018-06-15 13:40:00'),
(7, 4, '2018-07-20 15:05:00'),
(8, 2, '2018-08-25 17:30:00'),
(9, 1, '2018-09-30 12:00:00'),
(10, 3, '2018-10-05 14:25:00'),
(1, 2, '2017-01-25 10:30:00'),
(2, 1, '2017-02-28 14:45:00'),
(3, 3, '2017-03-03 09:20:00'),
(4, 1, '2017-04-06 16:50:00'),
(5, 2, '2017-05-09 11:15:00'),
(6, 1, '2017-06-12 13:40:00'),
(7, 4, '2017-07-15 15:05:00'),
(8, 2, '2017-08-18 17:30:00'),
(9, 1, '2017-09-21 12:00:00'),
(10, 3, '2017-10-24 14:25:00'),
(1, 2, '2016-01-30 10:30:00'),
(2, 1, '2016-02-03 14:45:00'),
(3, 3, '2016-03-06 09:20:00'),
(4, 1, '2016-04-09 16:50:00'),
(5, 2, '2016-05-12 11:15:00'),
(6, 1, '2016-06-15 13:40:00'),
(7, 4, '2016-07-18 15:05:00'),
(8, 2, '2016-08-21 17:30:00'),
(9, 1, '2016-09-24 12:00:00'),
(10, 3, '2016-10-27 14:25:00'),
(1, 2, '2015-01-05 10:30:00'),
(2, 1, '2015-02-08 14:45:00'),
(3, 3, '2015-03-11 09:20:00'),
(4, 1, '2015-04-14 16:50:00'),
(5, 2, '2015-05-17 11:15:00'),
(6, 1, '2015-06-20 13:40:00'),
(7, 4, '2015-07-23 15:05:00'),
(8, 2, '2015-08-26 17:30:00'),
(9, 1, '2015-09-29 12:00:00'),
(10, 3, '2015-10-02 14:25:00'),
(1, 2, '2022-01-10 10:30:00'),
(2, 1, '2022-02-15 14:45:00'),
(3, 3, '2022-03-20 09:20:00'),
(4, 1, '2022-04-25 16:50:00'),
(5, 2, '2022-05-30 11:15:00');


-- VINCULADO VENDAS A CLIENTE:

ALTER TABLE Vendas
ADD COLUMN id_cliente INT NOT NULL;

ALTER TABLE Vendas
ADD FOREIGN KEY (id_cliente) REFERENCES Clientes(id);

-- SELECT ALL:
SELECT 
    vendas.id,
    clientes.nome,
    clientes.cpf,
    DATE_FORMAT(vendas.data_hora_venda, '%d/%m/%y') as "data_venda",
    consoles.nome,
    marcas.nome,
    vendas.quantidade,
    consoles.preco,
    vendas.status
FROM
    VENDAS
        INNER JOIN
    consoles ON vendas.id_console = consoles.id
        INNER JOIN
    marcas ON consoles.id_marca = marcas.id
        INNER JOIN
    clientes ON vendas.id_cliente = clientes.id
WHERE
    vendas.status = 'Completed'
ORDER BY vendas.id;

-- EXEMPLO DE VIEWER:
create view vendas_consoles as
	select marcas.nome as 'marca', consoles.nome as 'console', clientes.nome as 'cliente'
		from vendas
		inner join clientes on (vendas.id_cliente = clientes.id)
		inner join consoles on (vendas.id_produto = consoles.id)
		inner join marcas on (consoles.marca_id = marcas.id);
		
select * from vendas_consoles;

-- exemplo view
create view vendas_finalizadas as
    SELECT 
        vendas.id,
        clientes.nome as 'nome_cliente',
        clientes.cpf,
        DATE_FORMAT(vendas.data_hora_venda, '%d/%m/%y') as "data_venda",
        consoles.nome as 'console',
        marcas.nome,
        vendas.quantidade,
        consoles.preco,
        vendas.status
    FROM
        VENDAS
            INNER JOIN
        consoles ON vendas.id_console = consoles.id
            INNER JOIN
        marcas ON consoles.id_marca = marcas.id
            INNER JOIN
        clientes ON vendas.id_cliente = clientes.id
    WHERE
        vendas.status = 'Completed'
    ORDER BY vendas.id;

SELECT * FROM vendas_finalizadas;

-- TRANSFORMA VALOR DOUBLE EM TEXTO:
DELIMITER $
DROP FUNCTION IF EXISTS formatar_valor $
CREATE FUNCTION formatar_valor(valor double) RETURNS varchar(20)
DETERMINISTIC
BEGIN
	DECLARE valor_formatado VARCHAR(20);
    SELECT CONCAT("R$ ", format(valor,2)) INTO valor_formatado;
    SELECT replace(valor_formatado, ".", ",") INTO valor_formatado;
    RETURN valor_formatado;
END $
DELIMITER ;

select formatar_valor(200.991); -- RETORNA: R$ 200,99

DROP VIEW IF EXISTS vendas_finalizadas;
CREATE VIEW vendas_finalizadas as
    SELECT 
        vendas.id,
        clientes.nome as 'nome_cliente',
        clientes.cpf,
        DATE_FORMAT(vendas.data_hora_venda, '%d/%m/%y') as "data_venda",
        consoles.nome as 'console',
        marcas.nome,
        vendas.quantidade,
        formatar_valor(consoles.preco) AS 'preco',
        vendas.status
    FROM
        VENDAS
            INNER JOIN
        consoles ON vendas.id_console = consoles.id
            INNER JOIN
        marcas ON consoles.id_marca = marcas.id
            INNER JOIN
        clientes ON vendas.id_cliente = clientes.id
    WHERE
        vendas.status = 'Completed'
    ORDER BY vendas.id;

SELECT * FROM vendas_finalizadas;

-- EXEMPLO COM CASE, TRAZENDO VENDAS DE 2018:
DROP VIEW IF EXISTS vendas_finalizadas;
CREATE VIEW vendas_finalizadas as
    SELECT 
        vendas.id,
        clientes.nome as 'nome_cliente',
        clientes.cpf,
        DATE_FORMAT(vendas.data_hora_venda, '%d/%m/%y') as "data_venda",
        consoles.nome as 'console',
        marcas.nome,
        vendas.quantidade,
        formatar_valor(consoles.preco) AS 'preco',
        formatar_valor(vendas.quantidade * consoles.preco) AS 'Total',
        case 
        	when vendas.status = 'Completed' then 'Finalizado'
        	when vendas.status = 'Shipped' then 'Enviado'
        	when vendas.status = 'Cancelled' then 'Cancelado'
        	when vendas.status = 'Pending' then 'Pendente'
        	else 'Retornado'
        end
    FROM
        VENDAS
            INNER JOIN
        consoles ON vendas.id_console = consoles.id
            INNER JOIN
        marcas ON consoles.id_marca = marcas.id
            INNER JOIN
        clientes ON vendas.id_cliente = clientes.id
    WHERE
        YEAR(vendas.data_hora_venda) = 2018
    ORDER BY vendas.id;
    
select * from vendas_finalizadas;
select * from vendas_finalizadas WHERE MONTH(data_venda) = 8;

-- EXEMPLO TRIGGER
ALTER TABLE clientes ADD COLUMN geracao VARCHAR(50);

DELIMITER $
DROP TRIGGER IF EXISTS preencher_geracao $
CREATE TRIGGER preencher_geracao before insert 
on clientes
FOR EACH ROW
BEGIN
    DECLARE ano_nascimento INT;
    DECLARE geracao_cliente VARCHAR(50);
    SET ano_nascimento := YEAR(new.data_nascimento);
    IF ano_nascimento <= 1927 THEN
        SET geracao_cliente := "The Greatest Generation";
    ELSEIF ano_nascimento >= 1928 AND ano_nascimento <= 1945 THEN
        SET geracao_cliente := "The Silent Generation";
    ELSEIF ano_nascimento >= 1946 AND ano_nascimento <= 1964 THEN
        SET geracao_cliente := "Baby Boom Generation";
    ELSEIF ano_nascimento >= 1965 AND ano_nascimento <= 1980 THEN
        SET geracao_cliente := "Generation X";
    ELSEIF ano_nascimento >= 1981 AND ano_nascimento <= 1996 THEN
        SET geracao_cliente := "Generation Y";
    ELSEIF ano_nascimento >= 1997 AND ano_nascimento <= 2010 THEN
        SET geracao_cliente := "Generation Z";
    ELSE
        SET geracao_cliente := "Generation Alpha";
    END IF;
    SET new.geracao := geracao_cliente;
END $
DELIMITER ;

INSERT INTO CLIENTES (nome, data_nascimento, cpf) VALUES 
('José Antônio', '1957-08-16', '12345678900'),
('Pedro', '1985-08-16', '12345678900'),
('Ana Rosa', '1925-08-16', '12345678900'),
('José Brigadeiro', '2003-08-16', '12345678900'),
('Carlos Antônio', '2015-08-16', '12345678900');

SELECT * FROM CLIENTES;

-- OBSERVAÇÃO: COMO NUNCA DELETAR DO BD:
-- remoção fisica:
DELETE FROM vendas WHERE id=88;

-- remoção digital:
ALTER TABLE vendas ADD COLUMN registro_ativo BIT default 1;

UPDATE vendas SET registro_ativo = 0 WHERE id= 38;
SELECT * FROM vendas;
SELECT * FROM vendas WHERE registro_ativo = 1;
SELECT * FROM vendas WHERE registro_ativo = 0;