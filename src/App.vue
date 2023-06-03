<script>
import { ref } from 'vue'
const activeName = ref('first')
</script>
<template>
  <el-config-provider namespace="ep">

    <BaseHeader />

    <!-- <h1 id="dev_hint">······开发中······</h1> -->
    <div style="text-align:center" >
      <el-icon><Guide /></el-icon><br/>
        <el-text class="page-title" type="default" tag="b">软件工程课程项目展示网站<br/></el-text>
        <el-icon><Guide /></el-icon>
    </div> 

      <el-icon><Guide /></el-icon>
      <el-descriptions
        class="margin-top"
        title=""
        column="2"
        size="large"
        border="true"
        labelStyle="font-size:30px"
        contentStyle="font-size:30px"
        id="description-table"
        >
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon>
              <user />
            </el-icon>
            小组成员
          </div>
        </template>
        <el-tag size="large"><el-text type="primary">李嘉華</el-text></el-tag>
        <el-tag size="large"><el-text type="primary">周骏</el-text></el-tag>
        <el-tag size="large"><el-text type="primary">林乔瀚</el-text></el-tag>
        <el-tag size="large"><el-text type="primary">莫森华</el-text></el-tag>
        <el-tag size="large"><el-text type="primary">康文豪</el-text></el-tag>
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon>
              <iphone />
            </el-icon>
            学校
          </div>
        </template>
        <el-tooltip content="点击跳转到学校官网">
        <el-link href="https://www.scut.edu.cn/" target="_blank">华南理工大学</el-link>
        </el-tooltip>
        <!-- <el-text type="default" tag="ins">华南理工大学</el-text> -->
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon>
              <location />
            </el-icon>
            题目
          </div>
        </template>
        <el-text type="default">5G手机评论分析</el-text>
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon>
              <tickets />
            </el-icon>
            指导老师
          </div>
        </template>
        <el-tag size="large"><el-text type="primary">苏锦钿</el-text></el-tag>
      </el-descriptions-item>
      </el-descriptions>
      <el-icon><Guide /></el-icon><br/>
      <el-icon><Guide /></el-icon>
    

    <div id="main">
      <el-tooltip
        content="回到顶部"
      >
      <el-backtop :right="100" :bottom="100" />
      </el-tooltip>



      <el-tabs type="border-card" id="tab-pane" model-value="first">
        <el-tab-pane name="zeroth" disabled>
          <template #label>
            <!-- <h2>结 果 展 示</h2> -->
            
            <el-tooltip
              class="box-item"
              effect="dark"
              content="请点击右边的标签以查看对应的图片"
              placement="top-start"
            >
            <el-text class="tab-text" type="success" size="large">结果展示</el-text>
          </el-tooltip>
          </template>
        </el-tab-pane>
        <el-tab-pane name="first">
          <template #label>
            <!-- <h1>好评词云</h1> -->
            <el-text class="tab-text" type="primary" size="large">1.好评词云</el-text>
          </template>
            <el-image v-loading="loading" src="/5G-PHA-Display-Website/images/advantagesCloud.png" fit="scale-down"/>
           
        </el-tab-pane>
        <el-tab-pane name="second">
          <template #label>
            <!-- <h1>差评词云</h1> -->
            <el-text class="tab-text" type="primary" size="large">2.差评词云</el-text>
          </template>
          <el-image v-loading="loading" src="/5G-PHA-Display-Website/images/disadvantagesCloud.png" fit="scale-down"/>
        </el-tab-pane>
        <!-- <el-tab-pane name="third">
          <template #label> -->
            <!-- <h1>关键词云图</h1> -->
            <!-- <el-text class="tab-text" type="primary" size="large">3.关键词词云</el-text>
          </template>
          <el-image v-loading="loading" src="/5G-PHA-Display-Website//images/wordcloud.png" fit="scale-down" />
        </el-tab-pane> -->
        <el-tab-pane name="forth">
          <template #label>
            <!-- <h1>星级统计图</h1> -->
            <el-text class="tab-text" type="primary" size="large">3.星级统计图</el-text>
          </template>
          <el-image v-loading="loading" src="/5G-PHA-Display-Website/images/stars.png" fit="scale-down" />
        </el-tab-pane>
      </el-tabs>

      <el-icon><Guide /></el-icon><br/>
      <el-icon><Guide /></el-icon>
      <!-- <el-carousel :interval="5000" arrow="always" id="carousel">
        <el-carousel-item v-for="item in 4" :key="item">
          <h3 text="2xl" justify="center">carousel占位符{{ item }}</h3>
        </el-carousel-item>
      </el-carousel> -->
    </div>
    <!-- <el-empty description="完" /> -->
    <br/><br/><br/><br/><br/><br/><br/><br/>

    <el-container>
      <el-footer style="text-align: center; font-size: 12px">
        版权所有&copy本项目小组 2023
      </el-footer>
    </el-container>
    </el-config-provider>
</template>

<style scoped>

.tab-text{
  font-size:28px;
}

#carousel{
  background-color: aquamarine;
}

#tab-pane{
  background-color:gray;
  position: relative;
  width: 70%;
  left:15%;
}

#description-table *{
  font-size: 30px;
  font-family: 'SimSun';

}

.page-title{
  font-size: 40px !important;
  /* text-align: center !important; //不起作用 */
  font-family: 'SimSun';
}

div#main{
  /* width: 100%; */
  /* left:0; */
  /* top:0; */
  /* position: absolute; */
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
