import xml.etree.ElementTree as ET
import csv

def xml_to_csv(xml_file_path, csv_file_path):
    # Parsear el archivo XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    # Espacio de nombres para buscar tags específicos
    ns = {
        'ss': 'urn:schemas-microsoft-com:office:spreadsheet'
    }
    
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        
        # Por cada fila en el archivo XML
        for row in root.findall('.//ss:Row', ns):
            row_data = []
            # Por cada celda en la fila
            for cell in row.findall('.//ss:Cell', ns):
                # Obtener el valor de la celda
                data = cell.find('.//ss:Data', ns)
                row_data.append(data.text if data is not None else '')
            writer.writerow(row_data)

paths = [
    '../Well_being_2013.xls',  # Asegúrate de que la extensión refleje el verdadero formato, en este caso, podría ser '.xml'
    '../Well_being_2014.xls',
    '../Well_being_2015.xls',
    '../Well_being_2016.xls',
    '../Well_being_2017.xls',
]

if __name__ == '__main__':
    for path in paths:
        xml_to_csv(path, path[:-4] + '.csv')  # Ajusta la extensión de salida apropiadamente

