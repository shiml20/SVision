<template>
  <el-header>
    <div class="l-content">
      <p>智慧园区可视化管理系统</p>
    </div>
    <div class="r-content">
        <img class="admin" src="../assets/images/admin.png" alt="">
        <el-dropdown>
          <span class="el-dropdown-link">
            <p>Admin</p>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item>个人中心</el-dropdown-item>
              <el-dropdown-item>设置中心</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      <el-button class="switch">
        <el-icon><SwitchButton /></el-icon>
      </el-button>
    </div>
  </el-header>>
</template>
<script>
</script>

<style lang="less" scoped>
header{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  background-color:black;
  height: 100%;
  height: 50px;
}
.l-content{
  color: white;
}
.r-content{
  p{
    color:white;
  }
  .admin{
    width: 40px;
    height: 100%;
  }
  .switch{
    position: absolute;
    width: 20px;
    height: 25px;
    top: 20px;
    margin:0;
    right:10px;
  }
}
</style>

