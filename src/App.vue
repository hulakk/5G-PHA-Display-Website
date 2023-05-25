<script>

</script>
<template>
  <el-config-provider namespace="ep">
    <BaseHeader />
    <h1 id="dev_hint">······开发中······</h1>
    <el-descriptions
      class="margin-top"
      title=""
      column="2"
      size="large"
      border="true"
      >
    <!-- <template #extra>
      <el-button type="primary">Operation</el-button>
    </template> -->
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <user />
          </el-icon>
          小组成员
        </div>
      </template>
      <el-tag size="large">李嘉華</el-tag>
      <el-tag size="large">周骏</el-tag>
      <el-tag size="large">林乔瀚</el-tag>
      <el-tag size="large">莫森华</el-tag>
      <el-tag size="large">康文豪</el-tag>
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <iphone />
          </el-icon>
          学校
        </div>
      </template>
      华南理工大学
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <location />
          </el-icon>
          题目
        </div>
      </template>
      5G手机评论分析
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <tickets />
          </el-icon>
          指导老师
        </div>
      </template>
      <el-tag size="large">1111</el-tag>
    </el-descriptions-item>
  </el-descriptions>
    <div id="main">
      <el-backtop :right="100" :bottom="100" />
      <el-carousel :interval="5000" arrow="always">
        <el-carousel-item v-for="item in 4" :key="item">
          <h3 text="2xl" justify="center">{{ item }}</h3>
        </el-carousel-item>
      </el-carousel>

      <el-tabs type="border-card">
        <el-tab-pane name="first">
          <template #label>
            <h1>优点云图</h1>
          </template>
          <img v-loading="loading" src="/images/advantagesCloud.png" fit="cover"/>
        </el-tab-pane>
        <el-tab-pane name="second">
          <template #label>
            <h1>缺点云图</h1>
          </template>
          <img v-loading="loading" src="/images/disadvantagesCloud.png" fit="cover"/>
        </el-tab-pane>
        <el-tab-pane name="third">
          <template #label>
            <h1>关键词云图</h1>
          </template>
          <img v-loading="loading" src="/images/wordcloud.png" fit="cover" />
        </el-tab-pane>
        <el-tab-pane name="forth">
          <template #label>
            <h1>评分图</h1>
          </template>
          <img v-loading="loading" src="/images/stars.png" fit="cover" />
        </el-tab-pane>
      </el-tabs>
    </div>
    </el-config-provider>
</template>

<style>
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
div#main{
  width: 100%;
  left:0;
  /* top:0; */
  position: absolute;
  text-align: center;
  font-family: "STXingkai","Microsoft YaHei";
}
h1#dev_hint{
    text-align: center;
    color: orange;
    font-family: "STCaiyun","Microsoft YaHei";
    font-size: 50px;
}
</style>



<!-- <template>
  <el-config-provider namespace="ep">
    <BaseHeader />
    <div class="flex main-container">
      <BaseSide />
      <div w="full" py="4">
        <Logos my="4" />
        <HelloWorld msg="Hello Vue 3 + Element Plus + Vite" />
      </div>
    </div>
  </el-config-provider>
</template>

<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}

.main-container {
  height: calc(100vh - var(--ep-menu-item-height) - 3px);
}
</style> -->
