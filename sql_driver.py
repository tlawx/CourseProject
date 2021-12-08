from sqlalchemy import create_engine, select, text, Table, MetaData
import requests
import time
import csv

def read_records_from_table(table_name, number_of_records):
    # database name should always _ instead fo non alphanumeric characters
    engine = create_engine("mysql+pymysql://root@localhost/hospital_price_transparency")


    with engine.begin() as conn:
        print("Querying Database")
        result = conn.execute("select * from {} limit {}".format(table_name, number_of_records)).fetchmany(number_of_records)

    return result

def execute_sql(tablename, sql_query):
    # database name should always _ instead fo non alphanumeric characters
    engine = create_engine("mysql+pymysql://root@localhost/hospital_price_transparency")


    with engine.begin() as conn:
        print("Querying Database")
        result = conn.execute(sql_query).fetch()

    return result


def fetch_records_from_api(table_name, number_of_records, offset):
    response = requests.get(" https://www.dolthub.com/api/v1alpha1/dolthub/hospital-price-transparency/master?q=SELECT%20*%0AFROM%20%60{}%60%0Alimit%20{}%20offset%20{}%0A%0A".format(table_name, number_of_records, offset))
    return response


def api_poll(sleep_time, total_records_fetch):
    result = []
    for i in range(total_records_fetch):
        print("Fetch batch #{}".format(i+1))
        result.extend(fetch_records_from_api('cpt_hcpcs', 100, i+1+100))
        time.sleep(sleep_time)

    return result

def query_hospitals_in_city(city):
    city = text(city.title())
    table=text('hospitals')
    # query_str = "select npi_number, name, url, street_address, city, state, zip_code, publish_date FROM hospitals WHERE city = '{}'".format(city.title())

    engine = create_engine("mysql+pymysql://root@localhost/hospital_price_transparency")
    connection = engine.connect()
    metadata = MetaData()
    hospitals = Table('hospitals', metadata, autoload=True, autoload_with=engine)

    query = select([hospitals])

    result = connection.execute(query)
    resultSet = result.fetchmany(10)
    return resultSet

def write_to_csv_file(data):
    with open('test.csv','wb') as out:
        csv_out=csv.writer(out)
        for row in data:
            row = row[:-2]
            print(row)
            csv_out.writerow(row)

if __name__ == '__main__':
    # result = read_records_from_table("cpt_hcpcs", 100)
    # print(result)

    # result_api = api_poll(1.1, 10)
    # print(result_api)

    data = query_hospitals_in_city("chicago")
    write_to_csv_file(data)