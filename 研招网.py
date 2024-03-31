import requests
from bs4 import BeautifulSoup
import time
import pymysql
from requests.exceptions import ConnectionError

connection = pymysql.connect(
    host='localhost',  # 主机名或者 IP 地址
    port=3306,  # 端口号
    user='root',
    password='123456',
    database='unvircity',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 定义查询参数范围
ssdm_range = [
    {
        "mc": "北京市",
        "dm": "11"
    },
    {
        "mc": "天津市",
        "dm": "12"
    },
    {
        "mc": "河北省",
        "dm": "13"
    },
    {
        "mc": "山西省",
        "dm": "14"
    },
    {
        "mc": "内蒙古自治区",
        "dm": "15"
    },
    {
        "mc": "辽宁省",
        "dm": "21"
    },
    {
        "mc": "吉林省",
        "dm": "22"
    },
    {
        "mc": "黑龙江省",
        "dm": "23"
    },
    {
        "mc": "上海市",
        "dm": "31"
    },
    {
        "mc": "江苏省",
        "dm": "32"
    },
    {
        "mc": "浙江省",
        "dm": "33"
    },
    {
        "mc": "安徽省",
        "dm": "34"
    },
    {
        "mc": "福建省",
        "dm": "35"
    },
    {
        "mc": "江西省",
        "dm": "36"
    },
    {
        "mc": "山东省",
        "dm": "37"
    },
    {
        "mc": "河南省",
        "dm": "41"
    },
    {
        "mc": "湖北省",
        "dm": "42"
    },
    {
        "mc": "湖南省",
        "dm": "43"
    },
    {
        "mc": "广东省",
        "dm": "44"
    },
    {
        "mc": "广西壮族自治区",
        "dm": "45"
    },
    {
        "mc": "海南省",
        "dm": "46"
    },
    {
        "mc": "重庆市",
        "dm": "50"
    },
    {
        "mc": "四川省",
        "dm": "51"
    },
    {
        "mc": "贵州省",
        "dm": "52"
    },
    {
        "mc": "云南省",
        "dm": "53"
    },
    {
        "mc": "西藏自治区",
        "dm": "54"
    },
    {
        "mc": "陕西省",
        "dm": "61"
    },
    {
        "mc": "甘肃省",
        "dm": "62"
    },
    {
        "mc": "青海省",
        "dm": "63"
    },
    {
        "mc": "宁夏回族自治区",
        "dm": "64"
    },
    {
        "mc": "新疆维吾尔自治区",
        "dm": "65"
    }
]
dwmc_value = ''
zymc_value = ''
xxfs_value = '1'
yjxkdm_range = [
    {
        "mc": "哲学",
        "dm": "0101"
    },
    {
        "mc": "应用伦理",
        "dm": "0151"
    },
    {
        "mc": "理论经济学",
        "dm": "0201"
    },
    {
        "mc": "应用经济学",
        "dm": "0202"
    },
    {
        "mc": "金融",
        "dm": "0251"
    },
    {
        "mc": "应用统计",
        "dm": "0252"
    },
    {
        "mc": "税务",
        "dm": "0253"
    },
    {
        "mc": "国际商务",
        "dm": "0254"
    },
    {
        "mc": "保险",
        "dm": "0255"
    },
    {
        "mc": "资产评估",
        "dm": "0256"
    },
    {
        "mc": "数字经济",
        "dm": "0258"
    },
    {
        "mc": "统计学",
        "dm": "0270"
    },
    {
        "mc": "区域国别学",
        "dm": "0271"
    },
    {
        "mc": "法学",
        "dm": "0301"
    },
    {
        "mc": "政治学",
        "dm": "0302"
    },
    {
        "mc": "社会学",
        "dm": "0303"
    },
    {
        "mc": "民族学",
        "dm": "0304"
    },
    {
        "mc": "马克思主义理论",
        "dm": "0305"
    },
    {
        "mc": "公安学",
        "dm": "0306"
    },
    {
        "mc": "中共党史党建学",
        "dm": "0307"
    },
    {
        "mc": "纪检监察学",
        "dm": "0308"
    },
    {
        "mc": "法律",
        "dm": "0351"
    },
    {
        "mc": "社会工作",
        "dm": "0352"
    },
    {
        "mc": "警务",
        "dm": "0353"
    },
    {
        "mc": "知识产权",
        "dm": "0354"
    },
    {
        "mc": "国际事务",
        "dm": "0355"
    },
    {
        "mc": "国家安全学",
        "dm": "0370"
    },
    {
        "mc": "区域国别学",
        "dm": "0371"
    },
    {
        "mc": "教育学",
        "dm": "0401"
    },
    {
        "mc": "心理学",
        "dm": "0402"
    },
    {
        "mc": "体育学",
        "dm": "0403"
    },
    {
        "mc": "教育",
        "dm": "0451"
    },
    {
        "mc": "体育",
        "dm": "0452"
    },
    {
        "mc": "国际中文教育",
        "dm": "0453"
    },
    {
        "mc": "应用心理",
        "dm": "0454"
    },
    {
        "mc": "",
        "dm": "0471"
    },
    {
        "mc": "中国语言文学",
        "dm": "0501"
    },
    {
        "mc": "外国语言文学",
        "dm": "0502"
    },
    {
        "mc": "新闻传播学",
        "dm": "0503"
    },
    {
        "mc": "翻译",
        "dm": "0551"
    },
    {
        "mc": "新闻与传播",
        "dm": "0552"
    },
    {
        "mc": "出版",
        "dm": "0553"
    },
    {
        "mc": "区域国别学",
        "dm": "0570"
    },
    {
        "mc": "考古学",
        "dm": "0601"
    },
    {
        "mc": "中国史",
        "dm": "0602"
    },
    {
        "mc": "世界史",
        "dm": "0603"
    },
    {
        "mc": "博物馆",
        "dm": "0651"
    },
    {
        "mc": "区域国别学",
        "dm": "0670"
    },
    {
        "mc": "数学",
        "dm": "0701"
    },
    {
        "mc": "物理学",
        "dm": "0702"
    },
    {
        "mc": "化学",
        "dm": "0703"
    },
    {
        "mc": "天文学",
        "dm": "0704"
    },
    {
        "mc": "地理学",
        "dm": "0705"
    },
    {
        "mc": "大气科学",
        "dm": "0706"
    },
    {
        "mc": "海洋科学",
        "dm": "0707"
    },
    {
        "mc": "地球物理学",
        "dm": "0708"
    },
    {
        "mc": "地质学",
        "dm": "0709"
    },
    {
        "mc": "生物学",
        "dm": "0710"
    },
    {
        "mc": "系统科学",
        "dm": "0711"
    },
    {
        "mc": "科学技术史",
        "dm": "0712"
    },
    {
        "mc": "生态学",
        "dm": "0713"
    },
    {
        "mc": "统计学",
        "dm": "0714"
    },
    {
        "mc": "气象",
        "dm": "0751"
    },
    {
        "mc": "集成电路科学与工程",
        "dm": "0770"
    },
    {
        "mc": "心理学",
        "dm": "0771"
    },
    {
        "mc": "力学",
        "dm": "0772"
    },
    {
        "mc": "材料科学与工程",
        "dm": "0773"
    },
    {
        "mc": "电子科学与技术",
        "dm": "0774"
    },
    {
        "mc": "计算机科学与技术",
        "dm": "0775"
    },
    {
        "mc": "环境科学与工程",
        "dm": "0776"
    },
    {
        "mc": "生物医学工程",
        "dm": "0777"
    },
    {
        "mc": "基础医学",
        "dm": "0778"
    },
    {
        "mc": "公共卫生与预防医学",
        "dm": "0779"
    },
    {
        "mc": "药学",
        "dm": "0780"
    },
    {
        "mc": "中药学",
        "dm": "0781"
    },
    {
        "mc": "护理学",
        "dm": "0783"
    },
    {
        "mc": "",
        "dm": "0784"
    },
    {
        "mc": "",
        "dm": "0785"
    },
    {
        "mc": "",
        "dm": "0786"
    },
    {
        "mc": "遥感科学与技术",
        "dm": "0787"
    },
    {
        "mc": "智能科学与技术",
        "dm": "0788"
    },
    {
        "mc": "纳米科学与工程",
        "dm": "0789"
    },
    {
        "mc": "力学",
        "dm": "0801"
    },
    {
        "mc": "机械工程",
        "dm": "0802"
    },
    {
        "mc": "光学工程",
        "dm": "0803"
    },
    {
        "mc": "仪器科学与技术",
        "dm": "0804"
    },
    {
        "mc": "材料科学与工程",
        "dm": "0805"
    },
    {
        "mc": "冶金工程",
        "dm": "0806"
    },
    {
        "mc": "动力工程及工程热物理",
        "dm": "0807"
    },
    {
        "mc": "电气工程",
        "dm": "0808"
    },
    {
        "mc": "电子科学与技术",
        "dm": "0809"
    },
    {
        "mc": "信息与通信工程",
        "dm": "0810"
    },
    {
        "mc": "控制科学与工程",
        "dm": "0811"
    },
    {
        "mc": "计算机科学与技术",
        "dm": "0812"
    },
    {
        "mc": "建筑学",
        "dm": "0813"
    },
    {
        "mc": "土木工程",
        "dm": "0814"
    },
    {
        "mc": "水利工程",
        "dm": "0815"
    },
    {
        "mc": "测绘科学与技术",
        "dm": "0816"
    },
    {
        "mc": "化学工程与技术",
        "dm": "0817"
    },
    {
        "mc": "地质资源与地质工程",
        "dm": "0818"
    },
    {
        "mc": "矿业工程",
        "dm": "0819"
    },
    {
        "mc": "石油与天然气工程",
        "dm": "0820"
    },
    {
        "mc": "纺织科学与工程",
        "dm": "0821"
    },
    {
        "mc": "轻工技术与工程",
        "dm": "0822"
    },
    {
        "mc": "交通运输工程",
        "dm": "0823"
    },
    {
        "mc": "船舶与海洋工程",
        "dm": "0824"
    },
    {
        "mc": "航空宇航科学与技术",
        "dm": "0825"
    },
    {
        "mc": "兵器科学与技术",
        "dm": "0826"
    },
    {
        "mc": "核科学与技术",
        "dm": "0827"
    },
    {
        "mc": "农业工程",
        "dm": "0828"
    },
    {
        "mc": "林业工程",
        "dm": "0829"
    },
    {
        "mc": "环境科学与工程",
        "dm": "0830"
    },
    {
        "mc": "生物医学工程",
        "dm": "0831"
    },
    {
        "mc": "食品科学与工程",
        "dm": "0832"
    },
    {
        "mc": "城乡规划学",
        "dm": "0833"
    },
    {
        "mc": "软件工程",
        "dm": "0835"
    },
    {
        "mc": "生物工程",
        "dm": "0836"
    },
    {
        "mc": "安全科学与工程",
        "dm": "0837"
    },
    {
        "mc": "公安技术",
        "dm": "0838"
    },
    {
        "mc": "网络空间安全",
        "dm": "0839"
    },
    {
        "mc": "建筑",
        "dm": "0851"
    },
    {
        "mc": "城乡规划",
        "dm": "0853"
    },
    {
        "mc": "电子信息",
        "dm": "0854"
    },
    {
        "mc": "机械",
        "dm": "0855"
    },
    {
        "mc": "材料与化工",
        "dm": "0856"
    },
    {
        "mc": "资源与环境",
        "dm": "0857"
    },
    {
        "mc": "能源动力",
        "dm": "0858"
    },
    {
        "mc": "土木水利",
        "dm": "0859"
    },
    {
        "mc": "生物与医药",
        "dm": "0860"
    },
    {
        "mc": "交通运输",
        "dm": "0861"
    },
    {
        "mc": "风景园林",
        "dm": "0862"
    },
    {
        "mc": "科学技术史",
        "dm": "0870"
    },
    {
        "mc": "管理科学与工程",
        "dm": "0871"
    },
    {
        "mc": "设计学",
        "dm": "0872"
    },
    {
        "mc": "集成电路科学与工程",
        "dm": "0873"
    },
    {
        "mc": "国家安全学",
        "dm": "0874"
    },
    {
        "mc": "遥感科学与技术",
        "dm": "0875"
    },
    {
        "mc": "智能科学与技术",
        "dm": "0876"
    },
    {
        "mc": "纳米科学与工程",
        "dm": "0877"
    },
    {
        "mc": "作物学",
        "dm": "0901"
    },
    {
        "mc": "园艺学",
        "dm": "0902"
    },
    {
        "mc": "农业资源与环境",
        "dm": "0903"
    },
    {
        "mc": "植物保护",
        "dm": "0904"
    },
    {
        "mc": "畜牧学",
        "dm": "0905"
    },
    {
        "mc": "兽医学",
        "dm": "0906"
    },
    {
        "mc": "林学",
        "dm": "0907"
    },
    {
        "mc": "水产",
        "dm": "0908"
    },
    {
        "mc": "草学",
        "dm": "0909"
    },
    {
        "mc": "水土保持与荒漠化防治学",
        "dm": "0910"
    },
    {
        "mc": "农业",
        "dm": "0951"
    },
    {
        "mc": "兽医",
        "dm": "0952"
    },
    {
        "mc": "林业",
        "dm": "0954"
    },
    {
        "mc": "食品与营养",
        "dm": "0955"
    },
    {
        "mc": "科学技术史",
        "dm": "0970"
    },
    {
        "mc": "环境科学与工程",
        "dm": "0971"
    },
    {
        "mc": "食品科学与工程",
        "dm": "0972"
    },
    {
        "mc": "基础医学",
        "dm": "1001"
    },
    {
        "mc": "临床医学",
        "dm": "1002"
    },
    {
        "mc": "口腔医学",
        "dm": "1003"
    },
    {
        "mc": "公共卫生与预防医学",
        "dm": "1004"
    },
    {
        "mc": "中医学",
        "dm": "1005"
    },
    {
        "mc": "中西医结合",
        "dm": "1006"
    },
    {
        "mc": "药学",
        "dm": "1007"
    },
    {
        "mc": "中药学",
        "dm": "1008"
    },
    {
        "mc": "特种医学",
        "dm": "1009"
    },
    {
        "mc": "护理学",
        "dm": "1011"
    },
    {
        "mc": "法医学",
        "dm": "1012"
    },
    {
        "mc": "临床医学",
        "dm": "1051"
    },
    {
        "mc": "口腔医学",
        "dm": "1052"
    },
    {
        "mc": "公共卫生",
        "dm": "1053"
    },
    {
        "mc": "护理",
        "dm": "1054"
    },
    {
        "mc": "药学",
        "dm": "1055"
    },
    {
        "mc": "中药",
        "dm": "1056"
    },
    {
        "mc": "中医",
        "dm": "1057"
    },
    {
        "mc": "医学技术",
        "dm": "1058"
    },
    {
        "mc": "针灸",
        "dm": "1059"
    },
    {
        "mc": "科学技术史",
        "dm": "1071"
    },
    {
        "mc": "生物医学工程",
        "dm": "1072"
    },
    {
        "mc": "",
        "dm": "1073"
    },
    {
        "mc": "",
        "dm": "1074"
    },
    {
        "mc": "军事思想与军事历史",
        "dm": "1101"
    },
    {
        "mc": "战略学",
        "dm": "1102"
    },
    {
        "mc": "联合作战学",
        "dm": "1103"
    },
    {
        "mc": "军兵种作战学",
        "dm": "1104"
    },
    {
        "mc": "军队指挥学",
        "dm": "1105"
    },
    {
        "mc": "军队政治工作学",
        "dm": "1106"
    },
    {
        "mc": "军事后勤学",
        "dm": "1107"
    },
    {
        "mc": "军事装备学",
        "dm": "1108"
    },
    {
        "mc": "军事管理学",
        "dm": "1109"
    },
    {
        "mc": "军事训练学",
        "dm": "1110"
    },
    {
        "mc": "军事智能",
        "dm": "1111"
    },
    {
        "mc": "联合作战指挥",
        "dm": "1152"
    },
    {
        "mc": "军兵种作战指挥",
        "dm": "1153"
    },
    {
        "mc": "作战指挥保障",
        "dm": "1154"
    },
    {
        "mc": "战时政治工作",
        "dm": "1155"
    },
    {
        "mc": "后勤与装备保障",
        "dm": "1156"
    },
    {
        "mc": "军事训练与管理",
        "dm": "1157"
    },
    {
        "mc": "国家安全学",
        "dm": "1170"
    },
    {
        "mc": "管理科学与工程",
        "dm": "1201"
    },
    {
        "mc": "工商管理学",
        "dm": "1202"
    },
    {
        "mc": "农林经济管理",
        "dm": "1203"
    },
    {
        "mc": "公共管理学",
        "dm": "1204"
    },
    {
        "mc": "信息资源管理",
        "dm": "1205"
    },
    {
        "mc": "工商管理",
        "dm": "1251"
    },
    {
        "mc": "公共管理",
        "dm": "1252"
    },
    {
        "mc": "会计",
        "dm": "1253"
    },
    {
        "mc": "旅游管理",
        "dm": "1254"
    },
    {
        "mc": "图书情报",
        "dm": "1255"
    },
    {
        "mc": "工程管理",
        "dm": "1256"
    },
    {
        "mc": "审计",
        "dm": "1257"
    },
    {
        "mc": "安全科学与工程",
        "dm": "1270"
    },
    {
        "mc": "国家安全学",
        "dm": "1271"
    },
    {
        "mc": "艺术学",
        "dm": "1301"
    },
    {
        "mc": "音乐与舞蹈学",
        "dm": "1302"
    },
    {
        "mc": "戏剧与影视学",
        "dm": "1303"
    },
    {
        "mc": "设计学",
        "dm": "1305"
    },
    {
        "mc": "音乐",
        "dm": "1352"
    },
    {
        "mc": "舞蹈",
        "dm": "1353"
    },
    {
        "mc": "戏剧与影视",
        "dm": "1354"
    },
    {
        "mc": "戏曲与曲艺",
        "dm": "1355"
    },
    {
        "mc": "美术与书法",
        "dm": "1356"
    },
    {
        "mc": "设计",
        "dm": "1357"
    },
    {
        "mc": "设计学",
        "dm": "1370"
    },
    {
        "mc": "集成电路科学与工程",
        "dm": "1401"
    },
    {
        "mc": "国家安全学",
        "dm": "1402"
    },
    {
        "mc": "设计学",
        "dm": "1403"
    },
    {
        "mc": "遥感科学与技术",
        "dm": "1404"
    },
    {
        "mc": "智能科学与技术",
        "dm": "1405"
    },
    {
        "mc": "纳米科学与工程",
        "dm": "1406"
    },
    {
        "mc": "区域国别学",
        "dm": "1407"
    },
    {
        "mc": "文物",
        "dm": "1451"
    },
    {
        "mc": "密码",
        "dm": "1452"
    }
]

retry_count = 10  # 设置重试次数

# 发送POST请求并打印表格数据
for ssdm in ssdm_range:
    for yjxkdm in yjxkdm_range:
        ssdm_value = ssdm['dm']
        yjxkdm_value = yjxkdm['dm']
        mldm_value = yjxkdm_value[:2]  # 取yjxkdm的前两位数字
        # 定义查询参数
        payload = {
            'ssdm': ssdm_value,
            'dwmc': dwmc_value,
            'mldm': mldm_value,
            'mlmc': '',
            'yjxkdm': yjxkdm_value,
            'zymc': '',
            'xxfs': xxfs_value
        }
        try:
            print(ssdm['mc'] + yjxkdm['mc'])
            # 发送POST请求
            response = requests.post('https://yz.chsi.com.cn/zsml/queryAction.do', data=payload)
            response.raise_for_status()  # 检查请求是否成功
            # 解析HTML文档
            soup = BeautifulSoup(response.text, 'html.parser')
            # 提取所有表格
            tables = soup.find_all('table')
            # 遍历表格并打印内容
            for table in tables:
                # 提取表格中的所有行
                rows = table.find_all('tr')
                # 跳过第一行（表头）
                for row in rows[1:]:
                    # 提取行中的所有单元格
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.text.strip() for cell in cells]
                    # 提取第一列的字符串并去掉前七个字符
                    dwmc_value2 = row_data[0][7:]
                    # 构造GET请求的URL，并包含动态生成的查询参数
                    url = f'https://yz.chsi.com.cn/zsml/querySchAction.do?ssdm={ssdm_value}&dwmc={dwmc_value2}&mldm={mldm_value}&mlmc=&yjxkdm={yjxkdm_value}&xxfs={xxfs_value}&zymc='
                    try:
                        # 发送新的GET请求
                        response_dwmc = requests.get(url)
                        response_dwmc.raise_for_status()  # 检查请求是否成功
                        # 解析响应的HTML文档
                        soup_dwmc = BeautifulSoup(response_dwmc.text, 'html.parser')
                        # 提取并打印表格数据
                        tables_dwmc = soup_dwmc.find_all('table')
                        for table_dwmc in tables_dwmc:
                            rows_dwmc = table_dwmc.find_all('tr')
                            data = []
                            for row_dwmc in rows_dwmc:
                                cells_dwmc = row_dwmc.find_all(['td', 'th'])
                                row_data_dwmc = [cell.text.strip() for cell in cells_dwmc]
                                data.extend(row_data_dwmc)
                                # 提取链接标签并获取链接
                                link = row_dwmc.find('a')
                                if link:
                                    link_url = 'https://yz.chsi.com.cn' + link['href']
                                    time.sleep(0.01)
                                    try:
                                        # 发送第三次GET请求
                                        response_third = requests.get(link_url)
                                        response_third.raise_for_status()  # 检查请求是否成功
                                        # 解析第三次响应的HTML文档
                                        soup_third = BeautifulSoup(response_third.text, 'html.parser')
                                        # 提取表格数据
                                        tables_third = soup_third.find_all('table')
                                        cell_texts = []  # 创建空列表用于存储数据
                                        for table_third in tables_third:
                                            rows_third = table_third.find_all('tr')
                                            for row_third in rows_third:
                                                cells_third = row_third.find_all(['td', 'th'])
                                                for cell in cells_third:
                                                    cell_texts.append(cell.text.strip())  # 将 cell.text 添加到列表中
                                        # 将数据插入MySQL数据库

                                        with connection.cursor() as cursor:
                                            sql = """
                                            INSERT INTO yzw (省市, 学科分类, 招生单位, 考试方式, 院系所, 专业, 学习方式, 研究方向, 指导老师, 拟招人数, 备注, 科目一, 科目二, 科目三, 科目四)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                            """
                                            cursor.execute(sql, (
                                                ssdm['mc'], yjxkdm['mc'], cell_texts[1], cell_texts[3],
                                                cell_texts[5], cell_texts[7], cell_texts[9], cell_texts[11],
                                                cell_texts[13], cell_texts[15], cell_texts[18], cell_texts[23],
                                                cell_texts[24], cell_texts[25], cell_texts[26]
                                            ))
                                        connection.commit()
                                        print(ssdm['mc'], yjxkdm['mc'], cell_texts[1], cell_texts[3],
                                              cell_texts[5], cell_texts[7], cell_texts[9], cell_texts[11],
                                              cell_texts[13], cell_texts[15], cell_texts[18], cell_texts[23],
                                              cell_texts[24], cell_texts[25], cell_texts[26])
                                    except ConnectionError as e:
                                        print(f"第三次请求出错：{e}")
                                        continue  # 继续下一次循环
                    except ConnectionError as e:
                        print(f"第二次请求出错：{e}")
                        continue  # 继续下一次循环
        except ConnectionError as e:
            print(f"第一次请求出错：{e}")
            continue  # 继续下一次循环

# 关闭MySQL连接
connection.close()
# 输入任意键继续
input("等一下")
