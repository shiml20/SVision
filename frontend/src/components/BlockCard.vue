<template>
    <div class="main">
        <div class="block">
            <div class="title">a</div>
            <div class="content">1</div>
        </div>
        <div class="block">
            <div class="title">b</div>
            <div class="content">2</div>
        </div>
        <div class="block">
            <div class="title">c</div>
            <div class="content">3</div>
        </div>
        <div class="block">
            <div class="title">d</div>
            <div class="content">4</div>
        </div>
    </div>

</template>

<style scoped lang="scss">
.main {
    display: flex;
    width: 100%;
    height: 100%;
    justify-content: space-between;
    //border: 1px solid red;
    background-color: black;

    .block {
        flex: 1;
        height: 100%;
        border: 1px solid black;
        // margin: 10%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border-radius: 10%;
        background-color: rgba(255, 255, 255, 0.2);

        .title {
            height: 100%;
            border: 1px solid #04E38A;
            color: #04E38A;
            text-align: center;
            word-break: break-all;
        }

        .content {
            height: 100%;
            border: 1px solid #04E38A;
            color: #04E38A;
            text-align: center;
            word-break: break-all;
        }
    }
}
</style>