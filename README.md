# Little_Wolf

**A Werewolf Bot For HackChat**  
为hack.chat量身打造的狼人杀游戏机器人

**Author(作者):**  
paperee(ee) jiangmuran(jmr) huolongguo10(Radium)

**Thanks(内测名单):**  
Maggie zzChumo xuan2wei1 4n0n4me DPG IAmLonelyWhoCanSaveMe 23  
666 Qwer xmzd DengquejieL mouse x jimmyfj MuRongPIG in9 a undefile  

## 【Linux如何快捷更新】
聊天室里输入(如有运行)：`|root close`  
终端里输入：`sudo chmod 777 updatewolf.sh`  
终端里输入：`updatewolf.sh`

## 【如何使用机器人】
安装库：`pip install -r requirements.txt`  
运行(以实际情况为准)：`python3 main.py`

## 【更新记录】
**致更新人员的版本号算法**  
- 修BUG&发现BUG 版本号不动
- 其他每条将版本号+=0.01 以此类推

### uwu.1.00｜2023.01.18｜paperee(ee)
- 完成了机器人框架

### None｜2023.01.19｜jiangmuran(jmr)
- 添加了结束游戏功能

### uwu.1.08｜2023.01.19｜paperee(ee)
- 修复了老版本的BUG(详见BUG报告)
- 优化了数据库结构
- 优化了代码结构(还是屎山)
- 修改了部分变量名(强迫症)
- 修改了女巫的阵营
- 添加了新的可操作和课变更项
- 添加了遗言功能
- 添加了自动强调功能
- 添加了自动判断消息类型

### uwu.1.10｜2023.01.20｜jiangmuran(jmr)
- 修复了老版本的BUG(详见BUG报告)
- 发现了更多BUG
- 优化了程序结构
- 补充了数据库项目

### uwu.1.12｜2023.01.21｜paperee(ee)
- 修复了老版本的BUG(详见BUG报告)
- 发现了更多BUG
- 修改了部分可操作项
- 添加了新的预设频道列表

### uwu.1.15｜2023.01.22｜jiangmuran(jmr)
- 修复了老版本的BUG(详见BUG报告)
- 发现了更多BUG
- 补充了更多词库
- 引入了读写文件想法
- 添加了debug功能
- 添加了简单的权限系统
- 添加了Linux下的一键更新

### uwu.1.19｜2023.01.23｜paperee(ee)
- 修复了老版本的BUG
- 优化了自动强调功能
- 优化了权限系统(强迫症)
- 添加了查询身份功能
- 添加了保存日志功能

### uwu.1.21｜2023.02.09｜huolongguo10(Radium)
- 修复了老版本的BUG(详见BUG报告)
- 优化了快捷更新
- 优化了异常错误显示

## 【是否解决｜已知BUG报告｜修复者】
- v｜预言家部分时候无法预测｜jiangmuran(jmr)
- v｜开始后无法停止/让村长下线｜jiangmuran(jmr)
- v｜变更牌名后部分无效｜paperee(ee)
- v｜变更牌组后无法自动开始｜paperee(ee)
- v｜结束后胜利方存活为0｜paperee(ee)
- v｜结束后女巫的用药不显示｜paperee(ee)
- v｜有时狼人的场合重复出现｜paperee(ee)
- v｜已知身份后还会显示请睁眼｜paperee(ee)
- v｜夜晚女巫的行动会保存到下一局｜paperee(ee)
- v｜卡等待时间可以重复/延时操作｜paperee(ee)
- v｜过早储存游戏起始点｜huolongguo10(Radium)

## 【是否实现｜预计加入功能｜实现者】
- x｜设置永久生效(写入文件)
- x｜机器人参与游戏(人机)
- x｜踢出玩家功能
- x｜多代理多账户发送信息｜ProxyChains
- v｜结束游戏功能｜jiangmuran(jmr)
- v｜查看数据功能(debug)｜jiangmuran(jmr)
- v｜权限系统｜jiangmuran(jmr)
- v｜遗言功能｜paperee(ee)
- v｜自动强调功能｜paperee(ee)
- v｜自动判断消息类型｜paperee(ee)
- v｜查询身份功能｜paperee(ee)
- v｜保存日志功能｜paperee(ee)

## 【是否实现｜卡牌｜阵营(True/False)｜实现者】
- v｜村民｜True｜paperee(ee)
- v｜预言家｜True｜paperee(ee)
- v｜狼人｜False｜paperee(ee)
- v｜女巫｜True｜paperee(ee)
- x｜守卫｜True
