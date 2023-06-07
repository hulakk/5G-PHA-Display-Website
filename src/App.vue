<script setup>
import { ref } from 'vue'

const erb_selected=ref("erb-a")
const s_mn=ref("")

const mn_list=[
  {label:'iPhone 13',value:'s-mn-ip13'},
  {label:'小米 12S',value:'s-mn-xm12s'},
  {label:'Galaxy A53 5G',value:'s-mn-gxa53'},
  {label:'Galaxy S22 Ultra',value:'s-mn-gxs22'},
  {label:'iPhone 14',value:'s-mn-ip14'},
  {label:'iPhone SE3',value:'s-mn-ipse3'},
  {label:'OPPO K10x',value:'s-mn-opk10x'},
  {label:'Redmi K40S',value:'s-mn-rmk40s'},
  {label:'vivo X90',value:'s-mn-vvx90'},
]

const phoneparameters={
  's-mn-ip13': {// 此处要和mn_list里的value对应
    fullname:'Apple iPhone 13', //全名
    cpu:'A15',     // cpu型号
    size:'宽71.5mm；长146.7mm；厚7.65mm',    // 机身尺寸
    weight:'173g',  //机身重量
    memory:'128GB / 256GB / 512GB',  //内存
    screenpixel:'2532 x 1170', //屏幕分辨率
    screensize:'6.1英寸',  // 屏幕尺寸
    screentype:'OLED直屏',  // 屏幕材质
    charge:'20W',      // 充电功率
    os:'iOS',          // 系统
    fc_pixel:'1200万像素',    // 前摄主像素
    bc_pixel:'1200万像素',    // 后摄主像素
  },
  // 'template':{
  //   fullname:'', //全名
  //   cpu:'',     // cpu型号
  //   size:'',    // 机身尺寸
  //   weight:'',  //机身重量
  //   memory:'',  //内存
  //   screenpixel:'', //屏幕分辨率
  //   screensize:'',  // 屏幕尺寸
  //   screentype:'',  // 屏幕材质
  //   charge:'',      // 充电功率
  //   os:'',          // 系统
  //   fc_pixel:'',    // 前摄主像素
  //   bc_pixel:'',    // 后摄主像素
  // },
  's-mn-xm12s':{
    fullname:'小米 12S', //全名
    cpu:'骁龙8+ Gen 1',     // cpu型号
    size:'宽69.9mm；长152.7mm；厚8.16mm',    // 机身尺寸
    weight:'182g',  //机身重量
    memory:'8GB+256GB / 12GB+256GB / 12GB+512GB',  //内存
    screenpixel:'2400*1080', //屏幕分辨率
    screensize:'6.28英寸',  // 屏幕尺寸
    screentype:'OLED',  // 屏幕材质
    charge:'67W',      // 充电功率
    os:'Android',          // 系统
    fc_pixel:'3200万像素',    // 前摄主像素
    bc_pixel:'5000万像素',    // 后摄主像素
  },
  's-mn-gxa53':{
    fullname:'三星 Galaxy A53 5G', //全名
    cpu:'Exynos系列',     // cpu型号
    size:'宽159.6mm；长74.8mm；厚8.1mm',    // 机身尺寸
    weight:'189g',  //机身重量
    memory:'8GB+128GB / 8GB+256GB',  //内存
    screenpixel:'1080 x 2400 (FHD+)', //屏幕分辨率
    screensize:'6.5英寸',  // 屏幕尺寸
    screentype:'OLED直屏',  // 屏幕材质
    charge:'25W',      // 充电功率
    os:'Android',          // 系统
    fc_pixel:'3200万像素',    // 前摄主像素
    bc_pixel:'6400万像素',    // 后摄主像素
  },
  's-mn-gxs22':{
    fullname:'三星 Galaxy S22 Ultra', //全名
    cpu:'骁龙8 Gen 1',     // cpu型号
    size:'宽77.9mm；长163.3mm；厚8.9mm',    // 机身尺寸
    weight:'228g',  //机身重量
    memory:'12GB+256GB / 12GB+512GB',  //内存
    screenpixel:'3088 x 1440(QHD+)', //屏幕分辨率
    screensize:'6.8英寸',  // 屏幕尺寸
    screentype:'OLED曲面屏',  // 屏幕材质
    charge:'45W',      // 充电功率
    os:'Android',          // 系统
    fc_pixel:'4000万像素',    // 前摄主像素
    bc_pixel:'10800万像素',    // 后摄主像素
  },
  's-mn-ip14':{
    fullname:'Apple iPhone 14', //全名
    cpu:'A15',     // cpu型号
    size:'宽71.5mm；长146.7mm；厚7.8mm',    // 机身尺寸
    weight:'172g',  //机身重量
    memory:'128GB / 256GB / 512GB',  //内存
    screenpixel:'2532 x 1170', //屏幕分辨率
    screensize:'6.1英寸',  // 屏幕尺寸
    screentype:'OLED直屏',  // 屏幕材质
    charge:'20W',      // 充电功率
    os:'iOS',          // 系统
    fc_pixel:'1200万像素',    // 前摄主像素
    bc_pixel:'1200万像素',    // 后摄主像素
  },
  's-mn-ipse3':{
    fullname:'Apple iPhone SE3', //全名
    cpu:'A15',     // cpu型号
    size:'宽67.3mm；长138.4mm；厚7.3mm',    // 机身尺寸
    weight:'144g',  //机身重量
    memory:'64GB / 128GB / 256GB',  //内存
    screenpixel:'1334 x 750 像素分辨率，326 ppi', //屏幕分辨率
    screensize:'4.7英寸',  // 屏幕尺寸
    screentype:'OLED',  // 屏幕材质
    charge:'20W',      // 充电功率
    os:'iOS',          // 系统
    fc_pixel:'1200万像素',    // 前摄主像素
    bc_pixel:'1200万像素',    // 后摄主像素
  },
  's-mn-opk10x':{
    fullname:'OPPO K10x', //全名
    cpu:'骁龙695',     // cpu型号
    size:'宽75.6mm；长164.3mm；厚8.5mm',    // 机身尺寸
    weight:'195g',  //机身重量
    memory:'8GB+128GB / 8GB+256GB / 12GB+256GB',  //内存
    screenpixel:'2412×1080', //屏幕分辨率
    screensize:'6.59英寸',  // 屏幕尺寸
    screentype:'LCD',  // 屏幕材质
    charge:'67W',      // 充电功率
    os:'Android',          // 系统
    fc_pixel:'1600万像素',    // 前摄主像素
    bc_pixel:'6400万像素',    // 后摄主像素
  },
  's-mn-rmk40s':{
    fullname:'小米 Redmi K40S', //全名
    cpu:'骁龙 870',     // cpu型号
    size:'宽75.95mm；长163.2mm；厚7.7mm',    // 机身尺寸
    weight:'195g',  //机身重量
    memory:'8GB+128GB / 8GB+256GB / 12GB+256GB',  //内存
    screenpixel:'2400 X 1080 FHD+', //屏幕分辨率
    screensize:'AMOLED',  // 屏幕尺寸
    screentype:'以官网信息为准(京东无数据)',  // 屏幕材质
    charge:'67W',      // 充电功率
    os:'Android',          // 系统
    fc_pixel:'2000万像素',    // 前摄主像素
    bc_pixel:'4800万像素',    // 后摄主像素
  },
  's-mn-vvx90':{
    fullname:'vivo X90', //全名
    cpu:'天玑9200',     // cpu型号
    size:'宽74.44mm；长164.1mm；厚8.48mm',    // 机身尺寸
    weight:'200g',  //机身重量
    memory:'8GB+128GB / 8GB+256GB / 12GB+256GB / 12GB+512GB',  //内存
    screenpixel:'2800 × 1260', //屏幕分辨率
    screensize:'6.78英寸',  // 屏幕尺寸
    screentype:'AMOLED',  // 屏幕材质
    charge:'120W',      // 充电功率
    os:'Android',          // 系统
    fc_pixel:'3200万像素',    // 前摄主像素
    bc_pixel:'5000万像素',    // 后摄主像素
  },

}

