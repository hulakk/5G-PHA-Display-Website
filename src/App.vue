<script setup>
import { ref } from 'vue'

const erb_selected=ref("erb-a")
const s_p=ref("")
const s_mn=ref("")

const jd_mn_list=[
  {label:'iphone13',value:'s-mn-ip13'},
  {label:'机型A',value:'s-mn-a'},
  {label:'机型B',value:'s-mn-b'},
  {label:'机型E',value:'s-mn-e'},
]
const tb_mn_list=[
  {label:'iphone13',value:'s-mn-ip13'},
  {label:'机型A',value:'s-mn-a'},
  {label:'机型B',value:'s-mn-b'},
  {label:'机型D',value:'s-mn-d'},
]
const phoneparameters={
  'ip13':{

  }
}
const phonecomment={
  'ip13':
    {
      advantage:'用户觉得iPhone13运行流畅、外观好看、性价比高、质量好、拍照效果好',
      disadvantage:'用户觉得iPhone13卡顿、容易发热、电池容量小、屏幕尺寸小、声音小'
    },

}
</script>
<template>
  <el-config-provider namespace="ep">

    <BaseHeader />

    <!-- <h1 id="dev_hint">······开发中······</h1> -->
    <div style="text-align:center" >
      <el-icon><Guide /></el-icon><br/>
        <el-text class="page-title" type="default" tag="b">5G手机评论分析<br/></el-text>
        <el-icon><Guide /></el-icon>
    </div> 

    

    <div id="main">
      <el-tooltip
        content="回到顶部"
      >
      <el-backtop :right="100" :bottom="100" />
      </el-tooltip>

      <div id="form-select">
        <table>
          <tr>
            <td>
              <el-text size="large">选择平台：</el-text>
              <el-select v-model="s_p" placeholder="未选择" size="large">
                <el-option label="京东" value="s-p-jd"/>
                <el-option label="淘宝" value="s-p-tb"/>
              </el-select>
            </td>
            <td>
              <el-text size="large">选择机型：</el-text>
              <el-select  v-model="s_mn" placeholder="未选择" size="large">
                <el-option
                  v-if="s_p==='s-p-jd'"
                  v-for="item in jd_mn_list"
                  :label="item.label"
                  :value="item.value"
                />
                <el-option
                  v-else-if="s_p==='s-p-tb'"
                  v-for="item in tb_mn_list"
                  :label="item.label"
                  :value="item.value"
                />
                <el-option v-else label="请先选择平台" disabled/>
              </el-select>
            </td>
          </tr>
        </table>
      </div>

      
      <el-tabs type="border-card" id="tab-pane" model-value="third">
        <!-- <el-tab-pane name="zeroth" disabled>
          <template #label>
            
            <el-tooltip
              class="box-item"
              effect="dark"
              content="请点击右边的标签以查看对应的图片"
              placement="top-start"
            >
            <el-text class="tab-text" type="success" size="large">结果展示</el-text>
          </el-tooltip>
          </template>
        </el-tab-pane> -->
        
        <el-tab-pane name="third">
          <template #label>
            <el-text class="tab-text" type="primary" size="large">手机参数</el-text>
          </template>
          <div v-if="s_p==='s-p-jd' && s_mn==='s-mn-ip13'">
            
          </div>
          <div v-else-if="s_p==='' || s_mn===''" class="result">
            <el-text type="warning" size="large">提示：请先在上方选择平台和机型</el-text>
          </div>
          <div v-else class="result">
            <el-text type="warning" size="large">对应平台和机型暂无内容</el-text>
          </div>
        </el-tab-pane>

        <el-tab-pane name="first">
          <template #label>
            <!-- <h1>好评词云</h1> -->
            <el-text class="tab-text" type="primary" size="large">评论词云</el-text>
          </template>

          <!-- 京东、iPhone13 -->
          <div v-if="s_p==='s-p-jd' && s_mn==='s-mn-ip13'" class="result">
            <div style="text-align: center;">
              <el-radio-group v-model="erb_selected">
              <el-radio-button label="erb-a" size="large">优点云图</el-radio-button>
              <el-radio-button label="erb-da" size="large">缺点云图</el-radio-button>
              </el-radio-group>
            </div>
            <div v-if="erb_selected==='erb-a'" class="result">
              <el-image v-loading="loading" src="./images/JD/iphone13/advantagesCloud.png" fit="scale-down"/>
            </div>
            <div v-else-if="erb_selected==='erb-da'" class="result">
              <el-image v-loading="loading" src="./images/JD/iphone13/disadvantagesCloud.png" fit="scale-down"/>
            </div>
            <div v-else class="result">
              <el-text type="warning" size="large">对应词云类型暂无图片</el-text>
            </div>
          </div>

          <div v-else-if="s_p==='' || s_mn===''" class="result">
            <el-text type="warning" size="large">提示：请先在上方选择平台和机型</el-text>
          </div>

          <div v-else class="result">
            <el-text type="warning" size="large">对应平台和机型暂无图片</el-text>
          </div>
        </el-tab-pane>

        <el-tab-pane name="second">
          <template #label>
            <el-text class="tab-text" type="primary" size="large">优缺点</el-text>
          </template>
          <div v-if="s_p==='s-p-jd' && s_mn==='s-mn-ip13'" class="result" style="text-align: left;">
            <el-text>优点：</el-text><br/>
            <p>{{ phonecomment['ip13'].advantage }}</p>
            <br/>
            <el-text>缺点：</el-text><br/>
            <p>{{ phonecomment['ip13'].disadvantage }}</p>
          </div>
          <div v-else-if="s_p==='' || s_mn===''" class="result">
            <el-text type="warning" size="large">提示：请先在上方选择平台和机型</el-text>
          </div>
          <div v-else class="result">
            <el-text type="warning" size="large">对应平台和机型暂无内容</el-text>
          </div>
        </el-tab-pane>

        

        <el-tab-pane name="forth">
          <template #label>
            <!-- <h1>星级统计图</h1> -->
            <el-text class="tab-text" type="primary" size="large">星级统计图</el-text>
          </template>
            <div v-if="s_p==='s-p-jd' && s_mn==='s-mn-ip13'">
              <el-image v-loading="loading" src="./images/JD/iphone13/stars.png" fit="scale-down" />
            </div>
            <div v-else-if="s_p==='' || s_mn===''" class="result">
              <el-text type="warning" size="large">提示：请先在上方选择平台和机型</el-text>
            </div>
            <div v-else class="result">
              <el-text type="warning" size="large">对应平台和机型暂无图片</el-text>
            </div>
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
        CopyRight&copy本项目小组 2023
      </el-footer>
    </el-container>
    </el-config-provider>
</template>

<style scoped>

.tab-text{
  font-size:28px;
}

#form-select{
  text-align: center;
  font-family: 'SimSun';
  position: relative;
  width:50%;
  left:25%;
}

#carousel{
  background-color: aquamarine;
}

#tab-pane{
  background-color:#F5FFFA;
  position: relative;
  width: 70%;
  left:15%;
}

#description-table *{
  font-size: 30px;
  font-family: 'SimSun';

}

.result *{
  font-size:30px;
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
