<script lang="ts">
export default {
  data: () => ({
    gridData: [
      { name: '优点云图', imgURL: "/images/advantagesCloud.png" },
      { name: '缺点云图', imgURL: "/images/disadvantagesCloud.png" },
      { name: '关键词云图', imgURL: "/images/wordcloud.png" },
      { name: '评分图', imgURL: "/images/stars.png" }
    ]
  })
}
</script>

<template>
  <div id="left">
    <table v-for="item in gridData">
      <tr>
        <th>
          {{ item.name }}
        </th>
        <th>
          <img :src="item.imgURL" :alt="item.name">
        </th>
      </tr>
    </table>
    
  
      <!-- <img src="/images/advantagesCloud.png" alt="优点云图加载失败"/>
      <br/>
      <img src="/images/disadvantagesCloud.png" alt="缺点云图加载失败"/>
      <br/>
      <img src="/images/wordcloud.png" alt="关键词云图加载失败"/>
      <br/>
      <img src="/images/stars.png" alt="评分加载失败"/> -->
  </div>
  
</template>


<style scoped>
body{
  margin:0;
  overflow: hidden;
}
h1{
    text-align: center;
}
div#v-model-test{
  text-align: center;
}
div#v-model-test input{
  font-size: xx-large;
}
div#left{
  background-color:  gray;
  width: 100%;
  left:0;
  top:0;
  position: absolute;
  text-align: center;
}
div#left img{
  width: 50%;
}
</style>
