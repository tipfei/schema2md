# -*- coding: utf-8 -*-
import json

filename = 'a.json'

c = json.load(open(filename, encoding='utf-8'))

with open(filename + '.md', 'w+') as f:
    f.truncate()
    def print_one(it, num, name='', dpt=0):
        if dpt == 0:
            f.write('\n# {}、 {}({})\n'.format(num, it["title"], it['_id']))
            f.write('- 简要描述: {}\n'.format(it['description']))
            f.write('- 访问方式: Restful API\n')
            f.write('- 数据格式: json\n')
            f.write('\n| 参数名      | 类型   | 说明    |\n')
            f.write('| :---        | :---   | :---    |\n')
        elif it['type'] in ('object', 'array'):
            title = it.get('title', 'NA')
            if it['type'] in ('array', ):
                it = it['items']
            if 'properties' not in it:
                return
            f.write('\n{} {}、 {}({})\n'.format('#' * (dpt + 1), num, title, name))
            f.write('| 参数名      | 类型   | 说明    |\n')
            f.write('| :---        | :---   | :---    |\n')
        for k, v in it['properties'].items():
            title = v.get('title', 'NA')
            f.write('|{}|{}|{}|\n'.format(k, v.get('type', 'string'), title))
        items = {k: v for k, v in it['properties'].items() if v.get('type', 'string') in ('object', 'array') and (v.get('properties', None) or v.get('items', None))}
        for idx, (k, v) in enumerate(items.items()):
            print_one(v, '{}.{}'.format(num, idx + 1), k, dpt + 1)
    for idx, it in enumerate(c):
        # print('>> {}'.format(it['_id']))
        print_one(it, str(idx + 1))
