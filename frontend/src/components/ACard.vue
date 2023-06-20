<template>
    <div class="block">
      <div class="plate">
        <div class="title">东</div>
        <div class="content">住宅区</div>
        <div class="content">Residential Area</div>
      </div>
      <div class="plate">
        <div class="title">球机数</div>
        <div class="content">2</div>
      </div>
    </div>
  </template>
  
  <style scoped lang="scss">
  .block {
    // width: 200px;
    // height: 200px;
    // padding: 10px;
    background-origin: content-box;
    background-image:
      linear-gradient(transparent 10px, #0e294c 10px, #0e294c calc(100% - 10px), transparent calc(100% - 10px), transparent 100%),
      linear-gradient(90deg, transparent 10px, #0e294c 10px, #0e294c calc(100% - 10px), transparent calc(100% - 10px), transparent 100%),
      linear-gradient(#4cc7f3 2px, transparent 2px, transparent calc(100% - 2px), #4cc7f3 calc(100% - 2px), #4cc7f3 100%),
      linear-gradient(90deg, #4cc7f3 2px, transparent 2px, transparent calc(100% - 2px), #4cc7f3 calc(100% - 2px), #4cc7f3 100%);
    background-repeat: no-repeat;
    background-position: top left, top left, bottom right, bottom right;
    background-size: 100% 100%, 100% 100%;
  
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    height: 100%;
    width: 100%;
    .plate {
      text-align: center;
  
      .title {
        // font-weight: bolder;
        font-size: 24px;
        color: #009dff;
      }
  
      .content {
        font-weight: bolder;
        font-size: 24px;
        color: yellow;
      }
    }
  }
  </style>