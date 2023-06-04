<script setup>
import { ref } from 'vue'

const erb_selected=ref("erb-a")
const s_mn=ref("")

const mn_list=[
  {label:'iPhone13',value:'s-mn-ip13'},
  {label:'机型A',value:'s-mn-a'},
  {label:'机型B',value:'s-mn-b'},
  {label:'机型C',value:'s-mn-c'},
]

const phoneparameters={
  's-mn-ip13': {// 此处要和mn_list里的value对应
    fullname:'Apple iPhone 13', //全名
    cpu:'A15',     // cpu型号
    size:'宽71.5mm；长146.7mm；厚7.65mm',    // 机身尺寸
    weight:'173g',  //机身重量
    memory:'128GB',  //内存
    screenpixel:'2532 x 1170', //屏幕分辨率
    screensize:'6.1英寸',  // 屏幕尺寸
    screentype:'OLED直屏',  // 屏幕材质
    charge:'20W',      // 充电功率
    os:'iOS',          // 系统
    fc_pixel:'1200万像素',    // 前摄主像素
    bc_pixel:'1200万像素',    // 后摄主像素
  },
  'template':{
    fullname:'', //全名
    cpu:'',     // cpu型号
    size:'',    // 机身尺寸
    weight:'',  //机身重量
    memory:'',  //内存
    screenpixel:'', //屏幕分辨率
    screensize:'',  // 屏幕尺寸
    screentype:'',  // 屏幕材质
    charge:'',      // 充电功率
    os:'',          // 系统
    fc_pixel:'',    // 前摄主像素
    bc_pixel:'',    // 后摄主像素
  }
}

const phonecomment={
  's-mn-ip13':  // 此处要和mn_list里的value对应
    {
      advantage:'用户觉得iPhone13运行流畅、外观好看、性价比高、质量好、拍照效果好',
      disadvantage:'用户觉得iPhone13卡顿、容易发热、电池容量小、屏幕尺寸小、声音小'
    },

}

const cloudpath={
  's-mn-ip13': {// 此处要和mn_list里的value对应
    a_imgpath:'./images/iphone13/advantagesCloud.png',
    da_imgpath:'./images/iphone13/disadvantagesCloud.png',
  }
}

const phonephoto={
  's-mn-ip13': // 此处要和mn_list里的value对应
    './images/iphone13/phone.png'
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
              <el-text size="large">选择机型：</el-text>
              <el-select  v-model="s_mn" placeholder="未选择" size="large">
                <el-option
                  v-for="item in mn_list"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </td>
          </tr>
        </table>
      </div>

      <div style="font-family:SimSun;">
        <el-image v-if="phonephoto.hasOwnProperty(s_mn)" v-loading="loading" :src="phonephoto[s_mn]" fit="scale-down"/>
        <!-- <el-empty v-else-if="s_mn===''" description="请先选择机型" />
        <el-empty v-else description="该机型无图片" /> -->
      </div>

      
      <el-tabs type="border-card" id="tab-pane" model-value="third">  
        <el-tab-pane name="third">
          <template #label>
            <el-text class="tab-text" type="primary" size="large">手机参数</el-text>
          </template>
          <div v-if="phoneparameters.hasOwnProperty(s_mn)" style="font-family: 'SimSun';text-align:left;font-size:30px">
            <p>全名：{{ phoneparameters[s_mn].fullname }}</p>
            <p>CPU型号：{{ phoneparameters[s_mn].cpu }}</p>
            <p>机身尺寸：{{ phoneparameters[s_mn].size }}</p>
            <p>机身重量：{{ phoneparameters[s_mn].weight }}</p>
            <p>内存：{{ phoneparameters[s_mn].memory }}</p>
            <p>屏幕分辨率：{{ phoneparameters[s_mn].screenpixel }}</p>
            <p>屏幕尺寸：{{ phoneparameters[s_mn].screensize }}</p>
            <p>屏幕材质：{{ phoneparameters[s_mn].screentype }}</p>
            <p>充电功率：{{ phoneparameters[s_mn].charge }}</p>
            <p>系统：{{ phoneparameters[s_mn].os }}</p>
            <p>前摄主像素：{{ phoneparameters[s_mn].fc_pixel }}</p>
            <p>后摄主像素：{{ phoneparameters[s_mn].bc_pixel }}</p>
          </div>
          <div v-else-if="s_mn===''" class="result">
            <el-empty description="提示：请先在上方选择机型" />
          </div>
          <div v-else class="result">
            <el-empty description="该机型暂无参数" />
          </div>
        </el-tab-pane>

        <el-tab-pane name="first">
          <template #label>
            <!-- <h1>好评词云</h1> -->
            <el-text class="tab-text" type="primary" size="large">评论词云</el-text>
          </template>

          <!-- 京东、iPhone13 -->
          <div v-if="cloudpath.hasOwnProperty(s_mn)" class="result">
            <div style="text-align: center;">
              <el-radio-group v-model="erb_selected">
              <el-radio-button label="erb-a" size="large">优点词云</el-radio-button>
              <el-radio-button label="erb-da" size="large">缺点词云</el-radio-button>
              </el-radio-group>
            </div>
            <div v-if="erb_selected==='erb-a'" class="result">
              <el-image v-loading="loading" :src="cloudpath[s_mn].a_imgpath" fit="scale-down"/>
            </div>
            <div v-else-if="erb_selected==='erb-da'" class="result">
              <el-image v-loading="loading" :src="cloudpath[s_mn].da_imgpath" fit="scale-down"/>
            </div>
            <div v-else class="result">
              <el-empty description="对应词云类型暂无" />
            </div>
          </div>

          <div v-else-if="s_mn===''" class="result">
            <el-empty description="提示：请先在上方选择机型" />
          </div>

          <div v-else class="result">
            <!-- <el-text type="warning" size="large">该机型暂无图片</el-text> -->
            <el-empty description="该机型暂无词云" />
          </div>
        </el-tab-pane>

        <el-tab-pane name="second">
          <template #label>
            <el-text class="tab-text" type="primary" size="large">优缺点</el-text>
          </template>
          <div v-if="phonecomment.hasOwnProperty(s_mn)" class="result" style="text-align: left;">
            <el-text>优点：</el-text><br/>
            <p>{{ phonecomment[s_mn].advantage }}</p>
            <br/>
            <el-text>缺点：</el-text><br/>
            <p>{{ phonecomment[s_mn].disadvantage }}</p>
            <br/><br/>
            <el-text type="info" size="small">注：本网站所有结论均从用户评论获取，仅供参考</el-text>
          </div>
          <div v-else-if="s_mn===''" class="result">
            <el-empty description="提示：请先在上方选择机型" />
            <!-- <el-empty description="提示：请先在上方选择机型" /> -->
          </div>
          <div v-else class="result">
            <!-- <el-empty description="该机型暂无内容" /> -->
            <el-empty description="该机型暂无内容" />
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
  width:30%;
  left:35%;
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
