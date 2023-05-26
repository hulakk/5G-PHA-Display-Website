<script lang="ts" setup>
import { toggleDark } from "~/composables";
</script>

<template>
  <el-menu class="el-menu-demo" mode="horizontal">
    <el-menu-item index="1" disabled>5G手机评价分析</el-menu-item>
    <el-sub-menu index="2">
      <template #title>分工</template>
      <el-sub-menu index="2-1">
        <template #title>爬虫小分组</template>
        <el-menu-item index="2-1-1">林乔瀚</el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="2-2">
        <template #title>建模小分组</template>
        <el-menu-item index="2-2-1">李嘉華</el-menu-item>
        <el-menu-item index="2-2-2">周骏</el-menu-item>
        <el-menu-item index="2-2-3">莫森华</el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="2-3">
        <template #title>网站搭建小分组</template>
        <el-menu-item index="2-3-1">康文豪</el-menu-item>
      </el-sub-menu>
      
    </el-sub-menu>
    <el-popover
    placement="bottom"
    :width="200"
    trigger="click"
  >
    <template #reference>
      <el-menu-item index="3" ref="buttonRef">Info</el-menu-item>
    </template>
      待补充
  </el-popover>
    
    <!-- <el-menu-item index="4">Orders</el-menu-item> -->
    <el-menu-item h="full" @click="toggleDark()">
      <button
        class="border-none w-full bg-transparent cursor-pointer"
        style="height: var(--ep-menu-item-height)"
      >
        <i inline-flex i="dark:ep-moon ep-sunny" />
      </button>
    </el-menu-item>
  </el-menu>
</template>
