CREATE DATABASE super_dev_financeiro;
USE super_dev_financeiro;

CREATE TABLE contas(
    id INT PRIMARY KEY AUTO_INCREMENT,
    saldo DOUBLE NOT NULL
);

INSERT INTO contas (saldo) VALUES
(129.90),
(250.00);

select id as 'ID', format(saldo,2) as 'SALDO' from contas;

-- ALTERANDO OS DADOS DA TABELA:
ALTER TABLE contas RENAME TO despesas;
ALTER TABLE despesas RENAME COLUMN saldo TO valor;
ALTER TABLE despesas ADD COLUMN status INT;
INSERT INTO despesas (valor) VALUES (110);

-- ATUALIZAR DESPESAS:
UPDATE despesas SET status = 0 WHERE id=1;
UPDATE despesas SET status = 1 WHERE id=2;
UPDATE despesas SET status = 1 WHERE id=3;

-- COLUNA despesas será 0 se não informado outro valor:
ALTER TABLE despesas ALTER COLUMN STATUS SET DEFAULT 0;
INSERT INTO despesas (valor) VALUES (950.10);

ALTER TABLE despesas ADD COLUMN nome VARCHAR(50);
ALTER TABLE despesas MODIFY nome VARCHAR(100);

UPDATE despesas SET nome = 'Internet Unifique' WHERE id=1;
UPDATE despesas SET nome = 'Gasolina' WHERE id=2;
UPDATE despesas SET nome = 'Restaurante' WHERE id=3;
UPDATE despesas SET nome = 'Aluguel' WHERE id=4;

ALTER TABLE despesas ADD COLUMN forma_pagamento VARCHAR(20);
UPDATE despesas SET forma_pagamento = 'pix' WHERE id=1;
UPDATE despesas SET forma_pagamento = 'cartão de crédito' WHERE id=2;
UPDATE despesas SET forma_pagamento = 'pix' WHERE id=3;
UPDATE despesas SET forma_pagamento = 'NULL' WHERE id=4;    

SELECT * FROM despesas WHERE forma_pagamento IS NULL;

ALTER TABLE despesas ADD COLUMN data_vencimento DATE;
UPDATE despesas SET data_vencimento = '2024-09-19' WHERE id=1;
UPDATE despesas SET data_vencimento = '2024-09-20' WHERE id=2;
UPDATE despesas SET data_vencimento = '2024-09-15' WHERE id=3;
UPDATE despesas SET data_vencimento = '2024-09-20' WHERE id=4;
ALTER TABLE despesas MODIFY data_vencimento DATE NOT NULL;

ALTER TABLE despesas ADD COLUMN data_pagamento DATE;

UPDATE despesas SET data_pagamento = '2024-09-16' WHERE id=2;
UPDATE despesas SET data_pagamento = '2024-09-15' WHERE id=3;
UPDATE despesas SET data_pagamento = STR_TO_DATE('16/09/2024', '%d/%m/%Y') WHERE id=2;
UPDATE despesas SET data_pagamento = STR_TO_DATE('15/09/2024', '%d/%m/%Y') WHERE id=3;

ALTER TABLE despesas ADD COLUMN categoria VARCHAR(40);
UPDATE despesas SET categoria = 'Contas Casa' WHERE id=1;
UPDATE despesas SET categoria = 'Carro' WHERE id=2;
UPDATE despesas SET categoria = 'Restaurante' WHERE id=3;
UPDATE despesas SET categoria = 'Contas Casa' WHERE id=4;
ALTER TABLE despesas MODIFY categoria VARCHAR(40) NOT NULL; 

CREATE TABLE categorias(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);
INSERT INTO categorias (nome) VALUES 
('Lazer'),
('Restaurante'),
('Contas Casa'),
('Carro'),
('Supermercado');

ALTER TABLE despesas ADD COLUMN id_categoria INT;
UPDATE despesas SET id_categoria = (SELECT id FROM categorias WHERE nome='Contas Casa') WHERE categoria='Contas Casa';
UPDATE despesas SET id_categoria = (SELECT id FROM categorias WHERE nome='Restaurante') WHERE categoria='Restaurante';
UPDATE despesas SET id_categoria = (SELECT id FROM categorias WHERE nome='Carro') WHERE categoria='Carro';

ALTER TABLE despesas DROP COLUMN categoria;

-- SHOW DATA:
SELECT 
    despesas.id, 
    despesas.nome,
    CASE
        WHEN despesas.status = 0 THEN 'PENDENTE'
        WHEN despesas.status = 1 THEN 'PAGO'
        ELSE 'VENCIDO'
    END AS status_formatado,
    FORMAT(despesas.valor, 2) AS valor_formatado,
    date_format(despesas.data_vencimento, '%d/%m/%y') as 'vencimento', 
    despesas.forma_pagamento,
    categorias.nome as 'categoria'
FROM despesas
INNER JOIN categorias ON categorias.id = despesas.id_categoria;
