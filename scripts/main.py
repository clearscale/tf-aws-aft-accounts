import os
import csv
import shutil
from jinja2 import Environment, PackageLoader, select_autoescape

jinja_env = Environment(
    loader = PackageLoader("main"),
    autoescape = select_autoescape()
)

# shutil.rmtree(os.getcwd() + "/output/")
# os.mkdir(os.getcwd() + "/output/")

def generate_template(_template, _data):
    return _template.render(_data)

if __name__ == "__main__":

    with open('accounts.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            # Account Name,ManagedOrganizationalUnit,TopOu,AccountEmail,SSOUserEmail,SSOUserFirstName,SSOUserLastName
        
            tf_template = generate_template(
            _template = jinja_env.get_template("account.tf.jinja2"),
            _data = {
                "AccountName": row[0],
                "AccountEmail": row[3],
                "ManagedOU": row[1],
                "SSOUserEmail": row[4],
                "SSOUserFirstName": row[5],
                "SSOUserLastName": row[6],
                }
            )

            with open(os.getcwd() + "/output/" + row[0] + ".tf", "a") as fd:
                fd.write(tf_template)