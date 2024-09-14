import mysql.connector

config = {
  'user': 'root',
  'password': 'admin',
  'host': '127.0.0.1',
  'database': 'supermercado',
}

try:
    # Conectar ao banco de dados
    cnx = mysql.connector.connect(**config)
    
    if cnx.is_connected():        
        # Criar um cursor e executar a consulta
        with cnx.cursor() as cursor:
            cursor.execute("""
            SELECT 
                categorias.nome as 'categoria',
                produtos.nome as 'produto',    
                produtos.preco
                FROM produtos
                INNER JOIN categorias ON categorias.id = produtos.id_categoria
                ORDER BY categorias.nome, produtos.nome;
            """)
            rows = cursor.fetchall()
            
            # Imprimir os resultados
            for row in rows:
                categoria, produto, valor = row; 
                print(categoria, produto, valor)
                
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if cnx.is_connected():
        cnx.close()
