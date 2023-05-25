<template>
  <el-config-provider namespace="ep">
    <BaseHeader />
    <div id="main">
      <h1 id="dev_hint">······开发中······</h1>
      <!-- <el-backtop :right="100" :bottom="100" /> -->

      <el-carousel :interval="4000" type="card" height="200px">
        <el-carousel-item v-for="item in 6" :key="item">
          <h3 text="2xl" justify="center">{{ item }}</h3>
        </el-carousel-item>
      </el-carousel>

      <el-tabs type="border-card">
        <el-tab-pane name="first">
          <template #label>
            <h1 class="el-collapse-item-title">优点云图</h1>
          </template>
          <el-image src="/images/advantagesCloud.png" fit="cover"/>
        </el-tab-pane>
        <el-tab-pane name="second">
          <template #label>
            <h1 class="el-collapse-item-title">缺点云图</h1>
          </template>
          <el-image src="/images/disadvantagesCloud.png" fit="cover"/>
        </el-tab-pane>
        <el-tab-pane name="third">
          <template #label>
            <h1 class="el-collapse-item-title">关键词云图</h1>
          </template>
          <el-image src="/images/wordcloud.png" fit="cover" />
        </el-tab-pane>
        <el-tab-pane name="forth">
          <template #label>
            <h1 class="el-collapse-item-title">评分图</h1>
          </template>
          <el-image src="/images/stars.png" fit="cover" />
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
  line-height: 200px;
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
