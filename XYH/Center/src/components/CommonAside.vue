<template>
    <el-aside width="180px">
        <el-menu class="el-menu-vertical-demo">
            <el-menu-item 
                :index="item.path" 
                v-for="item in noChildren()"
                :key="item.path"
                @click="clickMenu(item)"
            >
                <span>{{item.label}}</span>
            </el-menu-item>            
        </el-menu>
    </el-aside>
</template>

<script>
import {useRouter} from 'vue-router'
export default {
    setup() {
        const list = [
            {
                path: '/user',
                name: 'user',
                label: '用户管理',
                icon: 'user',
                url: 'UserManage/UserManage'
            },
            {
                path: '/rule',
                name: 'rule',
                label: '报警规则',
                icon: 'rule',
                url: 'AlarmRule/AlarmRule'
            },
        ];

        const router = useRouter();

        const noChildren = ()=>{
            return list.filter((item) => !item.children);
        };

        const hasChildren = () => {
            return list.filter((item) => item.children);
        };

        const clickMenu =(item) => {
            router.push({
                name: item.name,
            });
        };

        return {
            noChildren,
            hasChildren,
            clickMenu
        };
    },
};
</script>

<style lang="less" scoped>
    
    .el-menu-vertical-demo{
        background-color: rgb(0, 0, 0);
        height: 100%;
    }
    span{
        color: white;
    }
    .el-menu{
        border-right:none;
        align-items: center;
    }
    
</style>