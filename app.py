from flask import Flask, render_template, Response, request, redirect, url_for, flash, session, redirect
import requests
import json
import string



app = Flask(__name__)
#app.config['SECRET_KEY'] = '1234qwer'

@app.route("/")
def index():
    return redirect('/main')

@app.route('/main', methods=["POST", "GET"])
def main():
    if request.method == 'POST':
        username = request.form['username']
        query = """{
          name
        }"""
        request2 = requests.get(f'https://api.github.com/users/{str(username)}')
        if request2.status_code == 200:
            start_name = request2.json()
        #deadUser = ent.get()
        query1 = """{
          name
        }"""
        request1 = requests.get(f'https://api.github.com/users/{str(username)}/repos')
        if request1.status_code == 200:
            start_repo = request1.json()
        try:
            result = start_name
            name = result["name"]
            result1 = start_repo
            repo = result1
            v = open('repo.json', 'w')
            v.close()
            g = open('repo.json', 'a+')
            h = "[\n"
            g.write(h)
            g.close()
            j = open('repo.json', 'a+')
            lines = " {\n" + "  " + '"name": ' + '"' + f"{str(name)}" + '"' + ","
            j.write(lines)
            j.close()
            t = open('repo.json', 'a+')
            one = " \n" + "  " + '"repo": ['
            t.write(one)
            t.close()
            for user in repo:
                a = user["name"]
                j = open('repo.json', 'a+')
                lines = '\n    {\n' + '     "name2": "' + f"{str(a)}" + '"\n    },'
                j.write(lines)
                j.close()
            k = open('repo.json', 'a+')
            lines = '\n    {\n' + '     "name2": "it was a last one"\n' + '    }' + "\n  ]\n" + " }\n"
            k.write(lines)
            k.close()
            f = open('repo.json', 'a+')
            h = "]"
            f.write(h)
            f.close()
            return redirect(url_for('result'))
        except:
            v = open('repo.json', 'w')
            v.close()
            g = open('repo.json', 'a+')
            h = "[\n"
            g.write(h)
            g.close()
            j = open('repo.json', 'a+')
            lines = " {\n" + "  " + '"name": ' + '"' + "not a user" + '"' + ","
            j.write(lines)
            j.close()
            t = open('repo.json', 'a+')
            one = " \n" + "  " + '"repo": "'
            t.write(one)
            t.close()
            k = open('repo.json', 'a+')
            lines = '"\n' + " }\n"
            k.write(lines)
            k.close()
            f = open('repo.json', 'a+')
            h = "]"
            f.write(h)
            f.close()
            return redirect(url_for('result'))
    return render_template("index.html")

@app.route('/result')
def result():  # put application's code here
    query2 = """query{
              getRepo{
                name
                repo
              }
            }
            """
    try:
        url = 'http://127.0.0.1:8000/'
        r = requests.post(url, json={'query': query2})
        json_data = json.loads(r.text)
        name = json_data['data']['getRepo']
        for name in name:
            a = name['name']
            info_name = open('info.txt', 'w')
            info_name.write(a)
            info_name.close()
            # print("fullname of user: \n" + a)
        repo = json_data['data']['getRepo']
        for repo in repo:
            a = repo['repo']
            b = a.split("[")[1]
            c = b.split("]")[0]
            v = c.replace("'name2': ", "")
            g = v.replace("'}", "")
            n = g.replace("{'", "<p>-")
            j = n.replace(", ", "\n</p>")
            info_runt = open('info.txt', 'a+')
            info_runt.write("\n")
            info_runt.write(j)
            info_runt.close()
            # print("repos of user: \n" + j)
        with open('info.txt', 'r') as f:
            tag = f.read()
            return tag
    except:
        ohh = "not a user"
        return ohh


@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
