# -*- coding: UTF-8 -*-

'''
A Werewolf Bot For HackChat
为hack.chat量身打造的狼人杀游戏机器人

Author:paperee
可以吐槽我的屎山代码 但不能对我的uwu变量名有意见(被打

Thanks:Maggie zzChumo xuan2wei1 4n0n4me jmr DPG IAmLonelyWhoCanSaveMe 23
感谢以上帮忙测试的小伙伴们

使用方法：
安装库：pip install websocket-client
运行(以实际情况为准)：python main.py

是否解决|已知BUG报告：
x|有时"【狼人】请睁眼"重复出现
x|结束后胜利方存活数显示0
x|已知身份后还会显示请睁眼
x|结束后女巫的用药不显示
'''

import websocket
import json
import time
import random
import os
import sys
import threading


# 地址:hack.chat
hc="wss://hack.chat/chat-ws"

# 频道:yc,ycl
yc="your-channel"
ycl="your-channell"
lo = "lounge"



cn=yc #选择

# bot名字
seeb=str(random.randint(1,999)).zfill(3)
botname=f"Little_Wolf_{seeb}"

# bot识别码
botpass="uwu"


# socket:ws地址,channel:频道
def main(socket,channel):

	# 主要数据库
	data={"uwu":False}

	# 初始牌组
	num=[1,1,2,3,3,4]

	# 卡牌列表
	card={0:{True:"好人",False:"坏人",None:"村长"},1:["平民","夜晚：注意旁白 安静等待\n白天：提出意见 跟随大家投票",True],2:["预言家","夜晚：选择一位村民得知身份\n白天：领导大家投票",True],3:["狼人","夜晚：选择一位村民杀死\n白天：隐藏身份 跟随大家投票",False],4:["女巫","夜晚：选择一位村民使用药水 每种药只能使用一次\n白天：隐藏身份 跟随大家投票",False]}

	# 剧情词组:通用
	general=[["选择","决定","打算","想要"],["断了气","没了动静","停了心跳","一命呜呼"],["深夜","半夜三更","凌晨两点","午夜时分"],["失去理智","愤愤不平","闹腾","愤怒"],["绿色","白色","翻折","皱巴巴","缺了角","整齐叠好","黑色","像屎一样"],["收回伸出纸片的手","不知如何抉择","有些迷茫","仔细思考"],["误入","闯入","跳进","来到"],["欺负","诅咒","戏弄","鞭尸"],["飘走了","被偷走了","被捡走了","不翼而飞"]]

	# 剧情词组:预言家
	prophet=[["犯了心肌梗塞","脑子不太清醒","撞到了头","摔了一跤"],["叹了口气","沉默不语","喃喃自语","摇了摇头"],["瞪大了双眼","惊掉了下巴","陷入沉思","不敢置信"],["熟","甜","香","舒服"],["没有回应","没有行动","家里没人","不在家中"]]

	# 剧情词组:狼人
	werewolf=[["惨叫","哀嚎","悲鸣","呜咽"],["四分五裂","难以辨认","被撕咬过","不成样"],["呼唤同伴","追赶","奔走","嬉闹"],["迷路","走丢","离群","去找对象"],["或许是想赌一把","其他狼的想法呢","其他狼赞同吗","真有心机呢"],["做可以吗","真的好吗","是在协助吗","有没有好处"],["伤心欲绝","重情重义","讲义气","悲伤"],["沉思中","略显憔悴","望向远方","不太坚定"]]

	# 剧情词组:女巫
	witch=[["自动写代码","让鱼变好吃","让人变性","压缩纸片"],["死一般的寂静","看似一派祥和","已经没有人影了","偶有远处的呼喊"],["无声","安静","静悄悄","悄无声息"],["大声","狡猾","诡异","阴森"],["想要休息","不知所踪","的纸片丢失了","的小屋无人打扫"]]

	try:
		ws=websocket.WebSocket()
		ws.connect(socket)

		time.sleep(0.5)
		ws.send(json.dumps({"cmd":"join","channel":channel,"nick":botname,"password":botpass}))

		time.sleep(0.5)
		ws.send(json.dumps({"cmd":"changecolor","color":"eee"}))

		print(f"{socket}/{channel}")
	
	except:
		time.sleep(30)
		os.execl(sys.executable,sys.executable,*sys.argv)

	# text:内容
	def send(text):
		ws.send(json.dumps({"cmd":"chat","text":str(text)}))

	while True:
		try:
			wss=json.loads(ws.recv())
		
		except:
			time.sleep(30)
			os.execl(sys.executable,sys.executable,*sys.argv)

		if "cmd" in wss:
			cmd=wss["cmd"]
		
			if cmd=="chat":
				time.sleep(1)
				nick=wss["nick"]
				text=wss["text"]

				if f"@{botname}" in text:
					send(f"/me uwu")

				elif text=="|help":
					send(f"/me >\n·\n[【狼人杀】](https://)生存\n开发者：纸片君ee(PAPEREE)\n机器人：{botname[:-4]}\n版本号：uwu.1.00\n开发进度：95%\n·\n[【手册】](https://)\n查看帮助：|help\n查看规则：|rule\n获取权限：|root\n开始生存：|uwu")


				elif text=="|rule":
					aua=str()

					if data["uwu"]:
						aua+=f"\n·\n卡牌设置({len(data['num'])}人局)：\n[【{card[1][0]}】](https://)x{data['num'].count(1)}\n[【{card[2][0]}】](https://)x{data['num'].count(2)}\n[【{card[3][0]}】](https://)x{data['num'].count(3)}\n[【{card[4][0]}】](https://)x{data['num'].count(4)}"
			
					true="".join([f"[【{card[uwu][0]}】](https://)" for uwu in card if uwu and card[uwu][-1]])
					false="".join([f"[【{card[uwu][0]}】](https://)" for uwu in card if uwu and not card[uwu][-1]])

					send(f"/me >\n·\n主要卡牌：\n{true}/[【{card[0][True]}】](https://)\n{false}/[【{card[0][False]}】](https://)\n{aua}\n·\n限制时长：\n[【{card[2][0]}】](https://)1分钟\n[【{card[3][0]}】](https://)2分钟\n[【{card[4][0]}】](https://)1分钟\n白天投票共4分钟\n·\n生存特性：\n[【{card[1][0]}】](https://)擅长推理\n[【{card[2][0]}】](https://)记性很好\n[【{card[3][0]}】](https://)杀人不受限制\n[【{card[4][0]}】](https://)不会猝死")

				elif text[:5]=="|root":
					if wss.get('trip')=="eYFDHl" or wss.get('trip')=="ejackX": # emmmm jmr do it
						if text=="|root":
							send(f"/me >\n[{nick}](https://)成功获取root权限")

							time.sleep(1)
							send(f"/w {nick} >\n·\n可变更项：\n卡牌(card) 其他(other)\n·\n详细说明：\n卡牌：牌序(1~4) 牌名(str) 阵营(bool)\n其他：正方阵营名(str) 反方阵营名(str) 村长称呼(str)")

						else:
							try:
								slices=[uwu.split(" ") for uwu in text.split("\n")]

								if slices[0][-1]=="card":
									for new in slices[1:]:
										card[int(new[0])]=[new[1],card[int(new[0])][1],True if new[2]=="True" else False]

									send(f"/me >\n变更执行成功")

								elif slices[0][-1]=="other":
									card[0]={True:slices[1][0],False:slices[1][1],None:slices[1][2]}
									send(f"/me >\n变更执行成功")

								else:
									send(f"/me >\n找不到此变更项")

							except:
								send(f"/w {nick} >\n执行时出现错误")

					else:
						send(f"/me quq")

				elif text=="|uwu":
					if data["uwu"]:
						if data.get('user'):
							send(f"/me >\n[【狼人杀】](https://)生存已经开始了")

						else:
							send(f"/me >\n[【{card[0][None]}】](https://)正在清点村里人数")

					else:
						data={"uwu":True,"owner":nick,"num":num,"time":time.time(),"round":0,"temp":[],"user":{},"sudden":[],"prophet":[],"werewolf":{"skip":False,"user":[],"wait":[],"kill":[],"dead":[]},"witch":{"med":{True:[True,True,"解药","救活"],False:[False,True,"毒药","杀死"]},"temp":[],"allow":[]},"day":{"wait":[],"kill":[],"dead":[]},"now":[]}
						send(f"/me >\n新的[【{card[0][None]}】](https://)诞生了 美好的夜晚要开始了")

						time.sleep(1)
						uvu=" ".join([str(uwu) for uwu in num])
						send(f"/w {nick} >\n·\n[【{card[0][None]}】](https://)[{nick}](https://)\n现在你可以选择改变牌组 否则为默认\n·\n卡牌详情：\n1.[【{card[1][0]}】](https://)\n2.[【{card[2][0]}】](https://)\n3.[【{card[3][0]}】](https://)\n4.[【{card[4][0]}】](https://)\n·\n默认牌组({len(num)}人局)：\n{uvu}\n·\n设置方法：\n/w {botname} 牌组")

						time.sleep(0.5)
						send(f"/me >\n[【{card[0][None]}】](https://)开始清点村里人数 请用1报数")

				elif data["uwu"]:
					if not data["user"]:
						if text=="1":
							if nick in data["temp"]:
								send(f"/me >\n[{nick}](https://)已经在花名册中了")

							else:
								data["temp"].append(nick)
								send(f"/me >\n[{nick}](https://){random.choice(general[6])}了村子 村里有{len(data['temp'])}人了")

						if len(data["temp"])==len(data["num"]):
							time.sleep(1)
							data["notice"]="@"+" @".join(data["temp"])+" "
							send(f"/me >\n{data['notice']}\n·\n人数到齐 开始抽牌 请注意查看私聊")

							random.shuffle(data["temp"])

							for uwu in data["temp"]:
								uvu=data["num"][data["temp"].index(uwu)]
								data["user"][uwu]=[uwu,card[uvu][0],card[0][card[uvu][2]],uvu,card[uvu][2],True]

								time.sleep(1)
								send(f"/w {uwu} >\n·\n你的卡牌：\n[【{card[uvu][0]}】](https://)/[【{card[0][card[uvu][2]]}】](https://)\n·\n你的任务：\n{card[uvu][1]}\n·\n获胜条件：\n[【{card[0][not card[uvu][2]]}】](https://)全员阵亡")

							time.sleep(2)
							send(f"/me >\n发牌完毕 [【狼人杀】](https://)生存正式开始")

							# nick:昵称,state:状态
							def change(nick,state=False):
								data["state"][state].append(data["state"][not state].pop(data["state"][not state].index(nick)))
								data["user"][nick][5]=state

							# 主循环
							def loop():
								while True:
									data["round"]+=1
									data["werewolf"]["skip"]=False
									data["day"]={"wait":[],"kill":[],"dead":data["day"]["dead"]}

									ava=list(data["user"].values())
									data["state"]={True:[uvu[0] for uvu in ava if uvu[5]],False:[uvu[0] for uvu in ava if not uvu[5]]}

									time.sleep(4)
									send(f"/me >\n[【回合{data['round']}】](https://)天黑请闭眼")

									print(data)

									for awa in list(data["user"].keys()):
										uwu=data["user"][awa]

										if uwu[3]==2:
											time.sleep(2)
											send(f"/me >\n[【{card[2][0]}】](https://)请睁眼")

											if uwu[5]:
												alive=[uvu for uvu in data["state"][True] if uvu!=uwu[0]]
												random.shuffle(alive)
												ovo=" ".join([f"[{uvu}](https://)" for uvu in alive])
												owo="\n".join([f"[【{data['user'][uvu][1]}】](https://)/[【{data['user'][uvu][2]}】](https://)[{data['user'][uvu][0]}](https://)" for uvu in data["prophet"]])

												data["now"]=[uwu[3],uwu[0]]

												time.sleep(1)
												send(f"/w {uwu[0]} >\n·\n[【{card[2][0]}】](https://)/[【{card[0][True]}】](https://)[{uwu[0]}](https://)\n现在你可以选择一位村民得知身份\n请在1分钟内做出选择\n·\n已知身份：\n你自己{owo}\n·\n选择方法：\n/w {botname} 对象\n·\n可选对象：\n{ovo}")

												for times in range(60):
													time.sleep(1)

													if data["now"][0]!=uwu[3]:
														break

												else:
													change(awa)
													data["sudden"].append(awa)

													time.sleep(1)
													send(f"/me >\n[【{card[2][0]}】](https://)[{awa}](https://)在今晚{random.choice(general[1])} 突然猝死")

											else:
												time.sleep(random.randint(10,50))
												send(f"/me >\n[【{card[2][0]}】](https://){random.choice(prophet[4])}")

										elif uwu[3]==3 and not data["werewolf"]["skip"]:
											time.sleep(2)
											send(f"/me >\n[【{card[3][0]}】](https://)请睁眼")

											if uwu[5]:
												alive=list(data["state"][True])
												random.shuffle(alive)
												ovo=" ".join([f"[{uvu}](https://)" for uvu in alive])

												note=[uvu for uvu in data["user"] if data["user"][uvu][3]==3 and data["user"][uvu][5]]
												data["werewolf"]={"skip":True,"user":note,"wait":note,"kill":[],"dead":data["werewolf"]["dead"]}
												data["now"]=[uwu[3],data["werewolf"]["user"]]

												for uvu in data["werewolf"]["user"]:
													time.sleep(1)
													owo=" ".join([f"[{aua}](https://)" for aua in data["werewolf"]["user"] if aua!=uvu])

													if owo:
														owo=f"\n·\n你的同伴：\n{owo}"

													send(f"/w {uvu} >\n·\n[【{card[3][0]}】](https://)/[【{card[0][False]}】](https://)[{uvu}](https://)\n现在你可以选择一位村民杀死\n狼群只有意见统一才会行动\n请在2分钟内做出选择{owo}\n·\n选择方法：\n/w {botname} 对象\n·\n可选对象：\n{ovo}")

												for times in range(120):
													time.sleep(1)

													if data["now"][0]!=uwu[3]:
														break

												else:
													for uvu in data["werewolf"]["user"]:
														if uvu not in data["werewolf"]["wait"]:
															time.sleep(1)
															send(f"/w {uvu} >\n今晚你的同伴猝死了\n{random.choice(werewolf[6])}的狼群忙于为TA送葬 没有行动")

													for uvu in data["werewolf"]["wait"]:
														change(uvu)
														data["sudden"].append(uvu)

														time.sleep(1)
														send(f"/me >\n[【{card[3][0]}】](https://)[{uvu}](https://)在今晚{random.choice(general[1])} 突然猝死")

											else:
												time.sleep(random.randint(20,40))
												send(f"/me >\n狼群中的狼{random.choice(werewolf[7])}")

										elif uwu[3]==4:
											time.sleep(2)
											send(f"/me >\n[【{card[4][0]}】](https://)请睁眼")

											if uwu[5]:
												data["witch"]={"med":data["witch"]["med"],"temp":[],"allow":[]}
												med=[uvu for uvu in data["witch"]["med"] if data["witch"]["med"][uvu][1]]

												if med:
													data["now"]=[uwu[3],uwu[0]]
													dead=[uvu for uvu in data["state"][False] if uvu not in data["sudden"]]
													alive=[uvu for uvu in data["state"][True] if uvu!=uwu[0]]

													ovo=" ".join([data["witch"]["med"][uvu][2] for uvu in med])
													owo=str()

													if dead and True in med:
														data["witch"]["allow"].extend(dead)
														random.shuffle(dead)
														owo+="\n可救："+" ".join([f"[{uvu}](https://)" for uvu in dead])

													if alive and False in med:
														data["witch"]["allow"].extend(alive)
														random.shuffle(alive)
														owo+="\n可杀："+" ".join([f"[{uvu}](https://)" for uvu in alive])

													time.sleep(1)
													send(f"/w {uwu[0]} >\n·\n[【{card[4][0]}】](https://)/[【{card[0][False]}】](https://)[{uwu[0]}](https://)\n现在你可以选择一位村民使用药水\n请在1分钟内做出选择\n·\n选择方法：\n/w {botname} 对象\n·\n所剩药水：\n{ovo}\n·\n可选对象：{owo}")

													for times in range(60):
														time.sleep(1)

														if data["now"][0]!=uwu[3]:
															break

													else:
														time.sleep(1)
														send(f"/me >\n黑夜里 只剩[【{card[4][0]}】](https://)四处飞行的身影")

												else:
													time.sleep(1)
													send(f"/w {uwu[0]} >\n·\n[【{card[4][0]}】](https://)[{uwu[0]}](https://)\n虽然轮到你行动 但你已经用完了药水")

													time.sleep(2)
													send(f"/me >\n[【{card[4][0]}】](https://)在研究能{random.choice(witch[0])}的药水")

											else:
												time.sleep(random.randint(10,50))
												send(f"/me >\n[【{card[4][0]}】](https://){random.choice(witch[4])}")


									time.sleep(4)
									send(f"/me >\n[【回合{data['round']}】](https://)天亮了")

									print(data)

									alive=list(data["state"][True])
									random.shuffle(alive)
									ovo=" ".join([f"[{uvu}](https://)" for uvu in alive])
									owo=str()

									if not data["witch"]["temp"] or data["witch"]["temp"][3]:
										owo="是一个平安夜\n"

									if isinstance(data["werewolf"]["kill"],str):
										owo=f"[{data['werewolf']['kill']}](https://)被[【{card[3][0]}】](https://)杀死了\n"

									if data["witch"]["temp"]:
										owo+=f"[{data['witch']['temp'][2]}](https://)被使用{data['witch']['temp'][0]}的[【{card[4][0]}】](https://){data['witch']['temp'][1]}了\n"

									time.sleep(2)
									send(f"/me >\n[【公告】](https://)昨晚{owo}")

									data["stats"]=[[uvu for uvu in data["user"] if data["user"][uvu][4] and data["user"][uvu][5]],[uvu for uvu in data["user"] if not data["user"][uvu][4] and data["user"][uvu][5]]]

									if not all(data["stats"]):
										break

									data["day"]={"wait":list(data["state"][True]),"kill":[],"dead":data["day"]["dead"]}
									data["now"]=[0,data["state"][True]]

									time.sleep(2)
									send(f"/me >\n·\n投票环节：\n每人一票 得票数最高的村民会被处死\n请在4分钟内做出选择\n·\n选择方法：\n/w {botname} 对象\n·\n可选对象：\n{ovo}")

									for times in range(240):
										time.sleep(1)

										if not data["day"]["wait"]:
											break

										elif times==180:
											send(f"/me >\n白天仅剩1分钟了")

									else:
										for uvu in data["day"]["wait"]:
											if data["user"][uvu][3]!=4:
												change(uvu)
												data["sudden"].append(uvu)

												time.sleep(2)
												send(f"/me >\n[【{data['user'][uvu][1]}】](https://)[{uvu}](https://)在白天{random.choice(general[1])} 突然猝死")

									if data["day"]["kill"]:
										time.sleep(2)
										aua=max(set(data["day"]["kill"]),key=data["day"]["kill"].count)

										try:
											change(aua)
											data["day"]["dead"].append(aua)
											send(f"/me >\n[【公告】](https://)投票结果统计完成\n{random.choice(general[3])}的人们处死了[{aua}](https://)")

										except:
											send(f"/me >\n[【公告】](https://)投票结果统计完成\n{random.choice(general[3])}的人们{random.choice(general[0])}处死[{aua}](https://)\n但当发现时 [{aua}](https://)已经猝死在家中了")

										alive=list(data["state"][True])
										random.shuffle(alive)
										ovo=" ".join([f"[{uvu}](https://)" for uvu in alive])

										time.sleep(2)
										send(f"/me >\n目前留在村子里的人有：\n{ovo}")

									data["stats"]=[[uvu for uvu in data["user"] if data["user"][uvu][4] and data["user"][uvu][5]],[uvu for uvu in data["user"] if not data["user"][uvu][4] and data["user"][uvu][5]]]
				
									if not all(data["stats"]):
										break

								time.sleep(4)
								winner=data["stats"].index([])

								uwu=[eb for eb in data["user"] if data["user"][eb][4]==winner and not data["user"][eb][5]]
								uvu=[eb for eb in data["user"] if data["user"][eb][4]==(not winner)]
								awa=" ".join([eb for eb in data["prophet"]])
								ava=" ".join([eb for eb in data["werewolf"]["dead"]])
								aua=" ".join([eb for eb in data["day"]["dead"]])
								quq="".join([f"\n[【{card[4][0]}】](https://){data['witch']['med'][eb][3]}了：{data['witch']['med'][eb][-1]}" for eb in data["witch"]["med"] if not data["witch"]["med"][eb][1]])
								ovo=" ".join(uvu)
								owo=" ".join(data['stats'][not int(winner)])
								ouo=str()
								note=str()

								if winner:
									send(f"/me >\n大家清楚地感受到 邪恶从村子里消失了")

								else:
									send(f"/me >\n这个村子正在发生异变\n血色笼罩村庄 时不时传来邪恶的声音")

								if uwu:
									uwu=f"\n死亡({len(uwu)})："+" ".join(uwu)

								else:
									uwu=str()

								if ovo:
									ouo=f"\n死亡({len(uvu)})：{ovo}"

								if awa:
									note+=f"\n[【{card[2][0]}】](https://)知道了：{awa}"

								if ava:
									note+=f"\n[【{card[3][0]}】](https://)杀死了：{ava}"

								if aua:
									note+=f"\n投票处死了：{aua}"

								if note:
									note=f"\n·\n特殊数据：{note}"

								time.sleep(2)
								send(f"/me >\n[【{card[0][not winner]}】](https://)阵亡 [【{card[0][winner]}】](https://)胜利")

								minutes=divmod(round(time.time()-data["time"]),60)
								send(f"/me >\n·\n[【统计】](https://)\n时长：{minutes[0]}分钟 {minutes[1]}秒\n回合数：{data['round']}\n·\n[【{card[0][winner]}】](https://)(胜)\n存活({len(data['stats'][winner])})：{owo}{uwu}\n·\n[【{card[0][not winner]}】](https://)(败){ouo}{note}")

								time.sleep(1)
								send(f"/me >\n本局结束 撒花-")

								data.clear()
								data["uwu"]=False

								sys.exit(0)

							# 开启多线程
							threading.Thread(target=loop).start()

			elif cmd=="info" and wss.get('type')=="whisper":
				time.sleep(1)

				if "from" in wss:
					nick=str(wss["from"])
					text=wss["text"]
					uwu=text[text.find(':')+2:]

					if data["uwu"]:
						if not data["user"]:
							if nick==data["owner"]:
								allow=[int(uwu) for uwu in uwu.split(' ') if uwu in ["1","2","3","4"]]

								if allow==data["num"]:
									send(f"/w {nick} >\n牌组和原先相同 不变更")

								elif len(allow)<4:
									send(f"/w {nick} >\n设定的有效牌至少要有4张")

								elif len(allow)<=len(data["temp"]):
									send(f"/w {nick} >\n花名册的人数已经达到/超过牌数了")

								else:
									data["num"]=sorted(allow)
									send(f"/me >\n[【{card[0][None]}】](https://)更改了村民身份牌数目")

									time.sleep(1)
									send(f"/me >\n现卡牌设置({len(allow)}人局)：\n1.[【{card[1][0]}】](https://)x{allow.count(1)}\n2.[【{card[2][0]}】](https://)x{allow.count(2)}\n3.[【{card[3][0]}】](https://)x{allow.count(3)}\n4.[【{card[4][0]}】](https://)x{allow.count(4)}")

						elif data["now"]:
							if nick in data["day"]["wait"]:
								if uwu in data["state"][True]:
									del data["day"]["wait"][data["day"]["wait"].index(nick)]
									data["day"]["kill"].append(uwu)
									aua=f"[{uwu}](https://)"

									if uwu==nick:
										aua="你自己"

									send(f"/w {nick} >\n你将写有{aua}名字的纸片塞进投票箱")

									time.sleep(2)
									send(f"/me >\n投票箱中多了一张{random.choice(general[4])}的纸片")

								elif uwu in data["state"][False]:
									send(f"/w {nick} >\n你没必要{random.choice(general[7])}死者")

								else:
									del data["day"]["wait"][data["day"]["wait"].index(nick)]
									send(f"/w {nick} >\n你{random.choice(general[5])} 放弃了投票")

									time.sleep(2)
									send(f"/me >\n有一张纸片{random.choice(general[8])}")

							elif nick==data["now"][1] or isinstance(data["now"][1],list) and nick in data["werewolf"]["wait"]:
								if data["now"][0]==2:
									if uwu==nick:
										send(f"/w {nick} >\n不允许[【{card[2][0]}】](https://)选择自己")

									else:
										if uwu in data["state"][True]:
											if uwu in data["prophet"]:
												send(f"/w {nick} >\n你已经预言过[{uwu}](https://)的身份了\nTA是[【{data['user'][uwu][1]}】](https://) 属于[【{data['user'][uwu][2]}】](https://)")

												time.sleep(2)
												send(f"/me >\n不幸的[【{card[2][0]}】](https://){random.choice(prophet[0])}")

											else:
												data["prophet"].append(uwu)
												send(f"/w {nick} >\n[{uwu}](https://)是[【{data['user'][uwu][1]}】](https://) 属于[【{data['user'][uwu][2]}】](https://)")

												aua=random.choice(prophet[1])

												if not data['user'][uwu][4]:
													aua=random.choice(prophet[2])

												time.sleep(2)
												send(f"/me >\n盯着水晶球的[【{card[2][0]}】](https://){aua}")

										elif uwu in data["state"][False]:
											send(f"/w {nick} >\n你没必要{random.choice(general[7])}死者")

										else:
											send(f"/w {nick} >\n你{random.choice(general[0])}今晚放弃预言 睡个好觉")

											time.sleep(2)
											send(f"/me >\n[【{card[2][0]}】](https://)睡得很{random.choice(prophet[3])}")

										data["now"]=[0,None]

								elif data["now"][0]==3:
									if uwu in data["state"][True]:
										del data["werewolf"]["wait"][data["werewolf"]["wait"].index(nick)]
										data["werewolf"]["kill"].append(uwu)

										aua=f"[{uwu}](https://)"

										if uwu==nick:
											aua=f"自己 {random.choice(werewolf[4])}"

										elif uwu in data["werewolf"]["user"]:
											aua=f"同伴[{uwu}](https://) 这样{random.choice(werewolf[5])}"

										send(f"/w {nick} >\n你{random.choice(general[0])}杀{aua}")

										for uvu in data["werewolf"]["wait"]:
											if uvu==uwu:
												aua="你"

											time.sleep(1)
											send(f"/w {uvu} >\n你的同伴[{nick}](https://){random.choice(general[0])}杀{aua}")

									elif uwu in data["state"][False]:
										send(f"/w {nick} >\n你没必要{random.choice(general[7])}死者")

									else:
										del data["werewolf"]["wait"][data["werewolf"]["wait"].index(nick)]
										send(f"/w {nick} >\n你{random.choice(general[0])}今晚做件好事 放过人类")

										for uvu in data["werewolf"]["wait"]:
											time.sleep(1)
											send(f"/w {uvu} >\n你的同伴[{nick}](https://){random.choice(general[3])}了")

									if not data["werewolf"]["wait"]:
										aua="你们意见不相同 因此没有杀人"

										if data["werewolf"]["kill"] and data["werewolf"]["kill"].count(uwu)==len(data["werewolf"]["kill"]):
											change(uwu)
											data["werewolf"]["dead"].append(uwu)
											data["werewolf"]["kill"]=uwu

											aua=f"你们杀死了[{uwu}](https://)\nTA是[【{data['user'][uwu][1]}】](https://) 属于[【{data['user'][uwu][2]}】](https://)"

											if uwu in data["werewolf"]["user"]:
												aua=f"你们杀死了同伴[{uwu}](https://)"

										for uvu in data["werewolf"]["user"]:
											time.sleep(1)

											if uvu==uwu:
												send(f"/w {uvu} >\n今晚 你被杀死了")

											else:
												send(f"/w {uvu} >\n今晚 {aua}")

										time.sleep(2)

										if uwu in data["user"] and not data["user"][uwu][5]:
											send(f"/me >\n[【公告】](https://){random.choice(general[2])} 只听见[{uwu}](https://)的{random.choice(werewolf[0])}和几声狼嚎\n当[{random.choice(data['state'][True])}](https://)跑去查看情况的时候 只发现[{uwu}](https://){random.choice(werewolf[1])}的尸体")

										else:
											send(f"/me >\n能听见远处狼群{random.choice(werewolf[2])}的声音")

										data["now"]=[0,None]

								elif data["now"][0]==4:
									if uwu==nick:
										send(f"/w {nick} >\n不允许[【{card[4][0]}】](https://)自己喝下药水")

									elif uwu in data["sudden"]:
										send(f"/w {nick} >\n你没必要{random.choice(general[7])}猝死的人")

									else:
										if uwu in data["witch"]["allow"]:
											state=not data["user"][uwu][5]
											uvu=data["witch"]["med"][state]
											send(f"/w {nick} >\n你使用{uvu[2]}成功{uvu[3]}了[{uwu}](https://)")

											change(uwu,state)
											data["witch"]["temp"]=[uvu[2],uvu[3],uwu,state]
											data["witch"]["med"][state][1]=False

											aua=f"获得了新生"

											if not state:
												aua=f"陷入了永眠"

											time.sleep(2)
											send(f"/me >\n[【公告】](https://){random.choice(general[2])} 村子里{random.choice(witch[1])}\n[{random.choice(data['state'][True])}](https://)挨家挨户地传话道 [{uwu}](https://){random.choice(witch[2])}地{aua}")

											data["now"]=[0,None]
											
										elif uwu in data["user"]:
											send(f"/w {nick} >\n你没有能给[{uwu}](https://)使用的药")

										else:
											send(f"/w {nick} >\n你{random.choice(general[0])}今晚放弃投药 等待机会")

											time.sleep(2)
											send(f"/me >\n[【{card[4][0]}】](https://)笑得很{random.choice(witch[3])}")
											data["now"]=[0,None]

							elif nick in data["state"][True]:
								send(f"/w {nick} >\n现在不是你的场合 快去睡觉——")

							elif nick in data["state"][False]:
								send(f"/w {nick} >\n你已经死了")


# 开启多线程
threading.Thread(target=main,args=(hc,cn,)).start()
