-- Outro exercício:
-- Criar tabela de estados
--   Colunas: id, sigla
--   Inserir dois registros de estados
--   Consultar todos os estados

CREATE DATABASE endereco;
USE endereco;

CREATE TABLE IF NOT EXISTS estados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    uf VARCHAR(2) NOT NULL
);

INSERT INTO estados (uf) VALUES 
('PR'),
('SC'),
('RS');

SELECT * FROM estados;

-- Criar tabela de cidades
--   Colunas: id, id_estado, nome
--   Inserir duas cidades para cada estado
--   Consultar nome da cidade e seu estado

CREATE TABLE IF NOT EXISTS cidades (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_estado INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    -- CHAVE ESTRANGEIRA:
    FOREIGN KEY (id_estado) REFERENCES estados(id)
);

INSERT INTO cidades (id_estado, nome) VALUES 
(1,'Curitiba'),
(2,'Florianopolis'),
(3,'Porto Alegre');

SELECT 
    estados.uf as 'UF',
    cidades.nome as 'Cidade'
    FROM estados
    INNER JOIN cidades ON cidades.id_estado = estados.id;

-- Criar tabela de bairros
--   Colunas: id, id_cidade, nome
--   Inserir dois bairros para cada cidades
--   Consultar nome do bairro e cidade
--   Consultar nome do bairro, cidade e estado

CREATE TABLE IF NOT EXISTS bairros (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cidade INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    -- CHAVE ESTRANGEIRA:
    FOREIGN KEY (id_cidade) REFERENCES cidades(id)
);

INSERT INTO bairros (id_cidade, nome) VALUES 
(1,'Bigorrilho'),
(1,'Portão'),
(2,'Agronômica'),
(2,'Ingleses'),
(3,'Santa Cecília'),
(3,'Vila Ipiranga');

SELECT 
    estados.uf as 'UF',
    cidades.nome as 'Cidade',
    bairros.nome as 'Bairro'
    FROM estados
    INNER JOIN cidades ON cidades.id_estado = estados.id
    INNER JOIN bairros ON bairros.id_cidade = cidades.id;

-- Criar tabela de endereços
--   Colunas: id, id_bairro, logradouro, numero
--   Inserir dois endereços para cada bairro
--   Consultar dados do endereço por completo(bairro, cidade, estado)

CREATE TABLE IF NOT EXISTS enderecos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_bairro INT NOT NULL,
    logradouro VARCHAR(50) NOT NULL,
    numero INT NOT NULL,
    -- CHAVE ESTRANGEIRA:
    FOREIGN KEY (id_bairro) REFERENCES bairros(id)
);

INSERT INTO enderecos (id_bairro, logradouro, numero) VALUES 
(1,'Rua 01 de curitiba', 123),
(1,'Rua 02 de curitiba', 456),
(2,'Rua 03 de curitiba', 789),
(2,'Rua 04 de curitiba', 001),
(3,'Rua 05 de floripa', 123),
(3,'Rua 06 de floripa', 456),
(4,'Rua 07 de floripa', 789),
(4,'Rua 08 de floripa', 001),
(5,'Rua 09 de POA', 123),
(5,'Rua 10 de POA', 456),
(6,'Rua 11 de POA', 789),
(6,'Rua 12 de POA', 001);

SELECT 
    estados.uf as 'UF',
    cidades.nome as 'Cidade',
    bairros.nome as 'Bairro',
    enderecos.logradouro as 'Logradouro',
    enderecos.numero as 'numero'
    FROM estados
    INNER JOIN cidades ON cidades.id_estado = estados.id
    INNER JOIN bairros ON bairros.id_cidade = cidades.id
    INNER JOIN enderecos ON enderecos.id_bairro = bairros.id;