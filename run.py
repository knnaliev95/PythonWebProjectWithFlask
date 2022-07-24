from flask import Flask, redirect,render_template,request
import sqlite3
app=Flask(__name__)
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        _u_name=request.form["u_name"]
        _u_password=request.form["u_password"]
        conn=sqlite3.connect("users.db")
        query=f"insert into user(u_name,u_password) values ('{_u_name}','{_u_password}')"
        conn.execute(query)
        conn.commit()
    return render_template("register.html")


@app.route("/showdata", methods=["GET","POST"])
def showdata():
    conn=sqlite3.connect("users.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    cursor.execute("select * from user")
    rows=cursor.fetchall()
    for i in rows:
        print(i["id"],i["u_name"],i["u_password"])

    return render_template("data.html",rows=rows)


@app.route("/delete", methods=["GET","POST"])
def delete():
    if request.method=="POST":
        user_name=request.form["u_name"]
        conn=sqlite3.connect("users.db")
        query=f"delete from user where u_name='{user_name}'"
        conn.execute(query)
        conn.commit()
    return render_template("delete.html")


@app.route("/change", methods=["GET","POST"])
def change():
    if request.method=="POST":
        old_username=request.form["old_u_name"]
        old_password=request.form["old_u_password"]
        new_username=request.form["new_u_name"]
        new_password=request.form["new_u_password"]
        conn=sqlite3.connect("users.db")
        u_id=f"select id from user where u_name='{old_username}' and u_password='{old_password}'"
        query=f"update user set u_name='{new_username}, u_password='{new_password}' where id='{u_id}'"
        conn.execute(query)
        conn.commit()

    return render_template("change.html")

if __name__=="__main__":
    app.run(port=5000,debug=True)