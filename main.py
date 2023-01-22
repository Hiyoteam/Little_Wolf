# -*- coding: UTF-8 -*-


'''
【设置区域】
改加入地址&频道 bot昵称 bot识别码
'''

# 地址列表:hack.chat
hc="wss://hack.chat/chat-ws"

# 频道列表:yc ycl lo warma
yc="your-channel"
ycl="your-channell"
lo="lounge"
warma="kt1j8rpc"

# 加入地址&频道
socket=hc
channel=yc

# bot昵称:Little_Wolf
botnick="Little_Wolf"

# bot识别码:SB2023
botpass="j3QI-7xVt9HlBuv6PXGXV7Vs176?BSf:RiWgf0Usp7zTrOTfY:FQwx85Vrl34W6B4b.DI9jAk9P3"


# jmr:i want root qwq
# ee:i see quq

# 三字母颜文字:uwu uvu
emote=["uwu","uvu"]


'''
【主要代码】
若要修改请慎重(掀桌
'''

import websocket
import json
import time
import random
import os
import sys
import threading

try:
	# 主要数据库
	data={"uwu":False}

	# root 权限列表
	rootlist=[]

	# 版本号
	ver="uwu.1.14"

	# 卡牌列表
	card={0:{True:"好人",False:"坏人"},
	1:["平民","夜晚：注意旁白 安静等待\n白天：提出意见 跟随大家投票",True],
	2:["预言家","夜晚：选择一位得知身份\n白天：领导大家投票",True],
	3:["狼人","夜晚：选择一位杀死\n白天：隐藏身份 跟随大家投票",False],
	4:["女巫","夜晚：选择一位使用药水 每种药只能使用一次\n白天：隐藏身份 跟随大家投票",True]}

	# 药水列表
	potion={True:["解药","救活"],
	False:["毒药","毒死"]}

	# 初始牌组
	group=[1,1,2,3,3,4]

	# 其他项目
	other={"op":"村长","core":"村民","game":"狼人杀"}

	# 剧情词组:通用
	general=[["选择","决定","打算","想要"],
	["断了气","没了动静","停了心跳","一命呜呼"],
	["深夜","半夜三更","凌晨两点","午夜时分","公鸡打鸣","星云服务器降价"],
	["失去理智","愤愤不平","闹腾","愤怒"],
	["绿色","白色","翻折","皱巴巴","缺了角","整齐叠好","像23的屎","不正经"],
	["收回伸出纸片的手","不知如何抉择","有些迷茫","仔细思考"],
	["误入","闯入","跳进","来到","飞进","滚进","骑着23闯入","在地下吃出一条地道吃入"],
	["欺负","诅咒","戏弄","鞭尸"],
	["飘走了","被偷走了","被捡走了","不翼而飞","被烧了","被23擦屁股了","被拼多多给骗了","被星云当服务器了"],
	["家里","身上","背后","手中","肚子里","保险箱中","午餐盒中","马桶水箱里"]]

	# 剧情词组:预言家
	prophet=[["犯了心肌梗塞","脑子不太清醒","撞到了头","摔了一跤","被水晶球反噬"],
	["叹了口气","沉默不语","喃喃自语","摇了摇头","大喊一声woc"],
	["瞪大了双眼","惊掉了下巴","陷入沉思","不敢置信"],
	["熟","甜","香","舒服"],
	["没有回应","没有行动","家里没人","不在家中","去保养水晶球了"]]

	# 剧情词组:狼人
	werewolf=[["惨叫","哀嚎","悲鸣","呜咽"],
	["四分五裂","难以辨认","被撕咬过","不成样","失败"],
	["呼唤同伴","追赶","奔走","嬉闹"],
	["迷路","走丢","离群","去找对象"],
	["或许是想赌一把","真有心机呢","这样好吗","这样可以吗"],
	["做可以吗","真的好吗","是在协助吗","有没有好处"],
	["伤心欲绝","重情重义","讲义气","悲伤"],
	["沉思中","略显憔悴","望向远方","不太坚定"]]

	# 剧情词组:女巫
	witch=[["自动写代码","让鱼变好吃","让人变性","压缩纸片","让星云降价","让预言家的水晶球出现rickroll"],
	["死一般的寂静","看似一派祥和","已经没有人影了","偶有远处的呼喊","只有一台播放着rickroll的电脑"],
	["无声","安静","静悄悄","悄无声息"],
	["大声","开心","神秘","诡异"],
	["想要休息","不知所踪","的纸片丢失了","的小屋无人打扫"]]

	# bot实际名
	botname=f"{botnick}_{str(random.randint(1,999)).zfill(3)}"

	# 保存配置文件
	def save_config():
		d = ""
		for i in rootlist:
			d=d+i+'\n'
		with open('admintriplist.txt','w') as f:
			f.write(d)
    # 加载配置文件
	def load_config():
		with open('admintriplist.txt','r') as f:
			root=f.read().split('\n')

	try:
		load_config()

		ws=websocket.WebSocket()
		ws.connect(socket)

		time.sleep(0.5)
		ws.send(json.dumps({"cmd":"join","channel":channel,"nick":botname,"password":botpass}))

		time.sleep(0.5)
		ws.send(json.dumps({"cmd":"changecolor","color":"eee"}))

		print(f"{socket}/{channel}\n")
	
	except:
		time.sleep(30)
		os.execl(sys.executable,sys.executable,*sys.argv)

	# text:内容
	def send(text,nick=None):
		time.sleep(1)
		text=str(text).replace("]","](https://)").replace("【","[【").replace("】","】](https://)")

		if text not in emote:
			text=f">\n{text}"

		if nick:
			ws.send(json.dumps({"cmd":"whisper","nick":nick,"text":text}))

		else:
			ws.send(json.dumps({"cmd":"emote","text":text}))

	# list_:列表
	def roll(list_):
		try:
			return random.choice(list_)

		except:
			return None

	# nick:昵称 state:状态
	def chan(nick,state=False):
		data["state"][state].append(data["state"][not state].pop(data["state"][not state].index(nick)))
		data["core"][nick][3]=state

		if not state and nick in data["msg"]:
			time.sleep(1)
			send(f"这时 [{nick}]{roll(general[9])}的遗言被发现了\n[{nick}]：[{data['msg'][nick]}]")

	while True:
		try:
			wss=json.loads(ws.recv())
		
		except:
			time.sleep(30)
			os.execl(sys.executable,sys.executable,*sys.argv)

		if "cmd" in wss:
			cmd=wss["cmd"]
		
			if cmd=="chat":
				nick=wss["nick"]
				text=wss["text"]

				if f"@{botname}" in text:
					send(roll(emote))

				elif text=="|help":
					send(f"·\n【{other['game']}】\n开发者：paperee(ee) jiangmuran(jmr)\n机器人：{botnick}\n版本号：{ver}\n·\n使用手册\n查看帮助：|help\n查看规则：|rules\n获取权限：|root\n开始游戏：|start")

				elif text=="|rules":
					note=str()

					if data["uwu"]:
						note+=f"\n·\n卡牌设置({len(data['group'])}人局)：\n【{card[1][0]}】x{data['group'].count(1)}\n【{card[2][0]}】x{data['group'].count(2)}\n【{card[3][0]}】x{data['group'].count(3)}\n【{card[4][0]}】x{data['group'].count(4)}"
			
					true="".join([f"【{card[_][0]}】" for _ in card if _ and card[_][-1]])
					false="".join([f"【{card[_][0]}】" for _ in card if _ and not card[_][-1]])

					send(f"·\n主要卡牌：\n{true}/【{card[0][True]}】\n{false}/【{card[0][False]}】\n{note}\n·\n限制时长：\n【{card[2][0]}】1分钟\n【{card[3][0]}】2分钟\n【{card[4][0]}】1分钟\n白天投票共4分钟\n·\n游戏特性：\n【{card[1][0]}】擅长推理\n【{card[2][0]}】记性很好\n【{card[3][0]}】杀人不受限制\n【{card[4][0]}】不会猝死")

				elif text[:5]=="|root":
					if (wss.get("trip") in rootlist) or wss.get("trip") == 'ejackX' or wss.get("trip") == 'eYFDHl':
						if text=="|root":
							send(f"[{nick}]成功获取root权限")

							time.sleep(1)
							send(f"·\n可操作项：\n重启(reboot) 关机(close) 添加root用户(add) 删除root用户(delete) 清空root用户(clear) 查看当前牌型/重新加载文件(reload)\n·\n可变更项：\n卡牌(card) 阵营(camp) 药水(potion) 牌组(group) 其他(other)\n·\n变更说明：\n卡牌：牌序(1~4) 牌名(str) 阵营(1/0)\n阵营：正方阵营名(str) 反方阵营名(str)\n药水：好坏(1/0) 药名(str) 状态(str)\n牌组：牌序(1~4)\n其他：发起者称呼(str) 玩家称呼(str) 游戏名(str)",nick)

						else:
							try:
								slices=[_.split(" ") for _ in text.split("\n")]
								order=slices[0][-1]
								note="变更执行成功"

								if order=="reboot":
									print("reboot:success\n")
									send("操作执行成功")

									time.sleep(1)
									os.execl(sys.executable,sys.executable,*sys.argv)

								elif order=="close":
									print("close:success\n")
									send("操作执行成功")

									time.sleep(1)
									ws.close()
									break

								elif order=="card":
									for _ in slices[1:]:
										if int(_[0]):
											card[int(_[0])]=[_[1],card[int(_[0])][1],bool(int(_[2]))]

									print(f"card:{card}\n")

								elif order=="camp":
									card[0]={True:slices[1][0],False:slices[1][1]}
									print(f"card:{card}\n")

								elif order=="potion":
									for _ in slices[1:]:
										potion[bool(int(_[0]))]=[_[1],_[2]]

									print(f"potion:{potion}\n")

								elif order=="group":
									uwu=[int(_) for _ in slices[1] if _ in list("1234")]
									group=uwu

									if data.get("group"):
										data["group"]=uwu

									print(f"group:{group}\n")

								elif order=="reload":
									load_config()
									send("重新加载成功")

									send(str(data),nick)

								elif order=="add":
									rootlist.append(slices[1][0])
									save_config()

								elif order=="delete":
									del rootlist[rootlist.index(slices[1][0])]
									save_config()


								elif order=="clear":
									rootlist=[]
									save_config()


								elif order=="other":
									other={'op':slices[1][0],'core':slices[1][1],'game':slices[1][2]}

								else:
									note="找不到此变更项"+order

								send(note)

							except:
								send("执行时出现错误")

					else:
						send(roll(emote))

				elif text=="|start":
					if data["uwu"]:
						if data.get("core"):
							send(f"【{other['game']}】已经开始了")

						else:
							send(f"【{other['op']}】正在清点村里人数")

					else:
						data={"uwu":True,"owner":nick,"group":group,"time":round(time.time()),"round":0,"temp":[],"core":{},"state":{True:[],False:[]},"sudden":[],"prophet":[],"werewolf":{"skip":False,"core":[],"wait":[],"kill":[],"dead":[]},"witch":{"med":{True:[True,True],False:[False,True]},"temp":[],"allow":[]},"day":{"wait":[],"kill":[],"dead":[]},"msg":{},"now":[]}
						send(f"新的【{other['op']}】诞生了 美好的夜晚要开始了")

						time.sleep(1)
						note=" ".join([str(_) for _ in group])
						send(f"·\n【{other['op']}】[{nick}]\n现在你可以选择改变牌组 否则为默认\n·\n卡牌详情：\n1.【{card[1][0]}】\n2.【{card[2][0]}】\n3.【{card[3][0]}】\n4.【{card[4][0]}】\n·\n默认牌组({len(group)}人局)：\n{note}\n·\n设置方法：\n/w {botname} 牌组",nick)

						time.sleep(0.5)
						send(f"【{other['op']}】开始清点村里人数 请用1报数")

						# 自动判断人数
						def auto():

							# 主循环
							def loop():
								while True:
									data["round"]+=1
									data["werewolf"]["skip"]=False
									data["day"]={"wait":[],"kill":[],"dead":data["day"]["dead"]}

									note=list(data["core"].values())
									data["state"]={True:[_[0] for _ in note if _[3]],
									False:[_[0] for _ in note if not _[3]]}

									time.sleep(4)
									print(f"data:{data}\n")
									send(f"【回合{data['round']}】天黑请闭眼")

									for _ in list(data["core"].keys()):
										uwu=data["core"][_]

										if uwu[1]==2:
											if uwu[3]:
												time.sleep(2)
												send(f"【{card[2][0]}】请睁眼")

												alive=[_ for _ in data["state"][True] if _!=uwu[0]]
												random.shuffle(alive)
												uwu_=" ".join([f"[{_}]" for _ in alive])
												_uwu="\n".join([f"【{card[data['core'][_][1]][0]}】/【{card[0][data['core'][_][2]]}】[{_}]" for _ in data["prophet"]])

												data["now"]=[uwu[1],uwu[0]]

												time.sleep(1)
												send(f"·\n【{card[2][0]}】/【{card[0][True]}】[{uwu[0]}]\n现在你可以选择一位对象得知身份\n请在1分钟内做出选择\n·\n已知身份：\n你自己{_uwu}\n·\n选择方法：\n/w {botname} 对象\n·\n可选对象：\n{uwu_}",uwu[0])

												for _ in range(60):
													time.sleep(1)

													if data["now"][0]!=uwu[1]:
														break

												else:
													chan(uwu[0])
													data["sudden"].append(uwu[0])

													time.sleep(1)
													send(f"【{card[2][0]}】[{uwu[0]}]在今晚{roll(general[1])} 突然猝死")

											else:
												time.sleep(random.randint(10,50))
												send(f"【{card[2][0]}】{roll(prophet[4])}")

										elif uwu[1]==3 and not data["werewolf"]["skip"]:
											if uwu[3]:
												time.sleep(2)
												send(f"【{card[3][0]}】请睁眼")

												alive=list(data["state"][True])
												random.shuffle(alive)
												uwu_=" ".join([f"[{_}]" for _ in alive])

												note=[_ for _ in data["core"] if data["core"][_][1]==3 and data["core"][_][3]]
												data["werewolf"]={"skip":True,"core":note,"wait":note,"kill":[],"dead":data["werewolf"]["dead"]}
												data["now"]=[uwu[1],data["werewolf"]["core"]]

												for _ in data["werewolf"]["core"]:
													time.sleep(1)
													_uwu=" ".join([f"[{__}]" for __ in data["werewolf"]["core"] if __!=_])

													if _uwu:
														_uwu=f"\n·\n你的同伴：\n{_uwu}"

													send(f"·\n【{card[3][0]}】/【{card[0][False]}】[{_}]\n现在你可以选择一位对象杀死\n狼群只有意见统一才会行动\n请在2分钟内做出选择{_uwu}\n·\n选择方法：\n/w {botname} 对象\n·\n可选对象：\n{uwu_}",_)

												for _ in range(120):
													time.sleep(1)

													if data["now"][0]!=uwu[1]:
														break

												else:
													for _ in data["werewolf"]["core"]:
														if _ not in data["werewolf"]["wait"]:
															time.sleep(1)
															send(f"今晚你的同伴猝死了\n{roll(werewolf[6])}的狼群忙于为TA送葬 没有行动",_)

													for _ in data["werewolf"]["wait"]:
														chan(_)
														data["sudden"].append(_)

														time.sleep(1)
														send(f"【{card[3][0]}】[{_}]在今晚{roll(general[1])} 突然猝死")

											else:
												time.sleep(random.randint(20,40))
												send(f"狼群中的狼{roll(werewolf[7])}")

										elif uwu[1]==4:
											if uwu[3]:
												time.sleep(2)
												send(f"【{card[4][0]}】请睁眼")

												data["witch"]={"med":data["witch"]["med"],"temp":[],"allow":[]}
												med=[_ for _ in data["witch"]["med"] if data["witch"]["med"][_][1]]

												if med:
													data["now"]=[uwu[1],uwu[0]]
													dead=[_ for _ in data["state"][False] if _ not in data["sudden"]]
													alive=[_ for _ in data["state"][True] if _!=uwu[0]]

													uwu_=" ".join([f"[{potion[data['witch']['med'][_][0]][0]}]" for _ in med if data['witch']['med'][_][1]])
													_uwu=str()

													if dead and True in med:
														data["witch"]["allow"].extend(dead)
														random.shuffle(dead)
														_uwu+="\n可救："+" ".join([f"[{_}]" for _ in dead])

													if alive and False in med:
														data["witch"]["allow"].extend(alive)
														random.shuffle(alive)
														_uwu+="\n可杀："+" ".join([f"[{_}]" for _ in alive])

													time.sleep(1)
													send(f"·\n【{card[4][0]}】/【{card[0][False]}】[{uwu[0]}]\n现在你可以选择一位对象使用药水\n请在1分钟内做出选择\n·\n选择方法：\n/w {botname} 对象\n·\n所剩药水：\n{uwu_}\n·\n可选对象：{_uwu}",uwu[0])

													for _ in range(60):
														time.sleep(1)

														if data["now"][0]!=uwu[1]:
															break

													else:
														time.sleep(1)
														send(f"黑夜里 只剩【{card[4][0]}】四处飞行的身影")

												else:
													time.sleep(1)
													send(f"·\n【{card[4][0]}】[{uwu[0]}]\n虽然轮到你行动 但你已经用完了药水",uwu[0])

													time.sleep(2)
													send(f"【{card[4][0]}】在研究能{roll(witch[0])}的药水")

											else:
												time.sleep(random.randint(10,50))
												send(f"【{card[4][0]}】{roll(witch[4])}")


									time.sleep(4)
									print(f"data:{data}\n")
									send(f"【回合{data['round']}】天亮了")

									alive=list(data["state"][True])
									random.shuffle(alive)
									uwu_=" ".join([f"[{_}]" for _ in alive])
									_uwu=str()

									if not data["witch"]["temp"] or data["witch"]["temp"][-1]:
										_uwu="是一个平安夜\n"

									if isinstance(data["werewolf"]["kill"],str):
										_uwu=f"[{data['werewolf']['kill']}]被【{card[3][0]}】杀死了\n"

									if data["witch"]["temp"]:
										_uwu+=f"[{data['witch']['temp'][0]}]被使用[{potion[data['witch']['temp'][-1]][0]}]的【{card[4][0]}】[{potion[data['witch']['temp'][-1]][1]}]了\n"

									time.sleep(2)
									send(f"【公告】昨晚{_uwu}")

									data["stats"]=[[_ for _ in data["core"] if data["core"][_][2] and data["core"][_][3]],
									[_ for _ in data["core"] if not data["core"][_][2] and data["core"][_][3]]]

									if not all(data["stats"]):
										break

									data["now"]=[0,data["state"][True]]
									data["day"]={"wait":list(data["state"][True]),"kill":[],"dead":data["day"]["dead"]}

									time.sleep(2)
									send(f"·\n投票环节：\n每人一票 得票数最高的【{other['core']}】会被处死\n请在4分钟内做出选择\n·\n选择方法：\n/w {botname} 对象\n·\n可选对象：\n{uwu_}")

									for _ in range(240):
										time.sleep(1)

										if not data["day"]["wait"]:
											break

										elif _==180:
											send("白天仅剩1分钟了")

									else:
										for _ in data["day"]["wait"]:
											if data["core"][_][1]!=4:
												chan(_)
												data["sudden"].append(_)

												time.sleep(2)
												send(f"【{card[data['core'][_][1]][0]}】[{_}]在白天{roll(general[1])} 突然猝死")

									if data["day"]["kill"]:
										time.sleep(2)
										note=max(set(data["day"]["kill"]),key=data["day"]["kill"].count)

										try:
											chan(note)
											data["day"]["dead"].append(note)
											send(f"【公告】投票结果统计完成\n{roll(general[3])}的【{other['core']}】们处死了[{note}]")

										except:
											send(f"【公告】投票结果统计完成\n{roll(general[3])}的【{other['core']}】们{roll(general[0])}处死[{note}]\n但当发现时 [{note}]已经猝死在家中了")

										alive=list(data["state"][True])
										random.shuffle(alive)
										uwu_=" ".join([f"[{_}]" for _ in alive])

										time.sleep(2)
										send(f"目前留在村子里的人有：\n{uwu_}")

									data["stats"]=[[_ for _ in data["core"] if data["core"][_][2] and data["core"][_][3]],
									[_ for _ in data["core"] if not data["core"][_][2] and data["core"][_][3]]]
				
									if not all(data["stats"]):
										break

								time.sleep(4)
								winner=data["stats"].index([])

								if winner:
									send(f"不知什么时候 天气变得晴朗\n大家清楚地感受到 邪恶从村子里消失了")

								else:
									send(f"这个村子正在发生异变\n血色笼罩村庄 时不时传来邪恶的声音")

								uwu=[[f"[{_}]" for _ in data["stats"][not int(winner)]],
								[f"[{_}]" for _ in data["core"] if data["core"][_][2]==winner and not data["core"][_][3]],
								[f"[{_}]" for _ in data["core"] if data["core"][_][2]==(not winner)],
								[f"[{_}]" for _ in data["prophet"]],
								[f"[{_}]" for _ in data["werewolf"]["dead"]],
								[f"\n【{card[4][0]}】[{potion[data['witch']['med'][_][0]][1]}]了：[{data['witch']['med'][_][-1]}]" for _ in data["witch"]["med"] if not data["witch"]["med"][_][1]],
								[f"[{_}]" for _ in data["day"]["dead"]]]

								note=[str() for _ in range(3)]

								for _ in range(len(uwu)):
									if uwu[_]:
										if not _:
											note[0]+=f"\n存活({len(data['stats'][not winner])})："+" ".join(uwu[_])

										elif _==1:
											note[0]+=f"\n死亡({len(uwu[_])})："+" ".join(uwu[_])

										elif _==2:
											note[1]+=f"\n死亡({len(uwu[_])})："+" ".join(uwu[_])

										else:
											if _==3:
												note[2]+=f"\n【{card[2][0]}】知道了："+" ".join(uwu[_])

											elif _==4:
												note[2]+=f"\n【{card[3][0]}】杀死了："+" ".join(uwu[_])

											elif _==5:
												note[2]+="".join(uwu[_])

											elif _==6:
												note[2]+=f"\n投票处死了："+" ".join(uwu[_])

								else:
									if note[2]:
										note[2]=f"\n·\n特殊数据：{note[2]}"

								time.sleep(2)
								send(f"【{card[0][not winner]}】阵亡 【{card[0][winner]}】胜利")

								minutes=divmod(round(time.time()-data["time"]),60)
								send(f"·\n统计数据：\n时长：{minutes[0]}分钟 {minutes[1]}秒\n回合数：{data['round']}\n·\n【{card[0][winner]}】(胜){note[0]}\n·\n【{card[0][not winner]}】(败){note[1]}{note[2]}")

								time.sleep(1)
								send(f"本局结束 完结撒花")

								data.clear()
								data["uwu"]=False

								sys.exit(0)

							while True:
								if data["uwu"] and len(data["temp"])==len(data["group"]):
									data["notice"]="@"+" @".join(data["temp"])+" "
									send(f"{data['notice']}\n人数到齐 开始抽牌 请注意查看私聊")

									random.shuffle(data["temp"])

									try:
										for _ in data["temp"]:
											note=data["group"][data["temp"].index(_)]
											data["core"][_]=[_,note,card[note][2],True]

											time.sleep(1)
											send(f"·\n你的卡牌：\n【{card[note][0]}】/【{card[0][card[note][2]]}】\n·\n你的任务：\n{card[note][1]}\n·\n获胜条件：\n【{card[0][not card[note][2]]}】全员阵亡\n·\n设置遗言(死亡前有效)：\n/w {botname} msg(换行)遗言",_)

									except:
										for _ in data["temp"][len(data["group"])-1:]:
											data["temp"].pop(data["temp"].index(_))

									time.sleep(2)
									send(f"发牌完毕 【{other['game']}】正式开始")

									# 开启多线程
									threading.Thread(target=loop).start()
									break

								else:
									time.sleep(2)

							sys.exit(0)

						# 开启多线程
						threading.Thread(target=auto).start()

				elif data["uwu"]:
					if not data["core"]:
						if text=="1":
							if nick in data["temp"]:
								send(f"[{nick}]已经在花名册中了")

							else:
								data["temp"].append(nick)
								send(f"[{nick}]{roll(general[6])}了村子 村里有{len(data['temp'])}人了")

			elif cmd=="info" and wss.get("type")=="whisper":
				if "from" in wss:
					nick=str(wss["from"])
					text=wss["text"]
					uwu=text[text.find(":")+2:]

					if data["uwu"]:
						msg=uwu.split("\n",1)

						if not data["core"]:
							if nick==data["owner"]:
								allow=[int(_) for _ in uwu.split(" ") if _ in list("1234")]

								if allow==data["group"]:
									send("牌组和原先相同 不变更",nick)

								elif len(allow)<len(data["temp"]):
									send("花名册的人数已经超过牌数了",nick)

								else:
									data["group"]=sorted(allow)
									send(f"【{other['op']}】更改了【{other['core']}】身份牌数目")

									time.sleep(1)
									send(f"现卡牌设置({len(allow)}人局)：\n1.【{card[1][0]}】x{allow.count(1)}\n2.【{card[2][0]}】x{allow.count(2)}\n3.【{card[3][0]}】x{allow.count(3)}\n4.【{card[4][0]}】x{allow.count(4)}")

						elif msg[0]=="msg" and nick in data["state"][True]:
							if len(msg)<2 and not msg[1].strip():
								send("请写下你的遗言",nick)

							elif "$" in text and not(wss.get("trip") in rootlist):
								send("如果说 遗言不允许LaTeX？",nick)

							else:
								if nick in data["msg"]:
									send("遗言更新成功",nick)

								else:
									send("遗言添加成功",nick)

								data["msg"][nick]=msg[1]

						elif data.get("now"):
							if nick in data["day"]["wait"]:
								if uwu in data["state"][True]:
									data["day"]["wait"].pop(data["day"]["wait"].index(nick))
									data["day"]["kill"].append(uwu)
									note=f"[{uwu}]"

									if uwu==nick:
										note="你自己"

									send(f"你将写有{note}名字的纸片塞进投票箱",nick)

									time.sleep(2)
									send(f"投票箱中多了一张{roll(general[4])}的纸片")

								elif uwu in data["state"][False]:
									send(f"你没必要{roll(general[7])}死者",nick)

								else:
									data["day"]["wait"].pop(data["day"]["wait"].index(nick))
									send(f"你{roll(general[5])} 放弃了投票",nick)

									time.sleep(2)
									send(f"有一张纸片{roll(general[8])}")

							elif nick==data["now"][1] or isinstance(data["now"][1],list) and nick in data["werewolf"]["wait"]:
								if data["now"][0]==2:
									if uwu==nick:
										send(f"不允许【{card[2][0]}】选择自己",nick)

									else:
										if uwu in data["state"][True]:
											if uwu in data["prophet"]:
												send(f"你已经预言过[{uwu}]的身份了\nTA是【{card[data['core'][uwu][1]][0]}】 属于【{card[0][data['core'][uwu][2]]}】",nick)

												time.sleep(2)
												send(f"不幸的【{card[2][0]}】{roll(prophet[0])}")

											else:
												data["prophet"].append(uwu)
												send(f"[{uwu}]是【{card[data['core'][uwu][1]][0]}】 属于【{card[0][data['core'][uwu][2]]}】",nick)

												note=roll(prophet[1])

												if not data["core"][uwu][2]:
													note=roll(prophet[2])

												time.sleep(2)
												send(f"盯着水晶球的【{card[2][0]}】{note}")

										elif uwu in data["state"][False]:
											send(f"你没必要{roll(general[7])}死者",nick)

										else:
											send(f"你{roll(general[0])}今晚放弃预言 睡个好觉",nick)

											time.sleep(2)
											send(f"【{card[2][0]}】睡得很{roll(prophet[3])}")

										data["now"]=[0,None]

								elif data["now"][0]==3:
									if uwu in data["state"][True]:
										data["werewolf"]["wait"].pop(data["werewolf"]["wait"].index(nick))
										data["werewolf"]["kill"].append(uwu)

										note=f"[{uwu}]"

										if uwu==nick:
											note=f"自己 {roll(werewolf[4])}"

										elif uwu in data["werewolf"]["core"]:
											note=f"同伴[{uwu}] 这样{roll(werewolf[5])}"

										send(f"你{roll(general[0])}杀{note}",nick)

										for _ in data["werewolf"]["wait"]:
											if _==uwu:
												note="你"

											time.sleep(1)
											send(f"你的同伴[{nick}]{roll(general[0])}杀{note}",_)

									elif uwu in data["state"][False]:
										send(f"你没必要{roll(general[7])}死者",nick)

									else:
										data["werewolf"]["wait"].pop(data["werewolf"]["wait"].index(nick))
										send(f"你{roll(general[0])}今晚做件好事 放过人类",nick)

										for _ in data["werewolf"]["wait"]:
											time.sleep(1)
											send(f"你的同伴[{nick}]{roll(general[3])}了",_)

									if not data["werewolf"]["wait"]:
										note="你们意见不相同 因此没有杀人"

										if data["werewolf"]["kill"] and data["werewolf"]["kill"].count(uwu)==len(data["werewolf"]["kill"]):
											chan(uwu)
											data["werewolf"]["dead"].append(uwu)
											data["werewolf"]["kill"]=uwu

											note=f"你们杀死了[{uwu}]\nTA是【{data['core'][uwu][1]}】 属于【{data['core'][uwu][2]}】"

											if uwu in data["werewolf"]["core"]:
												note=f"你们杀死了同伴[{uwu}]"

										for _ in data["werewolf"]["core"]:
											time.sleep(1)

											if _==uwu:
												send("今晚 你被杀死了",_)

											else:
												send(f"今晚 {note}",_)

										time.sleep(2)

										if uwu in data["core"] and not data["core"][uwu][3]:
											send(f"【公告】{roll(general[2])} 只听见[{uwu}]的{roll(werewolf[0])}和几声狼嚎\n当[{roll(data['state'][True])}]跑去查看情况的时候 只发现[{uwu}]{roll(werewolf[1])}的尸体")

										else:
											send(f"能听见远处狼群{roll(werewolf[2])}的声音")

										data["now"]=[0,None]

								elif data["now"][0]==4:
									if uwu==nick:
										send(f"不允许【{card[4][0]}】自己喝下药水",nick)

									elif uwu in data["sudden"]:
										send(f"你没必要{roll(general[7])}猝死的人",nick)

									else:
										if uwu in data["witch"]["allow"]:
											state=not data["core"][uwu][3]
											note=data["witch"]["med"][state]
											send(f"你使用{potion[note[0]][0]}成功{potion[note[0]][1]}了[{uwu}]",nick)

											chan(uwu,state)
											data["witch"]["temp"]=[uwu,state]
											data["witch"]["med"][state]=[state,False,uwu]

											note=f"获得了新生"

											if not state:
												note=f"陷入了永眠"

											time.sleep(2)
											send(f"【公告】{roll(general[2])} 村子里{roll(witch[1])}\n[{roll(data['state'][True])}]挨家挨户地传话道 [{uwu}]{roll(witch[2])}地{note}")

											data["now"]=[0,None]
											
										elif uwu in data["core"]:
											send(f"你没有能给[{uwu}]使用的药",nick)

										else:
											send(f"你{roll(general[0])}今晚放弃投药 等待机会",nick)

											time.sleep(2)
											send(f"【{card[4][0]}】笑得很{roll(witch[3])}")

											data["now"]=[0,None]

							elif nick in data["state"][True]:
								send("现在不是你的场合 快去睡觉——",nick)

							elif nick in data["state"][False]:
								send("你已经死了",nick)

except Exception as quq:
	print(f"error:{quq}\n")
