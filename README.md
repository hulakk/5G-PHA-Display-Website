为方便Github Page部署，本目录设为子仓库  

只针对@hulakk：任何更改需先提交到[此仓库](https://github.com/hulakk/5G-PHA-Display-Website.git) ，再同步到此处  

@hulakk以外的人如果嫌麻烦（本来也是不必要的麻烦），也可以直接提交在这里，余下工作让@hulakk解决  

同步：  
```sh
# 同步
git subtree pull --prefix=website-src https://github.com/hulakk/5G-PHA-Display-Website.git main
```

修改代码或资源后，需要重新生成网页：  
```sh
# 方法一（强烈推荐）
# @hulakk,让他解决
```

```sh
# 方法二（十分不推荐）

# 1.安装node.js

# 2.安装环境
npm install

# 3.本地调试
npm run dev 

# 4.生成正式版本并部署到云端
npm run build
npm run deploy
```