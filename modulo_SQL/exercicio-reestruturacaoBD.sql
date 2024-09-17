--Exercício 01: Comece criando uma tabela chamada produtos com as colunas:
--id (chave primária com numeração automática)
--nome (do tipo texto)

CREATE DATABASE super_dev_exercicio;
USE super_dev_exercicio;

CREATE TABLE produtos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50)
);

--1. Inserir registros
--Insira três registros na tabela produtos com nomes de produtos eletrônicos de sua escolha, por exemplo:
--"Smartphone X"
--"Laptop Y"
--"Tablet Z"

INSERT INTO produtos (nome) VALUES 
('Smartphone X'),
('Laptop Y'),
('Tablet Z');

--2. Alterar registros
--Atualize o nome de um dos produtos inseridos para um novo nome diferente. Por exemplo, altere "Laptop Y" para "Ultrabook Y".
UPDATE produtos SET nome='Ultrabook Y' WHERE id=2;

--3. Renomear o nome de uma tabela
--Renomeie a tabela produtos para estoque.
ALTER TABLE produtos RENAME TO estoque;

--4. Renomear o nome de uma coluna
--Renomeie a coluna nome da tabela estoque para nome_produto.
ALTER TABLE estoque RENAME COLUMN nome TO nome_produto;

--5. Alterar o tipo de dado de uma coluna
--Altere o tipo de dado da coluna nome_produto para suportar até 255 caracteres, caso ainda não suporte esse tamanho.
ALTER TABLE estoque MODIFY nome_produto VARCHAR(255);
DESCRIBE estoque;

--6. Definir um valor default para uma coluna
--Adicione uma nova coluna chamada preco na tabela estoque e defina o valor padrão como 0.00.
ALTER TABLE estoque ADD COLUMN preco DOUBLE;
ALTER TABLE estoque ALTER COLUMN preco SET DEFAULT 0.00;
INSERT INTO estoque (nome_produto) VALUES ('PlayStation 5');

--7. Criar uma foreign key para outra tabela
--Embora estejamos trabalhando com uma única tabela, vamos simular uma relação simples:
--Adicione uma nova coluna chamada categoria_id na tabela estoque.
--Crie uma tabela auxiliar chamada categorias com as colunas:
--id (chave primária com numeração automática)
--nome_categoria (do tipo texto)
--Estabeleça uma relação onde categoria_id na tabela estoque referencia id na tabela categorias, criando uma chave estrangeira.

ALTER TABLE estoque ADD COLUMN categoria_id INT;

CREATE TABLE categorias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_categoria VARCHAR(50)
);

INSERT INTO categorias (nome_categoria) VALUES 
('Celular'),
('Notebook'),
('Videogame');

ALTER TABLE estoque ADD CONSTRAINT fk_categoria FOREIGN KEY(categoria_id) REFERENCES categorias(id);

--8. Remover a foreign key de uma tabela sem excluir a coluna
--Remova a restrição da chave estrangeira na coluna categoria_id da tabela estoque, mas mantenha a coluna categoria_id.

ALTER TABLE estoque DROP FOREIGN KEY fk_categoria;

--9. Adicionar o NOT NULL para uma coluna
--Altere a coluna nome_produto na tabela estoque para que não permita valores nulos (NOT NULL).

ALTER TABLE estoque MODIFY nome_produto VARCHAR(255) NOT NULL; 