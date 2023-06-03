<script lang="ts" setup>
import { toggleDark } from "~/composables";
</script>

<template>
  <el-menu class="el-menu-demo" mode="horizontal">
    <el-menu-item index="1" disabled>
      <el-text type="success">5G手机评价分析</el-text>
    </el-menu-item>
    <el-sub-menu index="2">
      <template #title>分工</template>
      <el-sub-menu index="2-1">
        <template #title>
          <el-text class="division-of-labor">爬虫小分组</el-text>
        </template>
        <el-menu-item index="2-1-1">
          <el-text class="division-of-labor">林乔瀚</el-text>
        </el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="2-2">
        <template #title>
          <el-text class="division-of-labor">建模小分组</el-text>
        </template>
        <el-menu-item index="2-2-1">
          <el-text class="division-of-labor">李嘉華</el-text>
        </el-menu-item>
        <el-menu-item index="2-2-2">
          <el-text class="division-of-labor">周骏</el-text>
        </el-menu-item>
        <el-menu-item index="2-2-3">
          <el-text class="division-of-labor">莫森华</el-text>
        </el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="2-3">
        <template #title>
          <el-text class="division-of-labor">网站搭建小分组</el-text>
        </template>
        <el-menu-item index="2-3-1">
          <el-text class="division-of-labor">康文豪</el-text>
        </el-menu-item>
      </el-sub-menu>
      
    </el-sub-menu>
    <el-popover
    placement="bottom"
    :width="200"
    trigger="click"
  >
    <template #reference>
      <el-menu-item index="3" ref="buttonRef">
        <el-text type="default">项目介绍</el-text>
      </el-menu-item>
    </template>
    <el-text class="info-text" type="info">进入5G时代，各大手机厂商纷纷推出5G手机，为了真实评估各主流的5G手机的用户口碑，可以登陆到主流电商网站，根据用户评价，识别出用户反馈的优劣势以及关注倾向度，从而客观评价5G手机的真实反馈。</el-text>
    <p></p>
    <el-text class="info-text" type="info">登陆主流电商网站（如京东、天猫等），锁定主流的5G手机（如VIVO X90、MI 13、IPHONE14等），分别获取各款手机完整的商品评价，通过对文本解析和分词处理，并剔除异常数据，汇总后得出各款手机的优点和缺点，为消费者提供选型参考。</el-text>
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
