-- APRESENTAR TODOS OS BANCOS DE DADOS CRIADOS:
SHOW SCHEMAS;

-- CRIAR DATABASE
CREATE DATABASE super_dev_loja;

-- SELECIONAR BANCO DE DADOS
USE super_dev_loja;

-- CREATE TABLE
CREATE TABLE cores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) 
);

-- CONSULTAR TABELAS
SHOW TABLES;

-- CONSULTAR OS REGISTROS DA TABELA CORES
SELECT id, nome FROM cores;

-- INSERIR UM DADOS
INSERT INTO cores (nome) VALUE ('vermelho');
INSERT INTO cores (nome) VALUE ('cinza');
INSERT INTO cores (nome) VALUE ('branco');
INSERT INTO cores (nome) VALUE ('preto');
INSERT INTO cores (nome) VALUE ('azul');
INSERT INTO cores (nome) VALUE ('roza');

-- ATUALIZAR
UPDATE cores SET nome='rosa' WHERE id = 6;

-- EXCLUIR
DELETE FROM cores WHERE id = 6;

-- BUSCAR A COR DE CODIGO 4
SELECT FROM cores WHERE id=4;

-- BUSCAR O NOME AZUL
SELECT FROM cores WHERE nome = 'azul';

-- CONSULTAR AS CORES EM ORDEM ALFABÉTICA
SELECT nome FROM cores ORDER BY nome DESC;

-- CRIAR TABELA fabricantes
CREATE TABLE fabricantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100)
);

-- MOSTRAR DADOS DA TABELA
DESCRIBE fabricantes;

-- INSERIR DADO NA TABELA
INSERT INTO fabricantes (nome) VALUE ('Alfa Romeo');
INSERT INTO fabricantes (nome) VALUE ('Ferrari');
INSERT INTO fabricantes (nome) VALUE ('Fiat');
INSERT INTO fabricantes (nome) VALUE ('Honda');
INSERT INTO fabricantes (nome) VALUE ('Hyundai');
INSERT INTO fabricantes (nome) VALUE ('Subaru');
INSERT INTO fabricantes (nome) VALUE ('Volkswagen');

-- CRIAR TABELAS alunos
CREATE TABLE alunos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    nota1 DOUBLE NOT NULL,
    nota2 DOUBLE NOT NULL,
    nota3 DOUBLE NOT NULL,
    data_nascimento DATE NOT NULL,
    descricao TEXT
);

-- INSERINDO OS DADOS
INSERT INTO alunos (nome, nota1, nota2, nota3, data_nascimento, descricao) VALUES
('Jorge', 10, 3.5, 7, "2006-01-26", "Felipe não é o pai" ),
('William', 8, 8.75, 10, "2004-04-27", "Joia rara" ),
('Mateus', 4.3, 7.1, 2, "2007-02-07", "Gremio" ),
('Nicolas', 2, 10, 9.75, "2006-07-12", "Tigrinho" );

-- MOSTRAR DADOS
SELECT * FROM alunos;

-- MOSTRAR IDs DESEJADOS
select * from alunos where id=1 or id=4;

-- MOSTRAR MEDIA
SELECT
    nome AS 'Aluno',
    ROUND((nota1 + nota2 + nota3)/3,2) AS 'Média'
    FROM ALUNOS;

-- MOSTRAR DATA
SELECT 
    nome AS 'Aluno',
    DAY(data_nascimento) AS 'Dia',
    MONTH(data_nascimento) AS 'Mês',
    YEAR(data_nascimento) AS 'Ano'
    FROM alunos
    WHERE YEAR(data_nascimento) = 2006;

-- POKEDEX
CREATE TABLE pokedex(
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    tipo1 VARCHAR(50) NOT NULL,
    tipo2 VARCHAR(50),
    numero_evolucoes INT NOT NULL
);

-- INSERIR DADOS NA POKEDEX
INSERT INTO pokedex (numero, nome, categoria, tipo1, numero_evolucoes) VALUES
(25, 'Pikachu', 'Mouse', 'Eletric', 3),
(54, 'Psyduck', 'Duck', 'Water', 2),
(101, 'Electrode', 'Ball', 'Eletric', 2),
(77, 'Ponyta', 'Fire Horse', 'Fire', 2),
(341, 'Corphish', 'Ruffian', 'Water', 2);

INSERT INTO pokedex (numero, nome, categoria, tipo1, tipo2, numero_evolucoes) VALUES
(75, 'Graveler', 'Rock', 'Rock', 'Ground', 3),
(123, 'Scyther', 'Mantis', 'Bug', 'Flying', 2),
(43, 'Oddish', 'Weed', 'Grass', 'Poison', 3),
(187, 'Hoppip', 'Cottonweed', 'Grass', 'Flying', 3),
(214, 'Heracross', 'Single Horn', 'Bug', 'Fighting', 1);

-- Consultar todos os pokemons com todas as colunas
SELECT * FROM pokedex;
-- Consultar todos os pokemons com as colunas nome, categoria ordenados por categoria
SELECT nome, categoria FROM pokedex ORDER BY categoria;
-- Consultar todos os pokemons com o numero, nome, tipo1 e tipo ordenados por numero 
SELECT numero, nome, tipo1 FROM pokedex ORDER BY numero;
-- Consultar os pokemons da categoria grama com as colunas nome, tipo, tipo2
SELECT nome, tipo1, tipo2 FROM pokedex WHERE categoria='grass';
-- Consultar os pokemons da categoria fantasma com as colunas numero, nome
SELECT numero, nome FROM pokedex WHERE categoria='ghost';
-- Consultar os pokemons que contenham mais do 2 evoluções
SELECT * FROM pokedex WHERE numero_evolucoes=2;