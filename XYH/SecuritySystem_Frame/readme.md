## 运行项目

```
npm run serve
```

## 准备

本项目使用了 `element-plus` 和 `echarts` 两个组件库。

安装：

```
npm install element-plus
npm install echarts

// 如果没安装路由 router
npm install vue-router
```

## 基本架构

1. 登陆页面 login
2. 主页 home 含5个子页面
   1. situation
   2. manage
   3. point
   4. synthesis
   5. center

### 登陆页面 login

使用 ApiPost7 软件进行调试，下载：https://www.apipost.cn/。在该软件中创建一个接口，通过 login.vue 中 axios 功能发送请求，获取响应后即可跳转到 home 页面。

ApiPost7介绍：简单来说，就是让你可以向指定url发送一个请求，然后它返回给你响应数据，这个数据可以在软件中进行设置。

### 主页 home

路由配置已经弄好了，现在主要就是写对应的 myIndex.vue 里面的前端页面的代码。