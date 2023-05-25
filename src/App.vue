<script lang="ts">
import { resolve } from 'path';


export default {
//   data: () => ({
//     gridData: [
//       { name: '优点云图', imgURL: "/5G-PHA-Display-Website/images/advantagesCloud.png", id: 'img1' },
//       { name: '缺点云图', imgURL: "/5G-PHA-Display-Website/images/disadvantagesCloud.png", id:'img2' },
//       { name: '关键词云图', imgURL: "/5G-PHA-Display-Website/images/wordcloud.png", id:'img3' },
//       { name: '评分图', imgURL: "/5G-PHA-Display-Website/images/stars.png", id:'img4' }
//     ]
//   })
}
</script>

<template>
  <div id="main">
    <h1 id="dev_hint">······开发中······</h1>
    <table id="result">
      <tr>
        <th class="name">优点云图</th>
        <th class="img"><img src="/images/advantagesCloud.png" alt='优点云图加载失败' id="img1"/></th>
      </tr>
      <tr>
        <th class="name">缺点云图</th>
        <th class="img"><img src="/images/disadvantagesCloud.png" alt='缺点云图加载失败' id="img2"/></th>
      </tr>
      <tr>
        <th class="name">关键词云图</th>
        <th class="img"><img src="/images/wordcloud.png" alt='关键词云图加载失败' id="img3"/></th>
      </tr>
      <tr>
        <th class="name">评分图</th>
        <th class="img"><img src="/images/stars.png" alt='评分图加载失败' id="img4"/></th>
      </tr>
    </table>


    <!-- <table v-for="item in gridData" id="result">
      <tr>
        <th class="name">
          {{ item.name }}
        </th>
        <th class="img">
          <img :src="item.imgURL" :alt='item.name+"加载失败"' :id="item.id"/>  
        </th>
      </tr>
    </table> -->
  </div>
  
</template>
<script>
  
</script>

<style scoped>

div#main{
  width: 100%;
  left:0;
  top:0;
  position: absolute;
  text-align: center;
}
h1#dev_hint{
    text-align: center;
    color: orange;
    font-family: "STCaiyun","Microsoft YaHei";
    font-size: 50px;
}
table#result{
  width:100%;
  text-align: center;
  border-collapse: collapse !important;
  border-style:groove;
  border-width: 8px;
  border-color: silver;
}
table#result th.name{
  width:30%;
  text-align: center;
  font-family: "STXingkai","Microsoft YaHei";
  font-size: 50px;
  border-collapse: collapse !important;
  border-right-style: groove;
  border-bottom-style: groove;
  border-width: 8px;
}
table#result th.img{
  width:70%;
  text-align: center;
  border-collapse: collapse !important;
  border-bottom-style: groove;
  border-width: 8px;
}
table#result th.img img{
  width:90%;
}
</style>
