from flask import Flask, render_template, request

import os
import csv
import rate_system
import data


data_list = data.data_list

#初期rate生成

member = set([])


for i in data_list:
	member = rate_system.member_make(i,member)

sorted_member = sorted(list(member))


app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
	rate = {}
	rate = rate_system.make_rate(member,rate)

	data_ = list(member)
	now = False
	return render_template("test.html",title="title jinja",message="お名前は？",member=sorted_member)

@app.route("/",methods=["POST"])
def index1():
	rate = {}
	rate = rate_system.make_rate(member,rate)

	now = True
	data_ = list(member)
	k = int(request.form.get("k-value"))
	player1 = request.form.get("player1")
	player2 = request.form.get("player2")
	player3 = request.form.get("player3")
	player4 = request.form.get("player4")
	rate_1 = rate_system.rate_all(data_list,rate,"",k)
	expectation = rate_system.expect(player1,player2,player3,player4,rate_1)
	expectation_ave = rate_system.expect_ave(player1,player2,player3,player4,rate_1)
	sorted_rate = sorted(rate_1.items(), key=lambda x:x[1], reverse=True)
	return render_template("test.html",title="title jinja",message="お名前は？",sorted_rate=sorted_rate,member=sorted_member,now=now,
		player1=player1,player2=player2,player3=player3,player4=player4,
		player1_1=round(expectation[0][0],3),player2_1=round(expectation[0][1],3),player3_1=round(expectation[0][2],3),player4_1=round(expectation[0][3],3),
		player1_2=round(expectation[1][0],3),player2_2=round(expectation[1][1],3),player3_2=round(expectation[1][2],3),player4_2=round(expectation[1][3],3),
		player1_3=round(expectation[2][0],3),player2_3=round(expectation[2][1],3),player3_3=round(expectation[2][2],3),player4_3=round(expectation[2][3],3),
		player1_4=round(expectation[3][0],3),player2_4=round(expectation[3][1],3),player3_4=round(expectation[3][2],3),player4_4=round(expectation[3][3],3),
		player1_expe=round(expectation_ave[0],3),player2_expe=round(expectation_ave[1],3),player3_expe=round(expectation_ave[2],3),player4_expe=round(expectation_ave[3],3))


if __name__ == "__main__":
	app.debug = True
	app.run(host="localhost")
