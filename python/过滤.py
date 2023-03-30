s = r"/flag|system|php|cat|sort|shell|\.|\\| |\'|\`|echo|\;|\？|\(|\:|\"|\<|\=/"
cn_s = ['（', '，', '：']
all_s = [chr(i) for i in range(32, 47 + 1)] + cn_s
dict = {
    ':': '英文冒号', '：': '中文冒号', '.': '点号',
    '^': '异或', '!': '英文感叹号', '！': '中文感叹号',
    '$': '美元符号', '&': '和好', '%': '百分号', '"': '双引号',
    "'": '单引号', '`': '反引号', '(': '左[英文]括号', ')': '右[英文]括号',
    '*': '星号', '_': '下划线', '<': "尖括号", '>': "尖括号", '+': "加号", '-': '减号',
    '?': '英文问号', '？': '中文问号', ';': '英文分号', '；': '中文分号',
    '/': '斜杠', '#': '井号', '=': '等号', '\\': '反斜线', ' ': '空格', ',': '英文逗号',
    '（': '中文括号','，':'中文逗号'
}
# for i in range(0,255):
# 	for i in s.strip('|'):
s1 = s.strip('/').split('|')
black_list = []
print(s1)
num = 0
for i in s1:
    if i[0] == '\\':
        # print(i[1:])
        num += 1
        black_list.append(i[1:])
        print(f'{i[1:]}【{dict[i[1:]]}】', end='  ')
        if num % 5 == 0:
            print()
print('被过滤')
print(f'黑名单：{black_list}')
num = 0  # 换行，方便查看
for i in all_s:
    if i not in black_list:
        num += 1
        print(f'{i}【{dict[i]}】', end='  ')
        if num % 5 == 0:
            print()
print('可以使用')
