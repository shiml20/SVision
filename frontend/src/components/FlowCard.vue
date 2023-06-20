<template>

<div class="card-header">
    {{ props.msg1 }}
</div>
<div class="card-main">
    <div class="item-1">
        {{ props.msg2 }}
    </div>
    <div class="item-2">

        <div class="item-2-1">
            <span class="items-1">
                {{ props.msg3 }}
            </span>
            <span class="items-2">
                {{ props.msg4 }}
            </span>
        </div>
        <div class="item-2-2">
            <span class="items-1"></span>
            {{ props.msg5 }}
            <span class="items-2">
                {{ props.msg6 }}
            </span>
        </div>
    </div>

</div>

</template>


<script setup>
/* eslint-disable */
const props = defineProps({
    msg1:{
        type:String,
        default: 'sss'
    },
    msg2:{
        type:String,
        default: 'aaa'
    },
    msg3:{
        type:String,
        default: 'ccc'
    },
    msg4:{
        type:String,
        default: 'dd'
    },
    msg5:{
        type:String,
        default: 'dd'
    },
    msg6:{
        type:String,
        default: 'dd'
    }
})


</script>

<style scoped lang="scss">
.card-header {
    height: 20%;
    color: white;
    font-size: x-large;
    padding-left: 10%;
}

.card-main {
    height: 80%;
    display: flex;
    flex-direction: column;
    margin-left: 10%;
    margin-right: 10%;
    .item-1 {
        //border: 1px solid red;
        height: 40%;
        color: rgb(4, 227, 138);
        font-size: xx-large;
        padding-left: 10%;
        padding-top: 10%;
    }

    .item-2 {
        //border: 1px solid red;
        height: 40%;
        display: flex;
        justify-content: space-between;
        color: white;
        padding:0 10%;
        padding-top: 7%;
        .item-2-1 {
            color: #8f8f8f;
            display: flex;
            flex-direction: column;
            .items-2 {
                color: white;
            }
        }
        .item-2-2 {
            color: #8f8f8f;
            display: flex;
            flex-direction: column;
            .items-2 {
                color: rgb(4, 227, 138);
            }
        }
    }
}

</style>