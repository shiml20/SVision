/* eslint-disable */

/*************************************************************************
【文件名】
【功能模块和目的】ts的配置
【开发者及日期】史明磊(shiml20@mails.tsinghua.edu.cn) 2023-02-11
【更改记录】
	2023-02-11 由史明磊增加注释
*************************************************************************/

declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}



/*************************************************************************
【模块名称】
【模块功能】为了在typescript中引入json文件而不报错
【参数】无
【返回值】无
【开发者及日期】史明磊(shiml20@mails.tsinghua.edu.cn) 2023-02-11
【更改记录】
	2023-02-11 由史明磊增加注释
*************************************************************************/

declare module "*.json" {
  const file: any;
  export default file;
}