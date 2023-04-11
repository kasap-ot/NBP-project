import random
import pandas as pd
import csv
import python_or_sql_scripts.utils as utils


if __name__ == '__main__':
    random.seed()
    # country_table_length  чува број на редови внесени во табелата COUNTRY.
    # Овој број ни е потребен за да знаеме кој е максималното ID во табелта COUNTRY.
    # И потоа бираме случајна вредост од 1 до country_table_length, и избраната вредност ја користиме како надворешен клуч
    # Значи, колку што имаме надворешни клучеви за една табела, толку променливи треба да имаме од ваков тип,за да се
    # осигураме дека надворешниот клуч секогаш ќе е во рангот на 1 до најголемата-вредност-на индексот т.е вредноста на ова променлива.
    country_table_length = pd.read_csv('../csv_files/country.csv', header=None).shape[0]
    # Патеката вие си ја избирате, само внимавајте да постои таква хиерархија од фолдери xD

    # Бројот на редови зависи од самата табела. Нека биде 1000 на пример па потоа ќе видиме како понатака.
    total_rows = 1000
    with open('../csv_files/company.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0,total_rows):
            # За секој атрибут се генерира вредност.Доколку id-то на соодветната табела не се генерира автоматски тогаш мора да го генерираме.
            # Сите id што имаат тип "serial" во ddl-от се генерираат автоматски.
            # Останатите имаат тип "integer" и мора да се генерирарат рачно преку генерирање на случаен број во ранг од 1 до name_table_length.

            #name
            name = "company " + utils.random_alphabetic_sequence_with_random_length(10,30-len("company "))

            #phone with pattern '[0-9]{9}'
            phone_number = utils.random_phone_number()
            #email with pattern '^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$'
            email_address = utils.random_email()
            #address
            address = utils.random_address()
            #country_id
            country_id = str(random.randint(1,country_table_length))

            #number_of_employees
            number_of_employees = str(random.randint(100,1000))

            # На крај го запишуваме редот во фајлот.
            writer.writerow([name,phone_number,email_address,address,country_id,number_of_employees])




