# SQL

## 一. 数据库基本操作

1. 查看所有数据库
```sql
SHOW DATABASES;
```

2. 创建新数据库
```sql
CREATE DATABASE db_name;
```

3. 删除数据库
```sql
DROP DATABASE db_name;
```

## 二. 数据表基本操作

1. 创建数据表
```sql
CREATE TABLE tb_name
(
    字段1 数据类型 [列级别约束条件] [默认值],
    字段2 数据类型 [列级别约束条件] [默认值],

    [表级约束条件]
);
```

2. 查看
```sql
SHOW TAELES;
```

3. 使用主键

定义列的同时定义主键
```sql
CREATE TABLE tb_name
(
    字段1 数据类型 PRIMARY KEY [默认值],
);
```

最后定义
```sql
CREATE TABLE tb_name
(
    字段1 数据类型 [列级别约束条件] [默认值],
    字段2 数据类型 [列级别约束条件] [默认值],

    [CONSTRAINT <约束名>] PRIMARY KEY [字段名]
);
```

多个主键
```sql
CREATE TABLE tb_name
(
    PRIMARY KEY [字段1,字段2,...]
);
```

使用外键
```sql
    [CONSTRAINT <外键名>] FOREIGN KEY 字段1[,字段2,...] REFERENCES <主表名> 主键列1[,主键列2,...]
```

使用非空约束
```sql
字段名 数据类型 NOT UNLL
```

使用唯一约束
```sql
字段名 数据类型 UNIQUE
```

设置自动增加
```sql
字段名 数据类型 AUTO_INCREMENT
```

查看表
```sql
DESCRIBE tb_name;

DESC tb_name;
```

## 三. 用户和密码
1. 登陆
```bash
mysql -u user_name -p
```

2. 创建用户
```sql
create user 'user_name'@'localhost' identified by 'mypassword';
```

3. 查看相关设置
```sql
SHOW VARIABLES LIKE 'validate_password%';
```

4. 密码等级
```
LOW Length >= 8 characters.
MEDIUM Length >= 8, numeric, mixed case, and special characters.
STRONG Length >= 8, numeric, mixed case, special characters and dictionary file.
```
5. 设置密码等级
```sql
SET GLOBAL validate_password.policy=LOW;
```

6. 修改密码
```sql
alter user 'root'@'localhost' identified by '123';
```