import xml.etree.ElementTree as ET

# Carregar o arquivo XML
tree = ET.parse('T2Ti-SisCom-Final.xml')
root = tree.getroot()

# Abrir arquivo SQL para escrita
with open('output.sql', 'w') as sql_file:
    for table in root.findall('.//TABLE'):
        table_name = table.get('Tablename')
        sql_file.write(f"CREATE TABLE `{table_name}` (\n")
        
        # Processar colunas
        columns = []
        for column in table.findall('.//COLUMN'):
            col_name = column.get('ColName')
            data_type = column.get('idDatatype')
            not_null = "NOT NULL" if column.get('NotNull') == "1" else ""
            auto_inc = "AUTO_INCREMENT" if column.get('AutoInc') == "1" else ""
            primary_key = "PRIMARY KEY" if column.get('PrimaryKey') == "1" else ""
            
            columns.append(f"`{col_name}` {data_type} {not_null} {auto_inc} {primary_key}")
        
        sql_file.write(",\n".join(columns))
        sql_file.write("\n);\n\n")
