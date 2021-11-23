from sqlalchemy import create_engine
import requests
import time

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
        result = conn.execute(sql_query).fetchone()

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


if __name__ == '__main__':
    #result = read_records_from_table("cpt_hcpcs", 100)



    # print(result)

    result_api = api_poll(1.1, 10)
    print(result_api)