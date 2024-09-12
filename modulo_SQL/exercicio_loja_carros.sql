-- CRIANDO A TABELA:
CREATE TABLE IF NOT EXISTS carros (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_fabricante INT NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    id_cor INT NOT NULL,
    ano INT NOT NULL,
    valor DOUBLE NOT NULL,
    -- CHAVE ESTRANGEIRA:
    FOREIGN KEY (id_fabricante) REFERENCES fabricantes(id),
    FOREIGN KEY (id_cor) REFERENCES cores(id)
);

-- INSERINDO DADO A TABELA:
INSERT INTO carros (id_fabricante, modelo, id_cor, ano, valor) VALUE
(2,"SF90", 1, 2018, 7000000.00);

INSERT INTO carros (id_fabricante, modelo, id_cor, ano, valor) VALUE
(7,"Polo", 2, 2017, 76500.00);

-- INNER JOIN DAS TABELAS:
SELECT carros.id, carros.modelo, carros.ano, cores.nome as 'cor', fabricantes.nome as 'fabricante'
FROM carros
INNER JOIN cores 
    ON cores.id = carros.id_cor 
INNER JOIN fabricantes 
    ON fabricantes.id = carros.id_fabricante;