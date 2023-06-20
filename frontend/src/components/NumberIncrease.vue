<!-- demo.vue -->
<template>
    <div class="statisContent" v-loading="loading">
      <div class="box-item">
        <li :class="{ 'number-item': !isNaN(item), 'mark-item': isNaN(item) }" v-for="(item, index) in orderNum"
          :key="index">
          <span v-if="!isNaN(item)">
            <i ref="numberItem">0123456789</i>
          </span>
        </li>
      </div>
    </div>
  </template>
  
  <script>

  export default {
    data() {
      return {
        loading: false,
        orderNum: ['0', '0', '0', '0', '0'],
        count: 100,
      }
    },
    props:{
        number: Number
    },
    methods: {
      // 设置文字滚动
      setNumberTransform() {
        const numberItems = this.$refs.numberItem // 拿到数字的ref，计算元素数量
        const numberArr = this.orderNum.filter(item => !isNaN(item))
        // 结合CSS 对数字字符进行滚动,显示订单数量
        for (let index = 0; index < numberItems.length; index++) {
          const elem = numberItems[index]
          elem.style.transform = `translate(-50%, -${numberArr[index] * 10}%)`
        }
      },
      // 处理总订单数字
      toOrderNum(num) {
        let bit = 5
        num = num.toString()
        // 把订单数变成字符串
        if (num.length < bit) {
          num = '0' + num // 如未满八位数，添加"0"补位
          this.toOrderNum(num) // 递归添加"0"补位
        } else if (num.length === bit) {
          // 订单数中加入逗号
          this.orderNum = num.split('') // 将其便变成数据，渲染至滚动数组
        } else {
          // 订单总量数字超过八位显示异常
          this.$message.warning('订单总量数字过大，显示异常，请联系客服')
        }
      },
      increaseNumber(nextnum) {
        // eslint-disable-next-line @typescript-eslint/no-this-alias
        let self = this
        this.timer = setInterval(() => {
          self.count = nextnum
          this.toOrderNum(self.count)
          this.$nextTick(() => {
            self.setNumberTransform(self.count)
          })
        }, 3000)
      },
    },
    mounted() {
      this.increaseNumber(this.number)
    }
  }
  </script>
  
  <style lang='scss'>
  .statisContent {
    padding-top: 20px;
  
    .number-item {
      width: 41px;
      height: 75px;
      list-style: none;
      margin-right: 10px;
      background-color: black;
      border-radius: 4px;
      border: 1px solid #04E38A;
      display: inline-block;
      font-size: 60px;
      color: #04E38A;
  
      &>span {
        position: relative;
        display: inline-block;
        margin-right: 10px;
        width: 100%;
        height: 100%;
        writing-mode: vertical-rl;
        text-orientation: upright;
        overflow: hidden;
  
        &>i {
          font-style: normal;
          position: absolute;
          top: 7px;
          left: 50%;
          transform: translate(-50%, 0);
          transition: transform 1s ease-in-out;
          letter-spacing: 10px;
        }
      }
    }
  
    .number-item:last-child {
      margin-right: 0;
    }
  }
  </style>
  
  