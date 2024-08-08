# 阅读我
## 用法
该文档包含一个计算器界面，该界面通过一个后端服务器与一个LLM进行交互，以生成URL。用户可以将prompt里面输入想要输入的然后给到LLM，LLM输出URL，然后用户将URL输入到浏览器，查看结果。

有一部分是和项目9相关的，计算器的网页界面也是与之相关。
## 文件结构
```plaintext
/api-main
    /node_modules           ->需要使用的库
        /express            
        /COR
    /API_Documentation.md   ->API文档(markdown版)
    /calculatorWeb.html     ->计算器界面
    /package.json           ->基础包
    /package-lock.json
    /Prompts.txt            ->写给LLM的prompt，让它生成URL
    /readme.md              ->阅读手册
    /script.js              ->连接前端和后端的脚本
    /server.js              ->后端服务器
```