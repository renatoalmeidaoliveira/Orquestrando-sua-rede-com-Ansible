import csv

with open('inventario.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    saida = open("inventory", "w+")
    for linha in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            saida.write(f'{linha[0]} ansible_host={linha[1]} ansible_network_os={linha[2]}\n')
    saida.close()