const phonecomment={
  's-mn-ip13':  // 此处要和mn_list里的value对应
    {
      advantage:'iPhone 13 运行流畅、外观好看、性价比高、质量好、拍照效果好',
      disadvantage:'iPhone 13 卡顿、容易发热、电池容量小、屏幕尺寸小、声音小'
    },
  's-mn-xm12s':{
      advantage:'小米12S 运行流畅、外观好看、性价比高、质量好、拍照好',
      disadvantage:'小米12S 卡顿、容易发热、容易卡相机、屏幕尺寸小、声音小',
    },
  's-mn-gxa53':{
      advantage:'Galaxy A53 5G 运行流畅、外观漂亮、性价比高、质量好、拍照效果好',
      disadvantage:'Galaxy A53 5G 卡顿、容易发热、耗电、充电慢、反应慢',
    },
  's-mn-gxs22':{
      advantage:'Galaxy S22 Ultra 运行流畅、外观漂亮、屏幕好、质量好、性价比高',
      disadvantage:'Galaxy S22 Ultra 容易发热、卡顿、耗电、充电慢、容易死机',
    },
  's-mn-ip14':{
      advantage:'iPhone 14 运行流畅、外观好看、运行速度很快、质量好、拍照效果好',
      disadvantage:'iPhone 14 卡顿、容易发热、内存不够、耗电、画面失真、续航差',
    },
  's-mn-ipse3':{
      advantage:'iPhone SE3 运行流畅、外观好看、性价比高、拍照效果好',
      disadvantage:'iPhone SE3 屏幕小、容易发热、容易死机、卡顿、声音小、质量差',
    },
  's-mn-opk10x':{
      advantage:'OPPO K10x 运行流畅、外观好看、性价比高、充电快、质量好、拍照效果好',
      disadvantage:'OPPO K10x 卡顿、画面模糊、容易发热、反应速度慢、耗电快',
    },
  's-mn-rmk40s':{
      advantage:'Redmi K40S 运行流畅、性价比高、外观好看、质量好、充电快',
      disadvantage:'Redmi K40S 卡顿、容易发热、耗电、电池容量小、反应慢、容易死机、画面失真',
    },
  's-mn-vvx90':{
      advantage:'vivo X90 运行流畅、外观好看、充电速度快、拍照效果好',
      disadvantage:'vivo X90 容易发热、卡顿、耗电、容易死机、画面模糊、内存容量小',
    },
}

