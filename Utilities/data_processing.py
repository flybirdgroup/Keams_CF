
# data clean up, replace duplicated province name into same format


def data_cleanup(df):
    df = df.replace('广东省','广东').replace('江苏省','江苏').replace('HONG KONG','香港')
    df['PROVINCE'] = df['PROVINCE'].apply(lambda x: province_to_short(x))

    # change Chinese into English
    df = df.rename(columns={"销售团队": "Sales_TEAM", "发票日期": "Invoice_date", "合同号": "Contract_NO","不含税单价":"price"})

    # process missing value 缺失值处理 - 因为数据量还是比较大,暂时dropna方法去掉
    df.dropna(inplace=True)
    return df


def province_to_short(province):
    if province == "广东":
        return "GD"
    elif province == "天津":
        return "TJ"
    elif province == "山东":
        return "SD"
    elif province == "辽宁":
        return "LN"
    elif province == "江苏":
        return "JS"
    elif province == "黑龙江":
        return "HLJ"
    elif province == "吉林":
        return "JL"
    elif province == "福建":
        return "HLJ"
    elif province == "安徽":
        return "JL"
    elif province == '北京':
        return 'BJ'
    elif province == '湖南':
        return 'HN'
    elif province == '上海':
        return 'SH'
    elif province == '重庆':
        return 'CQ'
    elif province == '山西':
        return 'SX'
    elif province == '四川':
        return 'SC'
    elif province == '江西':
        return 'JX'
    elif province == '浙江':
        return 'ZJ'
    elif province == '湖北':
        return 'HUB'
    elif province == '河北':
        return 'HEB'
    elif province == '陕西':
        return 'XX'
    elif province == '广西':
        return 'GX'
    elif province == '内蒙古':
        return 'NMG'
    elif province == '云南':
        return 'YN'
    elif province == '宁夏':
        return 'LX'
    elif province == '甘肃':
        return 'GS'
    elif province == '河南':
        return 'HEN'
    elif province == 'GERMANY':
        return 'DE'
    elif province == 'ITALY':
        return 'IT'
    elif province == 'TAIWAN':
        return 'TW'
    elif province == 'SINGAPORE':
        return 'SG'
    elif province == '香港':
        return 'HK'