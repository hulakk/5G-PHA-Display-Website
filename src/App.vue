<script lang="ts">


export default {
  data: () => ({
    gridData: [
      { name: '优点云图', imgURL: "./assest/images/advantagesCloud.png" },
      { name: '缺点云图', imgURL: "./assest/images/disadvantagesCloud.png" },
      { name: '关键词云图', imgURL: "./assest/images/wordcloud.png" },
      { name: '评分图', imgURL: "./assest/images/stars.png" }
    ]
  })
}
</script>

<template>
  <div id="main">
    <h1 id="dev_hint">······开发中······</h1>
    <table v-for="item in gridData" id="result">
      <tr>
        <th id="name">
          {{ item.name }}
        </th>
        <th id="img">
          <img :src="item.imgURL" :alt='item.name+"加载失败"'>
        </th>
      </tr>
    </table>
  </div>
  
</template>


<style scoped>
/* body{
  margin:0;
  overflow: hidden;
} */

div#main{
  /* background-color:  gray; */
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
}
table#result{
  width:100%;
  text-align: center;
}
table#result th#name{
  width:30%;
  text-align: center;
  font-family: "STXingkai","Microsoft YaHei";
  font-size: 50px;
  border-width:8px;
  border-style: groove;
  border-collapse: collapse;
  border-spacing: 0;
}
table#result th#img{
  width:70%;
  text-align: center;
  border-width:8px;
  border-style: groove;
  border-collapse: collapse;
  border-spacing: 0;
}
table#result th#img img{
  width:90%;
}
</style>
