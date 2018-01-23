// 初始化 layer模块
layui.use(['layer', 'laydate'], function() {
  return;
});

function showUserInfo() {
  layer.open({
    type: 1,
    skin: 'layui-layer-rim', //加上边框
    area: ['600px', '360px'],
    shadeClose: true,
    content: '\<\div style="padding:20px;">我就是大宝哥，大宝哥就是我！\<\/div>'
  });
}
