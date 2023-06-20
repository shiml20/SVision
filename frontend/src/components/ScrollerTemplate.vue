<template>
    <div
      class="scroll-container"
      :id="scrollId"
      style="border:0px solid red;
      height: 100%;
      width: 100%;
      overflow-y: scroll;
      text-align: center;
      top: 0%;
      left: 0%;"
    >
      <div>
        <div class="item">
          <div class="title">① 设备编号: A231001</div>
          <div class="content">设备点位: A区B1层001拐角处</div>
          <div class="content">检修时间: 2023年2月10日</div>
          <div class="content">设备状况：正常</div>
        </div>
        <div class="item">
          <div class="title">② 设备编号: B241001</div>
          <div class="content">设备点位: B区B1层001拐角处</div>
          <div class="content">检修时间: 2023年2月10日</div>
          <div class="content">设备状况：正常</div>
        </div>
        <div class="item">
          <div class="title">③ 设备编号: B241002</div>
          <div class="content">设备点位: B区B1层002楼梯处</div>
          <div class="content">检修时间: 2023年2月10日</div>
          <div class="content">设备状况：正常</div>
        </div>
        <div class="item">
          <div class="title">④ 设备编号: C241001</div>
          <div class="content">设备点位: C区B1层001楼梯处</div>
          <div class="content">检修时间: 2023年2月10日</div>
          <div class="content">设备状况：正常</div>
        </div>
        <div class="item">
          <div class="title">⑤ 设备编号: D241001</div>
          <div class="content">设备点位: D1层001拐角处</div>
          <div class="content">检修时间: 2023年2月10日</div>
          <div class="content">设备状况：正常</div>
        </div>
        <div class="item">
          <div class="title">⑥ 设备编号: E241003</div>
          <div class="content">设备点位: E区B1层001拐角处</div>
          <div class="content">检修时间: 2023年2月10日</div>
          <div class="content">设备状况：正常</div>
        </div>
        <div class="item">
          <div class="title">⑦ 设备编号: F241001</div>
          <div class="content">设备点位: F区B1层001楼梯处</div>
          <div class="content">检修时间: 2023年2月10日</div>
          <div class="content">设备状况：正常</div>
        </div>
      </div>
    </div>
</template>
  
<script>
  export default {
  data() {
    return {
      scrollTimer: null, // 滚动定时器
      pauseTimer: null, // 暂停定时器
      scrollId: 'scrollId', // 滚动容器id
      scrollDirection: 'down' // 滚动方向 up向上 down向下
    }
  },
  unmounted() {
    // 清理定时器
    clearTimeout(this.pauseTimer)
    this.pauseTimer = null
    clearInterval(this.scrollTimer)
    this.scrollTimer = null
    // 清理点击监听
    window.document.removeEventListener('click', this.pauseScroll)
  },
  mounted() {
    this.dataCompleteFun()
  },
  methods: {
    // 数据加载完成方法
    dataCompleteFun() {
      // 开启滚动
      this.autoScroll()
    },
    autoScroll() {
      const scrollHeight = document.getElementById(this.scrollId).scrollHeight
      const clientHeight = document.getElementById(this.scrollId).clientHeight
      const scroll = scrollHeight - clientHeight
      // 滚动长度为0
      if (scroll === 0) {
        return
      }
      // 触发滚动方法
      this.scrollFun()
      // 去除点击监听
      window.document.removeEventListener('click', this.pauseScroll)
      // 重设点击监听
      window.document.addEventListener('click', this.pauseScroll, false)
    },
    pauseScroll() {
      // 定时器不为空
      if (this.scrollTimer) {
        // 清除定时器
        clearInterval(this.scrollTimer)
        this.scrollTimer = null
        // 一秒钟后重新开始定时器
        this.pauseTimer = setTimeout(() => {
          this.scrollFun()
        }, 2000)
      }
    },
    scrollFun() {
      // 如果定时器存在
      if (this.scrollTimer) {
        // 则先清除
        clearInterval(this.scrollTimer)
        this.scrollTimer = null
      }
      this.scrollTimer = setInterval(() => {
        const scrollHeight = document.getElementById(this.scrollId).scrollHeight
        const clientHeight = document.getElementById(this.scrollId).clientHeight
        const scroll = scrollHeight - clientHeight
        // 获取当前滚动条距离顶部高度
        const scrollTop = document.getElementById(this.scrollId).scrollTop
        // 向下滚动
        if (this.scrollDirection === 'down') {
          const temp = scrollTop + 1
          document.getElementById(this.scrollId).scrollTop = temp // 滚动
          // 距离顶部高度  大于等于 滚动长度
          if (scroll <= temp) {
            // 滚动到底部 停止定时器
            clearInterval(this.scrollTimer)
            this.scrollTimer = null
            document.getElementById(this.scrollId).scrollTop = 0 // 滚动
            // 改变方向
            // this.scrollDirection = 'up'
            // 一秒后重开定时器
            setTimeout(() => {
              this.scrollFun()
            }, 1000)
          }
        } 
      }, 150)
    }
  }
}
</script>

<style scoped lang="scss">
 .scroll-container {
  height: 100%;
  width: 100%;
  position: relative;
 }
 .item {
  color: white;
  border-top: 2px dashed gray;
  padding-top: 1%;
  margin-top: 5%;
  div {
    text-align: left;
  }
  .title {
    font-size: x-larger;
    color: #006ec9;
  }
  .content {
    margin-top: 1%;
    padding-left: 10%;
  }
 }

</style>