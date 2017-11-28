# -*-coding:utf-8-*-


# 验证是否为有效身份证
def id_number_isvalid(card_id):
    # 转为字符串，防止传入int类型数据不能通过下标截取
    card_id = str(card_id)
    # 判断输入的身份证号是否规范（总长18位且前17位都是数字）
    if not (len(card_id) == 18 and card_id[:17].isdigit()):
        return False

    province = {"11": u"北京", "12": u"天津", "13": u"河北", "14": u"山西", "15": u"内蒙古", "21": u"辽宁", "22": u"吉林",
                "23": u"黑龙江", "31": u"上海", "32": u"江苏", "33": u"浙江", "34": u"安徽", "35": u"福建", "36": u"江西", "37": u"山东",
                "41": u"河南", "42": u"湖北", "43": u"湖南", "44": u"广东", "45": u"广西", "46": u"海南", "50": u"重庆", "51": u"四川",
                "52": u"贵州", "53": u"云南", "54": u"西藏", "61": u"陕西", "62": u"甘肃", "63": u"青海", "64": u"宁夏", "65": u"新疆",
                "71": u"台湾", "81": u"香港", "82": u"澳门", "91": u"国外"}
    key = card_id[:2]
    if key not in province:
        return False
    # 身份证前17位对应的加权值
    w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

    # 身份证最后一位计算出的校验值
    check_bit = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    result = 0
    # 遍历身份证号前17位并计算出乘以对应加权数后的和
    for i in xrange(0, 17):
        num = int(card_id[i])
        result += num * w[i]
    # 求除以11后的余数作为校验值的下标索引值
    index = result % 11
    # 计算出的校验值和原始值相等则是正确的身份证号
    if check_bit[index] == card_id[17]:
        return True
    else:
        return False


if __name__ == '__main__':
    print id_number_isvalid("150930298913734325")