const cloudpath={
  's-mn-ip13': {// 此处要和mn_list里的value对应
    a_imgpath:'./images/output/iphone 13/advantagesCloud.png',
    da_imgpath:'./images/output/iphone 13/disadvantagesCloud.png',
  },
  's-mn-xm12s':{
    a_imgpath:'./images/output/小米12S/advantagesCloud.png',
    da_imgpath:'./images/output/小米12S/disadvantagesCloud.png',
  },
  's-mn-gxa53':{
    a_imgpath:'./images/output/Gala A53 5G/advantagesCloud.png',
    da_imgpath:'./images/output/Gala A53 5G/disadvantagesCloud.png',
  },
  's-mn-gxs22':{
    a_imgpath:'./images/output/Galaxy S22 Ultra/advantagesCloud.png',
    da_imgpath:'./images/output/Galaxy S22 Ultra/disadvantagesCloud.png',
  },
  's-mn-ip14':{
    a_imgpath:'./images/output/iphone 14/advantagesCloud.png',
    da_imgpath:'./images/output/iphone 14/disadvantagesCloud.png',
  },
  's-mn-ipse3':{
    a_imgpath:'./images/output/iphoneSE/advantagesCloud.png',
    da_imgpath:'./images/output/iphoneSE/disadvantagesCloud.png',
  },
  's-mn-opk10x':{
    a_imgpath:'./images/output/oppo K10x/advantagesCloud.png',
    da_imgpath:'./images/output/oppo K10x/disadvantagesCloud.png',
  },
  's-mn-rmk40s':{
    a_imgpath:'./images/output/Redmi K40S/advantagesCloud.png',
    da_imgpath:'./images/output/Redmi K40S/disadvantagesCloud.png',
  },
  's-mn-vvx90':{
    a_imgpath:'./images/output/vivo X90/advantagesCloud.png',
    da_imgpath:'./images/output/vivo X90/disadvantagesCloud.png',
  },

}

const phonephoto={
  's-mn-ip13': // 此处要和mn_list里的value对应
    './images/PhoneAppearance/iPhone13.png',
  's-mn-xm12s':
    './images/PhoneAppearance/Xiaomi12S.png',
  's-mn-gxa53':
    './images/PhoneAppearance/Galaxy_A53_5G.png',
  's-mn-gxs22':
    './images/PhoneAppearance/Galaxy_S22_Ultra.png',
  's-mn-ip14':
    './images/PhoneAppearance/iPhone14.png',
  's-mn-ipse3':
    './images/PhoneAppearance/iPhoneSE.png',
  's-mn-opk10x':
    './images/PhoneAppearance/OPPO_K10x.png',
  's-mn-rmk40s':
    './images/PhoneAppearance/Redmi_K40S.png',
  's-mn-vvx90':
    './images/PhoneAppearance/vivo_X90.png',
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
        <br/>
        <el-image v-if="phonephoto.hasOwnProperty(s_mn)" v-loading="loading" :src="phonephoto[s_mn]" fit="scale-down"/>
        <!-- <el-empty v-else-if="s_mn===''" description="请先选择机型" />
        <el-empty v-else description="该机型无图片" /> -->
        <br/>
        <br/>
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
              <br/><br/>
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
            <p>用户提及最多的优点包括 {{ phonecomment[s_mn].advantage }}</p>
            <br/>
            <el-text>缺点：</el-text><br/>
            <p>用户提及最多的缺点包括 {{ phonecomment[s_mn].disadvantage }}</p>
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

#tab-pane{
  background-color:#F5FFFA;
  position: relative;
  width: 70%;
  left:15%;
}
html.dark #tab-pane{
  background-color:#252726;
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
