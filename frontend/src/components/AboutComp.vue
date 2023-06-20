<template>
    <div class="b-container">
        <div class="line-1">我们是SVision智慧安防系统</div>
        <div class="line-2">致力于数字赋能城市管理</div>
        <div class="line-3">SVision以“人/货/场”为核心，基于人工智能、物联网和大数据技术实现综合智慧安防管理</div>
            <div class="login-btn">
                <a href="https://docs.qq.com/slide/DQ0FubUxNbVFuQlFU">
                    <button  class="button1" @onclick="Jump" style="color:white; text-decoration:none">了解更多</button>
                    </a>
                <HR align=center  width="100%" color=#987cb9  SIZE=5></HR>
              </div>
        <div class="item">
            <div class="sub-item">
                <div class="item-title">关于我们</div>
                <div>我们的目标</div>
                <div>我们的用途</div>
            </div>
            <div class="sub-item">
                <div class="item-title">资源</div>
                <div>智慧安防管理系统</div>
                <div>海康威视硬件资源</div>
            </div>
            <div class="sub-item">
                <div class="item-title">联系我们</div>
                <div>18858868888</div>
                <div>shiml20@mails.tsinghua.edu.cn</div>
            </div>
        </div>
    </div>
 

</template>

<script setup>
</script>

<style scoped lang="scss">

.b-container {
    background-image: url('../assets/img/aboutbg.jpg');
    background-size: cover;
    background-position: center;
    width: 100%;
    position: relative;
    color: white;
    padding-top: 12%;
    text-align: center;
    div {
        //border: 1px solid red;
        margin-top: 5px;
    }
    display: flex;
    flex-direction: column;
}
.b-container {
    .line-1 {
        height: 15%;
        font-size: 40px;
    }
    .line-2 {
        height: 15%;
        font-size: 50px;
        color: #2cb9eb;
    }
    .line-3 {
        height: 10%;
    }

    .login-btn {
        height: 15%;
          .button1 {
            background-color: #18c4fc;
            border: none;
            color: white;
            margin-left: 10px;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        .button2 {
          background-color: #a19ca7;
          border: none;
          margin-left: 10px;
          padding: 10px 20px;
          text-align: center;
          text-decoration: none;
          display: inline-block;
          font-size: 16px;
          margin: 4px 2px;
          cursor: pointer;
      }

    }
    .item {
        height: 40%;
        width: 100%;
        display: flex;
        justify-content: space-between;
        .sub-item {
            width: 30%;
        }
        .item-title {
            color: #187db3;
            margin-bottom: 10%;
        }
    }

}

</style>


