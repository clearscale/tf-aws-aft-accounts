import os
import csv
import time
from jinja2 import Environment, PackageLoader, select_autoescape

jinja_env = Environment(
    loader = PackageLoader("main"),
    autoescape = select_autoescape()
)

output_path = os.getcwd() + "/output_" + str(time.time())

def generate_folder():
    print("Using output path: ", output_path)

    try: 
        os.mkdir(output_path) 
    except OSError as error: 
        print(error) 

def generate_template(_template, _data):
    return _template.render(_data)

if __name__ == "__main__":

    generate_folder()

    with open('accounts.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:        
            tf_template = generate_template(
            _template = jinja_env.get_template("account.tf.jinja2"),
            _data = {
                "AccountName": row[0],
                "ManagedOU": row[1],
                "AccountEmail": row[2],
                "SSOUserEmail": row[3],
                "SSOUserFirstName": row[4],
                "SSOUserLastName": row[5],
                }
            )

            with open(output_path + "/" + row[0] + ".tf", "a") as fd:
                fd.write(tf_template)