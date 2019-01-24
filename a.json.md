
# 1、 数据模型定义(sys-schema_definition)
- 简要描述: 定义模型信息
- 访问方式: Restful API
- 数据格式: json

| 参数名      | 类型   | 说明    |
| :---        | :---   | :---    |
|name|string|模型名称|
|nameSpace|string|模型命名空间|
|version|string|版本号|
|modelType|string|模型类型|
|modelClass|integer|模型可见级别|
|dataLevel|integer|数据权限等级|
|description|string|模型描述|
|orgId|string|模型所属组织|
|orgPath|string|模式所属组织路径|
|schema|object|模型属性schema|
|isIssued|boolean|发布状态|
|_creator|string|创建用户|
|_createdTime|object|创建时间|
|_updater|string|更新用户|
|_updatedTime|object|修改时间|
